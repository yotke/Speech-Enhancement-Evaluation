#!/usr/bin/env python3

import os
import os.path
import subprocess
import signal
import time
import threading

#current_dir=$(pwd)

# Run DTLN on noised LibriSpeech dataset witch include more then 100000 hours of audio




def Run_DTLN_Func(noise_kind):
   input1 = "/home/yotam/softwares/project/matlab/noised/"+noise_kind+"_noise "
   input2 = "/home/yotam/softwares/project/LibriTTS/"+noise_kind+"/my_output "
   print(input1)
   subprocess.run(["/home/yotam/softwares/project/LibriTTS/runDTLN "+input1 +input2 +noise_kind],stdout=subprocess.PIPE, shell=True)


#subprocess.run(["/home/yotam/softwares/project/LibriTTS/runDTLN /home/yotam/softwares/project/matlab/noised/white_noise /home/yotam/softwares/project/LibriTTS/white/my_output white"],stdout=subprocess.PIPE, shell=True)
def main_f():
    os.chdir('/home/yotam/PycharmProjects/DTLN-master')

    t1 = threading.Thread(target=Run_DTLN_Func, args=("babble",))
    t2 = threading.Thread(target=Run_DTLN_Func, args=("white",))

    t1.start()
    time.sleep(0.005)
    t2.start()

    t1.join()
    t2.join()
    #Run_DTLN_Func("babble")
    #Run_DTLN_Func("white")


main_f()
