#!/usr/bin/env python3

import os
import os.path
import subprocess
import signal


## babble
os.system('echo "New output of our cost function:" >> $(pwd)/babble/TotCost.txt') 

path_to_dir= "/home/yotam/softwares/project/LibriTTS"

#####################################################################
# Run cost_function with DTLN
os.system('echo Signals processed by SE algorithm: >> $(pwd)/babble/TotCost.txt') 
subprocess.run(["$(pwd)/Evaluation_Tool/cost_function_part processed_noised_signal babble>> $(pwd)/babble/TotCost.txt"],stdout=subprocess.PIPE, shell=True)

#######################################################################
# Run cost_function without DTLN
os.system('echo Clean signals precessed: >> $(pwd)/babble/TotCost.txt ') 
subprocess.run(["$(pwd)/Evaluation_Tool/cost_function_part clean_signal babble >> $(pwd)/babble/TotCost.txt"],stdout=subprocess.PIPE, shell=True)

#######################################################################
# Run cost_function on noised without DTLN
os.system('echo Noised signals without SE processing: >> $(pwd)/babble/TotCost.txt ') 
subprocess.run(["$(pwd)/Evaluation_Tool/cost_function_part noised_signal babble >> $(pwd)/babble/TotCost.txt"],stdout=subprocess.PIPE, shell=True)



## White

os.system('echo "New output of our cost function:" >> $(pwd)/white/TotCost.txt') 
#####################################################################
# Run cost_function with DTLN
os.system('echo Signals processed by SE algorithm: >> $(pwd)/white/TotCost.txt') 
subprocess.run(["$(pwd)/Evaluation_Tool/cost_function_part processed_noised_signal white >> $(pwd)/white/TotCost.txt"],stdout=subprocess.PIPE, shell=True)

#######################################################################
# Run cost_function without DTLN
os.system('echo Clean signals precessed: >> $(pwd)/white/TotCost.txt ') 
subprocess.run(["$(pwd)/Evaluation_Tool/cost_function_part clean_signal white >> $(pwd)/white/TotCost.txt"],stdout=subprocess.PIPE, shell=True)

#######################################################################
# Run cost_function on noised without DTLN
os.system('echo Noised signals without SE processing: >> $(pwd)/white/TotCost.txt ') 
subprocess.run(["$(pwd)/Evaluation_Tool/cost_function_part noised_signal white >> $(pwd)/white/TotCost.txt"],stdout=subprocess.PIPE, shell=True)

