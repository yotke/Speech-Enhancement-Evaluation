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

##babble
#####################################################################
# Run diff and after it run cost_function
subprocess.run(["$(pwd)/tmp/babble/Remove_punctuation $(pwd)/tmp/babble/clean_signal $(pwd)/babble/my_output/clean_signal babble"],stdout=subprocess.PIPE, shell=True)
######################################################################
subprocess.run(["$(pwd)/tmp/babble/Remove_punctuation $(pwd)/tmp/babble/processed_noised_signal $(pwd)/babble/my_output/processed_noised_signal babble"],stdout=subprocess.PIPE, shell=True)
######################################################################
subprocess.run(["$(pwd)/tmp/babble/Remove_punctuation $(pwd)/tmp/babble/noised_signal $(pwd)/babble/my_output/noised_signal babble"],stdout=subprocess.PIPE, shell=True)

os.chdir(pwd)

