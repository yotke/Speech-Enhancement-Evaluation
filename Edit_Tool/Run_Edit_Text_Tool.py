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

def Move_all_txt_files():
	os.system("echo Move all text files to one directory:")
	subprocess.run(["$(pwd)/Edit_Tool/move_txt_files -o $(pwd)/test-clean"],stdout=subprocess.PIPE, shell=True)


def clean_all_txt_files():
	os.system("echo Clean all text files from punctuations:")
	subprocess.run(["$(pwd)/Edit_Tool/Remove_punctuation $(pwd)/original_txt_files"],stdout=subprocess.PIPE, shell=True)
	


Move_all_txt_files()


clean_all_txt_files()



