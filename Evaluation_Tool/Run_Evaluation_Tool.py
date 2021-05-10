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

noiseKind=sys.argv[1]

def preparation_for_run():
	print('create tmp dir and move punctuation tool:')
	subprocess.run(["$(pwd)/Evaluation_Tool/build_tmp_dirs "+noiseKind],stdout=subprocess.PIPE, shell=True)
	subprocess.run(["$(pwd)/Evaluation_Tool/build_tmp_dirs white"],stdout=subprocess.PIPE, shell=True)
	subprocess.run(["$(pwd)/Evaluation_Tool/move_and_change_name_punctutation "+noiseKind],stdout=subprocess.PIPE, shell=True)
	subprocess.run(["$(pwd)/Evaluation_Tool/move_and_change_name_punctutation white"],stdout=subprocess.PIPE, shell=True)
    	
def Run_Speech_Recognition():
	print('Run Speech_Recognition_algorithm:')
	subprocess.run(["$(pwd)/Evaluation_Tool/run_speech_recognition $(pwd)/part_wav_files/ "+noiseKind],stdout=subprocess.PIPE, shell=True)
	subprocess.run(["$(pwd)/Evaluation_Tool/run_speech_recognition $(pwd)/part_wav_files/ white"],stdout=subprocess.PIPE, shell=True)



def Run_clean_punctuation():
    print('Run clean punctuation function:')
    #print(cwd)
    nwd = cwd+"/tmp/"+noiseKind
    print(nwd)
    #os.chdir(nwd)
    subprocess.run([nwd+"/run_LibriSpeech_remove_punctuation.py babble"], stdout=subprocess.PIPE, shell=True)
    nwd = cwd +"/tmp/white"
    #os.chdir(nwd)
    subprocess.run([nwd+"/run_LibriSpeech_remove_punctuation.py white"], stdout=subprocess.PIPE, shell=True)	
    os.chdir(cwd)

def Run_Diff():
    print('Run Diff function:')
    subprocess.run(["./Evaluation_Tool/run_LibriSpeech_diff_part.py "+noiseKind], stdout=subprocess.PIPE, shell=True)
    subprocess.run(["./Evaluation_Tool/run_LibriSpeech_diff_part.py white"], stdout=subprocess.PIPE, shell=True)
  
def Run_cost_function():
    print('Cost function:')
    subprocess.run(["./Evaluation_Tool/run_LibriSpeech_cost_function_part.py "+noiseKind], stdout=subprocess.PIPE, shell=True)
    subprocess.run(["./Evaluation_Tool/run_LibriSpeech_cost_function_part.py white"], stdout=subprocess.PIPE, shell=True)



preparation_for_run()


Run_Speech_Recognition()

sys.stdout.flush()

Run_clean_punctuation()


Run_Diff()


Run_cost_function()
