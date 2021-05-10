#!/usr/bin/env python3

import os
import os.path
import subprocess
import signal
import time
import threading
import sys
#current_dir=$(pwd)

# Run DTLN on noised LibriSpeech dataset witch include more then 100000 hours of audio
kind=sys.argv[1]
cwd = os.getcwd()


def Run_DTLN_Func(noise_kind):
   input1 = cwd+"/noised/"+noise_kind+"_noise "
   input2 = cwd+"/"+noise_kind+"/my_output "
   print(input1)
   print(cwd+"/runDTLN "+input1 +input2 +noise_kind +cwd)
   subprocess.run([cwd+"/runDTLN "+input1 +input2 +noise_kind +" "+cwd],stdout=subprocess.PIPE, shell=True)


#subprocess.run(["/home/yotam/softwares/project/LibriTTS/runDTLN /home/yotam/softwares/project/matlab/noised/white_noise /home/yotam/softwares/project/LibriTTS/white/my_output white"],stdout=subprocess.PIPE, shell=True)
def main_f():
    os.chdir('/home/yotam/PycharmProjects/DTLN-master')

    t1 = threading.Thread(target=Run_DTLN_Func, args=(kind,))
    t2 = threading.Thread(target=Run_DTLN_Func, args=("white",))

    t1.start()
    time.sleep(0.005)
    t2.start()

    t1.join()
    t2.join()
    #Run_DTLN_Func("babble")
    #Run_DTLN_Func("white")


main_f()
