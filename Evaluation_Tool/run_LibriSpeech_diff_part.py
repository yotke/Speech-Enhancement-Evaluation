#!/usr/bin/env python3

import os
import os.path
import subprocess
import signal
import sys

kind = sys.argv[1]

#####################################################################
# Run diff and after it run cost_function
subprocess.run(["$(pwd)/Evaluation_Tool/run_diff $(pwd)/"+kind+"/my_output/processed_noised_signal $(pwd)/part_clean_original_txt_file processed_noised_signal "+kind],stdout=subprocess.PIPE, shell=True)
######################################################################
subprocess.run(["$(pwd)/Evaluation_Tool/run_diff $(pwd)/"+kind+"/my_output/clean_signal $(pwd)/part_clean_original_txt_file clean_signal "+kind],stdout=subprocess.PIPE, shell=True)
######################################################################
subprocess.run(["$(pwd)/Evaluation_Tool/run_diff $(pwd)/"+kind+"/my_output/noised_signal $(pwd)/part_clean_original_txt_file noised_signal "+kind],stdout=subprocess.PIPE, shell=True)




