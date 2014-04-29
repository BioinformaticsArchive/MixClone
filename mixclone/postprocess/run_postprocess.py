'''
Created on 2012-08-18

@author: Yi Li

pyloh.postprocess.plot

================================================================================

Modified on 2014-04-11

@author: Yi Li

'''
import os
import sys
import pickle as pkl

import numpy as np
import scipy as sp
from matplotlib import pyplot as plt

from mixclone import constants
from mixclone.preprocess.data import Data

def run_postprocess(args):
    if args.input == True:
        file_name = args.output_filename_base + '.MixClone.input.pkl'
    else:
        file_name = args.output_filename_base + '.MixClone.output.pkl'
    
    infile = open(file_name, 'rb')
    data = pkl.load(infile)
    infile.close()
    
    extract_paired_counts(data, args.output_filename_base)
    
    extract_segments(data, args.output_filename_base)
    
        
def extract_paired_counts(data, output_filename_base):
    counts_file_name = output_filename_base + '.MixClone.counts'
    outfile = open(counts_file_name, 'w')
    segments = data.segments
    
    outfile.write('\t'.join(['#seg_name', 'normal_A', 'normal_B', 'tumor_A',
                             'tumor_B', 'chrom', 'pos']) + '\n')
    
    for j in range(0, data.seg_num):
        for i in range(0, segments[j].paired_counts.shape[0]):
            outfile.write(segments[j].name + '\t'
                          + '\t'.join(map(str, segments[j].paired_counts[i])) + '\n')

    outfile.close()
    
    
def extract_segments(data, output_filename_base):
    segments_file_name = output_filename_base + '.MixClone.segments'
    outfile = open(segments_file_name, 'w')
    segments = data.segments
    
    outfile.write('\t'.join(['#seg_name', 'chrom', 'start', 'end', 'normal_reads_num',
                             'tumor_reads_num', 'LOH_frac', 'LOH_status', 'log2_ratio',
                             'copy_number', 'allele_type', 'subclone_prev', 'subclone_cluster']) + '\n')
    
    for j in range(0, data.seg_num):
        outfile.write('\t'.join(map(str, [segments[j].name, segments[j].chrom_name,segments[j].start,
                                segments[j].end, segments[j].normal_reads_num, segments[j].tumor_reads_num,
                                segments[j].LOH_frac, segments[j].LOH_status, segments[j].log2_ratio,
                                segments[j].copy_number, segments[j].allele_type,
                                "{0:.3f}".format(segments[j].subclone_prev), segments[j].subclone_cluster])) + '\n')

    outfile.close()
    
    