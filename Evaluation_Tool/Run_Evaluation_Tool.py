#!/usr/bin/env python3

import os
import os.path
import subprocess
import signal
import time
import threading
import speech_recognition as sr
import simpleaudio as sa
from os import path
import sys
import tkinter as tk
from tkinter import filedialog,Text

cwd = os.getcwd()
print(cwd)

def preparation_for_run():
	os.system('echo create tmp dir and move punctuation tool:')
	subprocess.run(["$(pwd)/Evaluation_Tool/build_tmp_dirs"],stdout=subprocess.PIPE, shell=True)
	subprocess.run(["$(pwd)/Evaluation_Tool/move_and_change_name_punctutation"],stdout=subprocess.PIPE, shell=True)

    	
def Run_Speech_Recognition():
	os.system('echo Run Speech_Recognition_algorithm:')
	subprocess.run(["$(pwd)/Evaluation_Tool/run_speech_recognition $(pwd)/part_wav_files/"],stdout=subprocess.PIPE, shell=True)


def Run_clean_punctuation():
    os.system('echo Run clean punctuation function:')
    nwd = cwd+"/tmp/babble"
    #os.chdir(nwd)
    exec(open("./tmp/babble/run_LibriSpeech_remove_punctuation.py").read())
    #nwd = cwd +"/tmp/white"
    #os.chdir(nwd)
    exec(open("./tmp/white/run_LibriSpeech_remove_punctuation.py").read())	
    os.chdir(cwd)


def Run_Diff():
    os.system('echo Run Diff function:')
    exec(open("./Evaluation_Tool/run_LibriSpeech_diff_part.py").read())
  
  
def Run_cost_function():
    os.system('echo Cost function:')
    exec(open("./Evaluation_Tool/run_LibriSpeech_cost_function_part.py").read())




preparation_for_run()


Run_Speech_Recognition()

#sys.stdout.flush()

Run_clean_punctuation()


Run_Diff()


Run_cost_function()