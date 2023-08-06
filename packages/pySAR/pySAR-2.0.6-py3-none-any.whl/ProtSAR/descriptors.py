
#########################################################################
###                         Descriptors                               ###
#########################################################################

# Copyright (c) 2016-2017, Zhijiang Yao, Jie Dong and Dongsheng Cao
# All rights reserved.
import pandas as pd
import numpy as np
import datetime, time
import argparse
import itertools
import pickle
import yaml
import io
import os
import time
from difflib import get_close_matches
import json
from tqdm import tqdm
from sklearn.preprocessing import StandardScaler

from globals import OUTPUT_DIR, OUTPUT_FOLDER, DATA_DIR
from aaindex import  AAIndex
from model import Model
from proDSP import ProDSP
from evaluate import Evaluate
from ProtSAR import ProtSAR
import utils as utils
from PyBioMed.PyBioMed.PyProtein import AAComposition, Autocorrelation, CTD, ConjointTriad, QuasiSequenceOrder, PseudoAAC

#show progress of each descriptor calculation - https://pypi.org/project/progress/
class Descriptors():

    # """
    # Digital Signal Processing on protein sequences. Transform protein sequences into their spectral form
    # via an Fast Fourier Transform (FFT). The output of a Fourier Transform is a complex number C made up of
    # an imaginary I and real R component. **what does an FFT do??
    #
    # Parameters
    # ----------
    # protein_sequences : numpy array
    #     array of protein sequences e.g MTIKEMPQPKTFGELKNLPLLNTDKP.
    # desc_dataset : str
    #     name of descriptors file storing previously calculated descriptors from
    #     the protein sequences. By default the class will search for a descriptors
    #     file called "descriptors.csv" in the 'data' directory. If it finds a file
    #     from the value put into desc_dataset then the descriptor values will be
    #     imported rather than calculated.
    # window : str
    #     window function to apply to the output of the FFT.
    # filter: str
    #     filter function to apply to the output of the FFT.
    #
    # Returns
    # -------
    #
    # """

    def __init__(self, protein_seqs, desc_dataset="descriptors.csv", all_desc=False):

        self.protein_seqs = protein_seqs
        #remove any gaps from protein sequences
        self.protein_seqs = utils.remove_gaps(self.protein_seqs)
        #assert that all gaps have been removed from the sequences
        assert '-' not in self.protein_seqs, 'Gaps (-) still found in dataset'

        #validate that all inputtted protein sequences are valid and only contain
        #valid amino acids, if not then raise ValueError
        invalid_seqs = utils.valid_sequence(self.protein_seqs)
        if invalid_seqs!=None:
            raise ValueError('Invalid Amino Acids found in protein sequence dataset: {}'.format(invalid_seqs))

        #get the total number of inputted protein sequences
        self.num_seqs = len(self.protein_seqs)

        self.all_desc = all_desc

        self.aa_composition = pd.DataFrame()
        self.dipeptide_composition = pd.DataFrame()
        self.tripeptide_composition = pd.DataFrame()
        self.normalized_moreaubroto_autocorrelation = pd.DataFrame()
        self.moran_autocorrelation = pd.DataFrame()
        self.geary_autocorrelation = pd.DataFrame()
        self.CTD = pd.DataFrame()
        self.composition = pd.DataFrame()
        self.transition = pd.DataFrame()
        self.distribution = pd.DataFrame()
        self.conjoint_triad = pd.DataFrame()
        self.seq_order_coupling_number = pd.DataFrame()
        self.quasi_seq_order = pd.DataFrame()
        self.pseudo_AAC = pd.DataFrame()
        self.amp_pseudo_AAC = pd.DataFrame()
        self.all_descriptors = pd.DataFrame()

        self.desc_dataset = os.path.join(DATA_DIR, desc_dataset)
        if os.path.isfile(self.desc_dataset):
            self.import_descriptors(self.desc_dataset)
        else:
            #initialise all descriptor variables to empty dataframes


            #if all_desc parameter true then calculate all descriptor value and store
            #in their respective instance variables
            if all_desc:
                self.all_descriptors = self.get_all_descriptors()
                self.all_descriptors.to_csv(os.path.join(DATA_DIR, 'descriptors.csv'))

    def import_descriptors(self, descriptor_file):

        """
        By default, the class will search for a file in the DATA_DIR called
        desciptors_(desc_dataset).csv with ALL ofthe pre-calculated descriptor values.
        This function parses this file and sets the descriptor instance variables
        to the correct features. The descriptors file should be of size N x 9920,
        where N is the number of protein sequences in the dataset, the method does
        not work if the file is not of this size. To create an descriptors file,
        create an instance of the desc class, with the parameter all_desc=True; this
        will calculate all descriptors and store them to the DATA_DIR.

        Returns
        -------

        """
        print('Importing Descriptors File....')

        try:
            descriptor_df = pd.read_csv(descriptor_file)
        except IOError:
            print('Error opening descriptor file: {}'.format(descriptor_file))
            return None

        assert descriptor_df.shape == (self.num_seqs, 10030), 'Descriptors \
            file must be of the shape ({}X10,030) such that all descriptor values can \
            be parsed from the file'.format(self.num_seqs)

        #replacing +/- infinity or NAN values with 0
        descriptor_df.replace([np.inf, -np.inf], np.nan)
        descriptor_df = descriptor_df.fillna(0)

        self.aa_composition = descriptor_df.iloc[:,: 20]
        self.dipeptide_composition = descriptor_df.iloc[:,20:420]
        self.tripeptide_composition = descriptor_df.iloc[:,420:8420]
        self.normalized_moreaubroto_autocorrelation = descriptor_df.iloc[:,8420:8660]
        self.moran_autocorrelation = descriptor_df.iloc[:,8660: 8900]
        self.geary_autocorrelation = descriptor_df.iloc[:,8900:9140]
        self.CTD =  descriptor_df.iloc[:,9140:9287] #split into C, T and D? **check conjoint - should it be 512?
        self.composition = descriptor_df.iloc[:,9140:9161]
        self.transition = descriptor_df.iloc[:,9161:9182]
        self.distribution = descriptor_df.iloc[:,9182:9287]
        # self.conjoint_triad = descriptor_df.iloc[:,9287:9630]
        # self.seq_order_coupling_number = descriptor_df.iloc[:,9630:9690]    **this should be one?
        # self.quasi_seq_order = descriptor_df.iloc[:,9690:9790]      100
        # self.pseudo_AAC = descriptor_df.iloc[:,9790:9840]   50
        # self.amp_pseudo_AAC = descriptor_df.iloc[:,9840:9920]       80
        # self.all_descriptors = descriptor_df.iloc[:,:]
        self.conjoint_triad = descriptor_df.iloc[:,9287:9799]
        self.seq_order_coupling_number = descriptor_df.iloc[:,9799:9800]
        self.quasi_seq_order = descriptor_df.iloc[:,9800:9900]
        self.pseudo_AAC = descriptor_df.iloc[:,9900:9950]
        self.amp_pseudo_AAC = descriptor_df.iloc[:,9950:10030]
        self.all_descriptors = descriptor_df.iloc[:,:]

    def get_aa_composition(self):

        """
        Calculate Amino Acid Composition (AA_Comp) of protein sequences. AA_comp
        describes the fraction of each amino acid type within a protein sequence,
        and is calculated as:
        AA_Comp(s) = AA(t)/N(s)

        where AA_Comp(s) is the AA_comp of protein sequence s, AA(t) is the number
        of amino acid types t (where t = 1,2,..,20) and N(s) is the length of the
        sequence s.

        Returns
        -------
        aa_comp_df : pd.DataFrame
            dataframe of AA composition for all protein sequences. DataFrame will
            be of the shape N x 20, where N is the number of protein sequences and
            20 is the number of features calcualted from the descriptor (for the
            20 amino acids).

        """
        print('\nGetting AA Composition Descriptors...')
        print('#####################################\n')
        AA_comp = []

        aa_comp = []
        #get feature names for AAComp descriptor
        aa = list((AAComposition.CalculateAAComposition(self.protein_seqs[0])).keys())

        #iterate through all sequences, calculate descriptor values and append to
        #AA_Comp list
        time.sleep(1)
        for seq in tqdm(self.protein_seqs,unit=" sequences",position=0,desc="Amid Composition"):
            # AAComp=AAComposition.CalculateAAComposition([seq])
            AAComp=AAComposition.CalculateAAComposition(seq)
            aa_comp.append(list(AAComp.values()))

        #convert calculated AAComp values into dataframe
        aa_comp_df = pd.DataFrame(data=aa_comp, columns=aa)

        self.aa_composition = aa_comp_df

        return aa_comp_df

    def get_dipeptide_composition(self):

        """
        Calculate Dipeptide Composition (Dipeptide_Comp) of protein sequences.
        Dipeptide composition is the fraction of each dipeptide type within a
        protein sequence. With dipeptides being of length 2 and there being 20
        canonical amino acids this creates 20^2 different combinations, thus a
        400-Dimensional vector will be produced such that:

        Dipeptide_Comp(s,t) = AA(s,t) / N -1

        where Dipeptide_Comp(s,t) is the dipeptide composition of the protein sequence
        for amino acid type s and t (where s and t = 1,2,..,20), AA(s,t) is the number
        of dipeptides represented by amino acid type s and t and N is the total number
        of dipeptides.

        Returns
        -------
        dipeptide_comp_df : pd.DataFrame
            dataframe of dipeptide composition for all protein sequences. DataFrame will
            be of the shape N x 400, where N is the number of protein sequences and
            400 is the number of features calcualted from the descriptor (20^2 for
            the 20 canonical amino acids).

        """
        print('\nGetting Dipeptide Composition Descriptors...')
        print('############################################\n')

        dipeptide_comp = []
        #get feature names for Dipeptide_comp descriptor
        dipeptides = list((AAComposition.CalculateDipeptideComposition(self.protein_seqs[0])).keys())

        #iterate through all sequences, calculate descriptor values and append to
        #dipeptide_comp list
        time.sleep(1)
        for seq in tqdm(self.protein_seqs,unit=" sequences",position=0,desc="Dipeptide Composition"):
            AADipeptide=AAComposition.CalculateDipeptideComposition(seq)
            dipeptide_comp.append(list(AADipeptide.values()))

        dipeptide_comp_df = pd.DataFrame(data=dipeptide_comp, columns=dipeptides)

        self.dipeptide_composition = dipeptide_comp_df

        #convert calculated Dipeptide_comp values into dataframe
        return dipeptide_comp_df

    def get_tripeptide_composition(self):

        """
        Calculate Tripeptide Composition (Tripetide_Comp) of protein sequences.
        Tripeptide composition is the fraction of each tripeptide type wihin a
        protein sequence. With dipeptides being of length 3 and there being 20
        canonical amino acids this creates 20^3 different combinations, thus a
        8000-Dimensional vector will be produced such that:

        Tripetide_Comp(s,t,u) = AA(s,t,u) / N -1

        where Tripetide_Comp(s,t,u) is the tripeptide composition of the protein sequence
        for amino acid type s, t and u (where s, t and u = 1,2,..,20), AA(s,t,u) is
        the numberof tripeptides represented by amino acid type s and t and N is
        the total number of tripeptides.

        Returns
        -------
        tripeptide_df : pd.DataFrame
            dataframe of tripeptide composition for all protein sequences. DataFrame will
            be of the shape N x 8000, where N is the number of protein sequences and
            8000 is the number of features calcualted from the descriptor (20^3 for
            the 20 canonical amino acids).

        """
        print('\nGetting Tripeptide Composition Descriptors...')
        print('#############################################\n')

        tripeptide_comp = []
        #get feature names for Tripeptide_comp descriptor
        tripeptides = list((AAComposition.GetSpectrumDict(self.protein_seqs[0])).keys())

        #iterate through all sequences, calculate descriptor values and append to
        #tripeptide_comp list
        for seq in tqdm(self.protein_seqs,unit=" sequences",position=0,desc="Tripeptide Comp"):
            AATripeptide=AAComposition.GetSpectrumDict(seq)
            tripeptide_comp.append(list(AATripeptide.values()))

        #convert calculated Tripeptide_comp values into dataframe
        tripeptide_comp_df = pd.DataFrame(data=tripeptide_comp, columns=tripeptides)

        self.tripeptide_composition = tripeptide_comp_df

        return tripeptide_comp_df

    def get_autocorrelation(self, aa_encoding=Autocorrelation._AAProperty, aa_name=Autocorrelation._AAPropertyName):

        """
        #Autocorrelation output is of shape N x 240.
        Calculate Normalized MoreauBrotoAuto Autocorrelation () of protein sequences.
        Norm_MoreauBroto (also known as Autocorrelation of a topoloigical structure ATS)
        describes how a property is distributed along the topological structure of a
        protein sequence.

        AC(d) = \sum_{i=1}^{N-d} P_i P_{i + d} \quad d = 1, 2, \ldots, \textrm{nlag}

        where d is called the lag of the autocorrelation; Pi and Pi+d are the properties of
        the amino acids at position i and i+d; nlag is the maximum value of the lag.

        Parameters
        ----------
        aa_encoding: dict
            dict of amino acid and their AAI index properties used to build the
            descriptor, defaultAutocorrelation._AAProperty is a list of the
            most used indices used: _AAProperty = (_Hydrophobicity,_AvFlexibility
            ,_Polarizability,_FreeEnergy,_ResidueASA,_ResidueVol,_Steric,_Mutability).

            Default AAI used building descriptor:
            AccNo. CIDH920105 - Normalized Average Hydrophobicity Scales
            AccNo. BHAR880101 - Average Flexibility Indices
            AccNo. CHAM820101 - Polarizability Parameter
            AccNo. CHAM820102 - Free Energy of Solution in Water, kcal/mole
            AccNo. CHOC760101 - Residue Accessible Surface Area in Tripeptide
            AccNo. BIGC670101 - Residue Volume
            AccNo. CHAM810101 - Steric Parameter
            AccNo. DAYM780201 - Relative Mutability

        aa_name: str
            string representing the AAI index name used for building descriptor,
            default Autocorrelation._AAPropertyName reflects the aa_encoding
            default values: _AAPropertyName = ("_Hydrophobicity","_AvFlexibility",
            "_Polarizability","_FreeEnergy","_ResidueASA","_ResidueVol","_Steric",
            "_Mutability")

        Returns
        -------
        norm_moreaubroto_autocorr_df : pd.DataFrame
            dataframe of Norm_MoreauBroto autocorrelation for all protein sequences.
            DataFrame will be of the shape N x X, where N is the number of protein
            sequences and X is the number of features calcualted from the descriptor
            (20^3 for the 20 canonical amino acids).

        """

        print('\nGetting Autocorrelation Descriptors...')
        print('######################################\n')

        norm_moreaubroto_autocorr = []
        norm_moreaubroto_autocorr_keys = []
        norm_moreaubroto_autocorr_values = []

        moran_autocorr = []
        moran_autocorr_keys = []
        moran_autocorr_values = []

        geary_autocorr = []
        geary_autocorr_keys = []
        geary_autocorr_values = []

        #iterate through protein sequences and calculate the Norm_MoreauBroto for each, append to list of values
        for seq in tqdm(self.protein_seqs,unit=" sequences",position=0,desc="Autocorrelation"):
            normMoreauBroto = Autocorrelation.CalculateNormalizedMoreauBrotoAuto(seq, aa_encoding,aa_name)
            norm_moreaubroto_autocorr.append(normMoreauBroto)
            moranautocorr = Autocorrelation.CalculateMoranAuto(seq, aa_encoding,aa_name)
            moran_autocorr.append(moranautocorr)
            gearyautocorr = Autocorrelation.CalculateGearyAuto(seq, aa_encoding,aa_name)
            geary_autocorr.append(gearyautocorr)

        #get keys/column names generated from the descriptor calculation
        for name in range(0,len(aa_name)):
          norm_moreaubroto_autocorr_keys.append(list(norm_moreaubroto_autocorr[0][aa_name[name]].keys()))
          moran_autocorr_keys.append(list(moran_autocorr[0][aa_name[name]].keys()))
          geary_autocorr_keys.append(list(geary_autocorr[0][aa_name[name]].keys()))

        # norm_moreaubroto_autocorr_keys = ([item for sublist in norm_moreaubroto_autocorr_keys for item in sublist])
        #flatten column names/keys into 1 1-D list
        norm_moreaubroto_autocorr_keys = utils.flatten(norm_moreaubroto_autocorr_keys)
        moran_autocorr_keys = utils.flatten(moran_autocorr_keys)
        geary_autocorr_keys = utils.flatten(geary_autocorr_keys)

        '''
        Reformatting the output of the descriptor from the PyBioMed package.
        The PyBioMed descriptor function returns a dict of dicts of the resultant
        values. For uniformity with the rest of the descriptor calculations,
        this output is transformed such that it can be output into a dataframe.
        '''

        #check length norm_moreaubroto_autocorr = moran_autocorr = geary_autocorr
        for x in range(0,len(list(norm_moreaubroto_autocorr))):
            for y in range(0,len(list(norm_moreaubroto_autocorr[x].values()))):
                norm_moreaubroto_autocorr_values.append(list((list((list(norm_moreaubroto_autocorr)[x]).values()))[y].values()))
                moran_autocorr_values.append(list((list((list(moran_autocorr)[x]).values()))[y].values()))
                geary_autocorr_values.append(list((list((list(geary_autocorr)[x]).values()))[y].values()))

        #flatten list of lists of the correlation values
        norm_moreaubroto_autocorr_values = utils.flatten(norm_moreaubroto_autocorr_values)
        moran_autocorr_values = utils.flatten(moran_autocorr_values)
        geary_autocorr_values = utils.flatten(geary_autocorr_values)

        # norm_moreaubroto_autocorr_values =  np.array([item for sublist in norm_moreaubroto_autocorr_values for item in sublist])
        #reshape into N x M array where N is the number of protein sequences and M is the number of AA properties used in the correlation
        norm_moreaubroto_autocorr_values_ = np.reshape(norm_moreaubroto_autocorr_values, (len(self.protein_seqs),len(norm_moreaubroto_autocorr_keys)))
        moran_autocorr_values_ = np.reshape(moran_autocorr_values, (len(self.protein_seqs),len(moran_autocorr_keys)))
        geary_autocorr_values_ = np.reshape(geary_autocorr_values, (len(self.protein_seqs),len(geary_autocorr_keys)))


        #convert Autocorrelation array values into a dataframe
        norm_moreaubroto_autocorr_df = pd.DataFrame(data=norm_moreaubroto_autocorr_values_, columns=norm_moreaubroto_autocorr_keys)
        moran_autocorr_df = pd.DataFrame(data=moran_autocorr_values_, columns=moran_autocorr_keys)
        geary_autocorr_df = pd.DataFrame(data=geary_autocorr_values_, columns=geary_autocorr_keys)

        self.normalized_moreaubroto_autocorrelation = norm_moreaubroto_autocorr_df
        self.moran_autocorrelation = moran_autocorr_df
        self.geary_autocorrelation = geary_autocorr_df

        return norm_moreaubroto_autocorr_df,moran_autocorr_df,geary_autocorr_df

    def get_ctd(self):

        """
        Calculate Composition, transition and distribution (CTD) of protein sequences.
        CTD is ...

        Returns
        -------
        ctd_df : pd.DataFrame

        """
        print('\nGetting CTD Descriptors...')
        print('##########################\n')

        ctd = []
        #get feature names for CTD descriptor
        keys = list((CTD.CalculateCTD(self.protein_seqs[0])).keys())

        #iterate through all sequences, calculate descriptor values and append to
        #ctd list
        time.sleep(1)
        for seq in tqdm(self.protein_seqs,unit=" sequences",position=0,desc="CTD"):
            ctd_=CTD.CalculateCTD(seq)
            ctd.append(list(ctd_.values()))

        #convert calculated ctd values into dataframe
        ctd_df = pd.DataFrame(data=ctd, columns=keys)

        self.CTD = ctd_df
        self.composition = ctd_df.iloc[:,:21]
        self.transition = ctd_df.iloc[:, 21: 42]
        self.distribution = ctd_df.iloc[:, 42: ]

        return ctd_df

    def get_conjoint_triad(self):

        """
        Calculate Conjoint Triad features for the protein sequences.
        Conjoint Triad is ...

        Returns
        -------
        ct_df : pd.DataFrame

        """
        print('\nGetting Conjoint Triad Descriptors...')
        print('##################################\n')

        ct = []
        #get feature names for CT descriptor
        keys = list((ConjointTriad.CalculateConjointTriad(self.protein_seqs[0])).keys())

        #iterate through all sequences, calculate descriptor values and append to
        #ct list
        for seq in tqdm(self.protein_seqs,unit=" sequences",position=0,desc="Conjoint Triad"):

            conTri=ConjointTriad.CalculateConjointTriad(seq)
            ct.append(list(conTri.values()))

        #convert calculated CT values into dataframe
        ct_df = pd.DataFrame(data=ct, columns=keys)

        self.conjoint_triad = ct_df

        return ct_df

    def get_seq_order_coupling_number(self):

        """
        Calculate Sequence Order Coupling Number features for the protein sequences.
        Sequence Order Coupling Number  is ...

        Returns
        -------
        seq_order_df : pd.DataFrame

        """
        print('\nGetting Sequence Order Coupling Descriptors...')
        print('#############################################\n')

        seq_order = []

        #iterate through all sequences, calculate descriptor values and append to
        #seq_order list
        for seq in tqdm(self.protein_seqs,unit=" sequences",position=0,desc="Sequence Order Coupling Number"):
            seq_order_num = QuasiSequenceOrder.GetSequenceOrderCouplingNumber(seq)
            seq_order.append(seq_order_num)

        #convert calculated seq_order values into dataframe
        seq_order_df = pd.DataFrame(data=seq_order)

        self.seq_order_coupling_number = seq_order_df

        return seq_order_df

    def get_quasi_seq_order(self):

        """
        Calculate Quasi Sequence Order features for the protein sequences.
        Quasi Sequence Order  is ...

        Returns
        -------
        quasi_seq_order_df : pd.DataFrame

        """
        print('\nGetting Quasi Sequence Order Descriptors...')
        print('###########################################\n')

        quasi_seq_order = []
        #get feature names for QuasiSeqOrder descriptor
        keys = list((QuasiSequenceOrder.GetQuasiSequenceOrder(self.protein_seqs[0])).keys())

        #iterate through all sequences, calculate descriptor values and append to
        #quasi_seq_order list
        for seq in tqdm(self.protein_seqs,unit=" sequences",position=0,desc="Quasi Sequence Order"):
            quasi_seq=QuasiSequenceOrder.GetQuasiSequenceOrder(seq)
            quasi_seq_order.append(list(quasi_seq.values()))

        #convert calculated quasi_seq_order values into dataframe
        quasi_seq_order_df = pd.DataFrame(data=quasi_seq_order, columns=keys)

        self.quasi_seq_order = quasi_seq_order_df

        return quasi_seq_order_df

    def get_pseudo_AAC(self, AAP=[PseudoAAC._Hydrophobicity]):

        """
        Calculate pseudo Amino Acid Composition features for the protein sequences.
        PsuedoAAComp is ...

        Returns
        -------
        psuedo_AAComp_df : pd.DataFrame

        """
        print('\nGetting Psuedo Amino Acid Composition Descriptors...')
        print('####################################################\n')

        psuedoAAComp = []
        #get feature names for PsuedoAAComp descriptor
        keys = (list(pseudoAAC.GetPseudoAAC(self.protein_seqs[0], AAP=AAP).keys()))

        #iterate through all sequences, calculate descriptor values and append to
        #psuedoAAComp list
        for seq in tqdm(self.protein_seqs,unit=" sequences",position=0,desc="Psuedo Amino Acid Composition"):
            psuedoAA=pseudoAAC.GetPseudoAAC(seq, AAP=AAP)
            psuedoAAComp.append(list(psuedoAA.values()))

        #convert calculated PsuedoAAComp values into dataframe
        psuedo_AAComp_df = pd.DataFrame(data=psuedoAAComp, columns=keys)

        self.pseudo_AAC = psuedo_AAComp_df

        return psuedo_AAComp_df

    def get_amp_pseudo_AAC(self):

        """
        Calculate type I pseudo-amino acid compostion features for the protein sequences.
        APsuedo_AAComp is ...

        Returns
        -------
        amp_pseudo_AAComp_df : pd.DataFrame

        """
        print('\nGetting Amphiphilic Amino Acid Composition Descriptors...')
        print('#########################################################\n')

        amp_pseudo_AAComp = []
        keys = list((PseudoAAC.GetAPseudoAAC(self.protein_seqs[0])).keys())

        for seq in tqdm(self.protein_seqs,unit=" sequences",position=0,desc="Ampiphillic Amino Acid Composition"):
            amp_psuedo=PseudoAAC.GetAPseudoAAC(seq)
            amp_pseudo_AAComp.append(list(amp_psuedo.values()))

        #convert calculated APsuedo_AAComp values into dataframe
        amp_pseudo_AAComp_df = pd.DataFrame(data=amp_pseudo_AAComp, columns=keys)

        self.amp_pseudo_AAC = amp_pseudo_AAComp_df

        return amp_pseudo_AAComp_df

    def get_descriptor_encoding(self,descriptor):

        """


        Returns
        -------
        desc_encoding : pd.DataFrame

        """
        #validate input descriptor is a valid available descriptor
        self.validDesc = self.valid_descriptors()
        descMatches = get_close_matches(descriptor,self.validDesc,cutoff=0.4)

        if descMatches!=[]:
            desc = descMatches[0]
        else:
            raise ValueError('Input descriptor ('+ desc + ') not in available descriptors /n '+self.valid_descriptors())

        print('desc',desc)

        if desc == 'aa_composition':
            if self.aa_composition.empty:
                self.get_aa_composition()
            desc_encoding = self.aa_composition

        elif desc == 'dipeptide_composition':
            if self.dipeptide_composition.empty:
                self.get_dipeptide_composition()
            desc_encoding = self.dipeptide_composition

        return desc_encoding

    def all_descriptors_list(self, desc_combo=1):

       """


       Returns
       -------
       desc_encoding : pd.DataFrame

       """
       all_descriptors = list(filter(lambda x: x.startswith('_'), list(self.__dict__.keys())))
       all_descriptors = list(filter(lambda x: not x.startswith('_all_desc'), all_descriptors))

       print('alldesc',all_descriptors)
       if desc_combo == 2:
           all_descriptors = list(itertools.combinations(all_descriptors, 2))
       elif desc_combo == 3:
           all_descriptors = list(itertools.combinations(all_descriptors, 3))
       else:
           pass     #if desc_combo input parameter not = 2 or 3 then use default all_descriptors

       return all_descriptors

    def get_all_descriptors(self):

        """


        Returns
        -------
        all_desc_df : pd.DataFrame

        """
        print('Calculating all Descriptor values:\n')

        # if not hasattr(self, 'aa_composition'):
        #     self.aa_composition = self.get_aa_composition()
        # if not hasattr(self, 'dipeptide_composition'):
        #     self.dipeptide_composition = self.get_dipeptide_composition()
        # if not hasattr(self, 'tripeptide_composition'):
        #     self.tripeptide_composition = self.get_tripeptide_composition()
        # if not hasattr(self, 'normalized_moreaubroto_autocorrelation') or \
        #     not hasattr(self, 'moran_autocorrelation') or \
        #     not hasattr(self, 'geary_autocorrelation'):
        #     self.normalized_moreaubroto_autocorrelation, self.moran_autocorrelation, \
        #     self.geary_autocorrelation = self.get_autocorrelation()
        # if not hasattr(self, 'CTD'):
        #     self.CTD = self.get_ctd()
        # if not hasattr(self, 'conjoint_triad'):
        #     self.conjoint_triad = self.get_conjoint_triad()
        # if not hasattr(self, 'seq_order_coupling_number'):
        #     self.seq_order_coupling_number = self.get_seq_order_coupling_number()
        # if not hasattr(self, 'quasi_seq_order'):
        #     self.quasi_seq_order = self.get_quasi_seq_order()
        # if not hasattr(self, 'pseudo_AAC'):
        #     self.pseudo_AAC = self.get_pseudo_AAC()
        # if not hasattr(self, 'amp_pseudo_AAC'):
        #     self.amp_pseudo_AAC = self.get_amp_pseudo_AAC()
        if (getattr(self, "aa_composition").empty):
                self.aa_composition = self.get_aa_composition()
        if (getattr(self, "dipeptide_composition").empty):
                self.dipeptide_composition = self.get_dipeptide_composition()

        if (getattr(self, "tripeptide_composition").empty):
                self.tripeptide_composition = self.get_tripeptide_composition()

        if (getattr(self, "normalized_moreaubroto_autocorrelation").empty) or \
            (getattr(self, "moran_autocorrelation").empty) or \
            (getattr(self, "geary_autocorrelation").empty):
            self.normalized_moreaubroto_autocorrelation, self.moran_autocorrelation, \
            self.geary_autocorrelation = self.get_autocorrelation()

        if (getattr(self, "CTD").empty):
                self.CTD = self.get_ctd()

        if (getattr(self, "conjoint_triad").empty):
                self.conjoint_triad = self.get_conjoint_triad()

        if (getattr(self, "seq_order_coupling_number").empty):
                self.seq_order_coupling_number = self.get_seq_order_coupling_number()

        if (getattr(self, "quasi_seq_order").empty):
                self.quasi_seq_order = self.get_quasi_seq_order()

        if (getattr(self, "pseudo_AAC").empty):
                self.pseudo_AAC = self.get_pseudo_AAC()

        if (getattr(self, "amp_pseudo_AAC").empty):
                self.amp_pseudo_AAC = self.get_amp_pseudo_AAC()

        # all_desc = [self.aa_composition, self.dipeptide_composition]
        all_desc = [self.aa_composition, self.dipeptide_composition, self.tripeptide_composition,
                           self.normalized_moreaubroto_autocorrelation, self.moran_autocorrelation,
                           self.geary_autocorrelation, self.composition. self.transition,
                           self.distribution, self.conjoint_triad, self.seq_order_coupling_number,
                           self.quasi_seq_order, self.pseudo_AAC, self.amp_pseudo_AAC]

        # all_desc = [self.aa_composition, self.dipeptide_composition, self.tripeptide_composition,
        #                    self.normalized_moreaubroto_autocorrelation, self.moran_autocorrelation,
        #                    self.geary_autocorrelation, self.CTD, self.conjoint_triad, self.seq_order_coupling_number]


        all_desc_df = pd.concat(all_desc, axis = 1)

        self.all_descriptors = all_desc_df

        return all_desc_df

    def valid_descriptors(self):

        """


        Returns
        -------
        all_desc_df : pd.DataFrame

        """
        # validDesc = ['aa_composition', 'dipeptide_composition', 'tripeptide_composition', \
        #     'norm_moreaubroto_autocorrelation','moran_autocorrelation','geary_autocorrelation', \
        #      'ctd', 'conjoint_triad','seq_order_coupling_number','quasi_seq_order_descriptors',\
        #      'pseudo_aa_comp', 'amphipilic_pseudo_aa_comp']
        validDesc = ['aa_composition', 'dipeptide_composition', 'tripeptide_composition', \
            'norm_moreaubroto_autocorrelation','moran_autocorrelation','geary_autocorrelation', \
             'ctd', 'composition', 'transition', 'distribution', 'conjoint_triad', \
             'seq_order_coupling_number','quasi_seq_order_descriptors',\
             'pseudo_aa_comp', 'amphipilic_pseudo_aa_comp']

        return validDesc

    def descriptor_groups(self):

        pass

    @property
    def all_desc(self):
        return self._all_desc

    @all_desc.setter
    def all_desc(self, val):
        self._all_desc = val

    @property
    def aa_composition(self):
        return self._aa_composition

    @aa_composition.setter
    def aa_composition(self, val):
        self._aa_composition = val

    @property
    def dipeptide_composition(self):
        return self._dipeptide_composition

    @dipeptide_composition.setter
    def dipeptide_composition(self, val):
        self._dipeptide_composition = val

    @property
    def tripeptide_composition(self):
        return self._tripeptide_composition

    @tripeptide_composition.setter
    def tripeptide_composition(self, val):
        self._tripeptide_composition = val

    @property
    def normalized_moreaubroto_autocorrelation(self):
        return self._normalized_moreaubroto_autocorrelation

    @normalized_moreaubroto_autocorrelation.setter
    def normalized_moreaubroto_autocorrelation(self, val):
        self._normalized_moreaubroto_autocorrelation = val

    @property
    def moran_autocorrelation(self):
        return self._moran_autocorrelation

    @moran_autocorrelation.setter
    def moran_autocorrelation(self, val):
        self._moran_autocorrelation = val

    @property
    def geary_autocorrelation(self):
        return self._geary_autocorrelation

    @geary_autocorrelation.setter
    def geary_autocorrelation(self, val):
        self._geary_autocorrelation = val

    @property
    def CTD(self):
        return self._CTD

    @CTD.setter
    def CTD(self, val):
        self._CTD = val

    @property
    def composition(self):
        return self._composition

    @composition.setter
    def composition(self, val):
        self._composition = val

    @property
    def transition(self):
        return self._transition

    @transition.setter
    def transition(self, val):
        self._transition = val

    @property
    def distribution(self):
        return self._distribution

    @distribution.setter
    def distribution(self, val):
        self._distribution = val

    @property
    def conjoint_triad(self):
        return self._conjoint_triad

    @conjoint_triad.setter
    def conjoint_triad(self, val):
        self._conjoint_triad = val

    @property
    def seq_order_coupling_number(self):
        return self._seq_order_coupling_number

    @seq_order_coupling_number.setter
    def seq_order_coupling_number(self, val):
        self._seq_order_coupling_number = val

    @property
    def quasi_seq_order(self):
        return self._quasi_seq_order

    @quasi_seq_order.setter
    def quasi_seq_order(self, val):
        self._quasi_seq_order = val

    @property
    def pseudo_AAC(self):
        return self._pseudo_AAC

    @pseudo_AAC.setter
    def pseudo_AAC(self, val):
        self._pseudo_AAC = val

    @property
    def amp_pseudo_AAC(self):
        return self._amp_pseudo_AAC

    @amp_pseudo_AAC.setter
    def amp_pseudo_AAC(self, val):
        self._amp_pseudo_AAC = val

    @property
    def all_descriptors(self):
        return self._all_descriptors

    @all_descriptors.setter
    def all_descriptors(self, val):
        self._all_descriptors = val

    def desc_to_class(self,str):

        return getattr(sys.modules[__name__], str)

    def __str__(self):
        pass

    def __repr__(self):
        return "Descriptor(Num Sequences: {}, Using All Descriptors: {})".format(
            self.num_seqs, self.all_desc
        )

    def __doc__(self):
        pass

    def __len__(self):
        pass

    def __shape__(self):
        pass
