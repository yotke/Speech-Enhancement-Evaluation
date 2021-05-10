#!/usr/bin/env python3

import os
import os.path
import subprocess
import signal
from os.path import dirname,abspath
import sys

kind=sys.argv[1];
pwd=os.getcwd()
nwd = dirname(dirname(dirname(abspath(__file__))))
print(nwd)
print(nwd)
os.chdir(nwd)

##babble
#####################################################################
# Run diff and after it run cost_function
subprocess.run(["./tmp/"+kind+"/Remove_punctuation $(pwd)/tmp/"+kind+"/clean_signal $(pwd)/"+kind+"/my_output/clean_signal "+kind],stdout=subprocess.PIPE, shell=True)
######################################################################
subprocess.run(["./tmp/"+kind+"/Remove_punctuation $(pwd)/tmp/"+kind+"/processed_noised_signal $(pwd)/"+kind+"/my_output/processed_noised_signal "+kind],stdout=subprocess.PIPE, shell=True)
######################################################################
subprocess.run(["./tmp/"+kind+"/Remove_punctuation $(pwd)/tmp/"+kind+"/noised_signal $(pwd)/"+kind+"/my_output/noised_signal "+kind],stdout=subprocess.PIPE, shell=True)

os.chdir(pwd)

