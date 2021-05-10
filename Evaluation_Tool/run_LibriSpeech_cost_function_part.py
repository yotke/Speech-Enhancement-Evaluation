#!/usr/bin/env python3

import os
import os.path
import subprocess
import signal
import sys
from io import StringIO  ## for Python 3
import io
from contextlib import redirect_stdout
noise_kind = sys.argv[1]
## babble
if os.path.exists(noise_kind+"/TotCost.txt")==True:
	os.remove(noise_kind+"/TotCost.txt")
f=open(noise_kind+"/TotCost.txt", 'a')
f.write('New output of our cost function:\n')
path_to_dir= "/home/yotam/softwares/project/LibriTTS"
kind=sys.argv[1]
# Run cost_function with DTLN
f.write("Signals processed by SE algorithm:\n")
p_processed=subprocess.run(["$(pwd)/Evaluation_Tool/cost_function_part processed_noised_signal "+noise_kind],capture_output=True, shell=True)
f.write(p_processed.stdout.decode())

# Run cost_function without DTLN
f.write("Clean signals precessed:\n")
p_clean=subprocess.run(["$(pwd)/Evaluation_Tool/cost_function_part clean_signal "+noise_kind],capture_output=True, shell=True)
f.write(p_clean.stdout.decode())
# Run cost_function on noised without DTLN
f.write("Noised signals without SE processing:\n")
p_Noisy=subprocess.run(["$(pwd)/Evaluation_Tool/cost_function_part noised_signal "+noise_kind],capture_output=True, shell=True)
f.write(p_Noisy.stdout.decode())

f.close()


