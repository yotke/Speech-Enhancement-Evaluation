#!/usr/bin/env python3

import os
import os.path
import subprocess
import signal
from os.path import dirname,abspath

pwd=os.getcwd()
nwd = dirname(dirname(dirname(abspath(__file__))))
#print(nwd)
os.chdir(nwd)

##white
#####################################################################
# Run diff and after it run cost_function
subprocess.Popen(["$(pwd)/tmp/white/Remove_punctuation $(pwd)/tmp/white/clean_signal $(pwd)/white/my_output/clean_signal white"],stdout=subprocess.PIPE, shell=True)
os.wait()
######################################################################
subprocess.Popen(["$(pwd)/tmp/white/Remove_punctuation $(pwd)/tmp/white/processed_noised_signal $(pwd)/white/my_output/processed_noised_signal white"],stdout=subprocess.PIPE, shell=True)
os.wait()
######################################################################
subprocess.Popen(["$(pwd)/tmp/white/Remove_punctuation $(pwd)/tmp/white/noised_signal $(pwd)/white/my_output/noised_signal white"],stdout=subprocess.PIPE, shell=True)
os.wait()
os.chdir(pwd)

