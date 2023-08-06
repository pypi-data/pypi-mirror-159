#Authors: Caitlin Rose, Vinaya Valsan, etc

import sys,os,json,ast,random,glob,h5py
import subprocess,time
import numpy as np
import lal
import rapid_pe.lalsimutils
from argparse import ArgumentParser
from ligo.gracedb.rest import GraceDb
from sklearn.neighbors import BallTree
from rapidpe_rift_pipe.modules import *
from glue import pipeline
from ligo import segments
from ligo.lw import ligolw
from ligo.lw import lsctables
from ligo.lw import utils as ligolw_utils
from rapidpe_rift_pipe.config import Config

@lsctables.use_in
class LIGOLWContentHandler(ligolw.LIGOLWContentHandler):
    pass

cfgname = sys.argv[1]
config = Config.load(cfgname)
output_dir = script_directory+"/"+config.output_parent_directory+"/"+output_event_directory+"/"

def main():

    event_info["wrapper_script_start_time"] = time.time()
 
    #read in the gstlal snr time series data

    if float(params["mass1"])+float(params["mass2"]) > 10.0:
        event_info["approximant"] = "SEOBNRv4_ROM" #v4 vs v4_ROM
    else:
        event_info["approximant"] = "TaylorT2"
        #event_info["approximant"] = "TaylorF2" #highest speed. 
        if "spin1z" in intrinsic_param_to_search:
        #If this is a spinning search, use SpinTaylorT4 instead
            event_info["approximant"] = "SpinTaylorT4"

    newlines = "universe = vanilla\n"
    newlines += "executable = "+config.exe_integration_extrinsic_likelihood+"\n"
    newlines += 'arguments = " '
    newlines += " --output-file="+integration_output_file_name
    newlines += " --mass1 "+str(inj_param["mass1"])+" --mass2 "+str(inj_param["mass2"])+" --spin1z "+str(inj_param["spin1z"])+" --spin2z "+str(inj_param["spin2z"])
    newlines += " "+extra_cmd_line
    newlines += ' "\n'
    newlines += "request_memory = 4096\naccounting_group = "+config.accounting_group+"\ngetenv = True\n"
    newlines += "log = logs/integrate.log\nerror = logs/integrate.err\noutput = logs/integrate.out\n"
    newlines += "notification = never\nqueue 1\n"

    #submit ILE subdag for each template
