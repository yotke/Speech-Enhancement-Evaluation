#!/usr/bin/env python3

import os
import os.path
import subprocess
import signal


#####################################################################
# Run diff and after it run cost_function
subprocess.run(["$(pwd)/Evaluation_Tool/run_diff $(pwd)/babble/my_output/processed_noised_signal $(pwd)/part_clean_original_txt_file processed_noised_signal babble"],stdout=subprocess.PIPE, shell=True)
######################################################################
subprocess.run(["$(pwd)/Evaluation_Tool/run_diff $(pwd)/babble/my_output/clean_signal $(pwd)/part_clean_original_txt_file clean_signal babble"],stdout=subprocess.PIPE, shell=True)
######################################################################
subprocess.run(["$(pwd)/Evaluation_Tool/run_diff $(pwd)/babble/my_output/noised_signal $(pwd)/part_clean_original_txt_file noised_signal babble"],stdout=subprocess.PIPE, shell=True)



##white

#####################################################################
# Run diff and after it run cost_function
subprocess.run(["$(pwd)/Evaluation_Tool/run_diff $(pwd)/white/my_output/processed_noised_signal $(pwd)/part_clean_original_txt_file processed_noised_signal white"],stdout=subprocess.PIPE, shell=True)
######################################################################
subprocess.run(["$(pwd)/Evaluation_Tool/run_diff $(pwd)/white/my_output/clean_signal $(pwd)/part_clean_original_txt_file clean_signal white"],stdout=subprocess.PIPE, shell=True)
######################################################################
subprocess.run(["$(pwd)/Evaluation_Tool/run_diff $(pwd)/white/my_output/noised_signal $(pwd)/part_clean_original_txt_file noised_signal white"],stdout=subprocess.PIPE, shell=True)



