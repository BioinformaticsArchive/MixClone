'''
Abstract classes which all models for classifying paired data should sub-class. 

Created on 2011-03-31

@author: Andrew Roth

JointSNVMix-0.6.2
joint_snv_mix.classification.base.EMModelTrainer
joint_snv_mix.classification.base.PriorParser

================================================================================

Modified on 2013-07-29

@author: Yi Li

pyloh.model.model_base

================================================================================

Modified on 2014-04-15

@author: Yi Li
'''
import sys
import pickle as pkl

from ConfigParser import ConfigParser

import numpy as np

from mixclone import constants
from mixclone.preprocess.data import Data

class ProbabilisticModel(object):
    def __init__(self, max_copynumber, baseline_thred):
        self.max_copynumber = max_copynumber
        self.baseline_thred = baseline_thred
        self.priors_parser = PriorParser()
        self._init_components()
        
    def read_priors(self, priors_filename):
        raise NotImplemented
    
    def read_data(self, filename_base):
        data_file_name = filename_base + '.MixClone.data.pkl'
        infile = open(data_file_name, 'rb')
        self.data = pkl.load(infile)
        
        infile.close()
        
    def preprocess(self):
        raise NotImplemented
        
    def run(self, max_iters, stop_value):
        trainer = self.model_trainer_class(self.priors, self.data, self.max_copynumber,
                                    self.baseline_thred, max_iters, stop_value)
        
        trainer.train()
        
        self.data = trainer.data
        
        #self.model_parameters = trainer.model_parameters
        
        #self.log_likelihood = trainer.log_likelihood
        
    def write_results(self, filename_base):
        results_file_name = self.filename_base + '.MixClone.results.pkl'
        outfile = open(results_file_name, 'wb')
        pkl.dump(self.data, outfile, protocol=2)
        
        outfile.close()

    def _init_components(self):
        raise NotImplemented


#JointSNVMix
class ModelTrainer(object):
    def __init__(self, priors, data, max_copynumber, baseline_thred, max_iters, stop_value):
        self.priors = priors
        
        self.data = data
        
        self.max_copynumber = max_copynumber
        
        self.baseline_thred = baseline_thred
        
        self.max_iters = max_iters
        
        self.stop_value = stop_value
        
        self.iters = 0
            
        self._init_components()
        
    def train(self):
        raise NotImplemented
    

class ConfigParameters(object):
    def __init__(self, max_copynumber, baseline_thred):
        self.max_copynumber = priors
        self.baseline_thred = data
        
        self._init_components()
        

class ModelParameters(object):
    def __init__(self, priors, data, config_parameters):
        self.priors = priors
        self.data = data
        self.config_parameters = config_parameters
        
        self._init_parameters()
    
    def update(self, sufficient_statistics):
        raise NotImplemented

    def _init_parameters(self):
        raise NotImplemented
    
    
class LatentVariables(object): 
    def __init__(self, data, config_parameters):       
        self.data = data
        self.config_parameters = config_parameters

    def update(self, parameters):
        raise NotImplemented


class ModelLikelihood(object):
    def __init__(self, data, config_parameters):
        self.data = data
        self.config_parameters = config_parameters
        
    def get_log_likelihood(self, parameters, priors):
        raise NotImplemented




