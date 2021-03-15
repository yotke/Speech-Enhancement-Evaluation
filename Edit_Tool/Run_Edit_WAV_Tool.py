#!/usr/bin/env python3

import os
#import os.path
import subprocess
import signal
import time
import threading
from os import path
import sys

cwd = os.getcwd()
print(cwd)
if(len(sys.argv)>1):
	print(len(sys.argv))
	input=sys.argv[1];
else:
	input=''
def convert_flac_to_wav_files():
	os.system("echo Convert flac files to wav files:")
	subprocess.run(["$(pwd)/Edit_Tool/convert_flac_to_wav_file $(pwd)/test-clean"],stdout=subprocess.PIPE, shell=True)

def Move_all_wav_files():
	os.system("echo Move all wav files to one directory:")
	subprocess.run(["$(pwd)/Edit_Tool/move_all_wav_files $(pwd)/test-clean"],stdout=subprocess.PIPE, shell=True)



if(input == "flac"):
	convert_flac_to_wav_files()
	
Move_all_wav_files()





