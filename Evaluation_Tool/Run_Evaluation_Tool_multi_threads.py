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
import threading
import time
from tkinter import filedialog,Text

cwd = os.getcwd()
print(cwd)

kind=sys.argv[1]
ASR_kind=sys.argv[2]
start = time.perf_counter()



def preparation_for_run(noiseKind):
	print('create tmp dir and move punctuation tool:')
	subprocess.run(["$(pwd)/Evaluation_Tool/build_tmp_dirs "+noiseKind],stdout=subprocess.PIPE, shell=True)
	subprocess.run(["$(pwd)/Evaluation_Tool/move_and_change_name_punctutation "+noiseKind],stdout=subprocess.PIPE, shell=True)

    	
def Run_Speech_Recognition(noiseKind,chosen_ASR):
	print('Run Speech_Recognition_algorithm:')
	print(chosen_ASR)
	subprocess.run(["$(pwd)/Evaluation_Tool/run_speech_recognition $(pwd)/part_wav_files/ "+noiseKind+" "+chosen_ASR],stdout=subprocess.PIPE, shell=True)


def Run_clean_punctuation(noiseKind):
    print('Run clean punctuation function:')
    #print(cwd)
    nwd = cwd+"/tmp/"+noiseKind
    print(nwd)
    #os.chdir(nwd)
    subprocess.run([nwd+"/run_LibriSpeech_remove_punctuation.py "+noiseKind], stdout=subprocess.PIPE, shell=True)
    os.chdir(cwd)

def Run_Diff(noiseKind):
    print('Run Diff function:')
    subprocess.run(["./Evaluation_Tool/run_LibriSpeech_diff_part.py "+noiseKind], stdout=subprocess.PIPE, shell=True)
  
def Run_cost_function(noiseKind):
    print('Cost function:')
    subprocess.run(["./Evaluation_Tool/run_LibriSpeech_cost_function_part.py "+noiseKind], stdout=subprocess.PIPE, shell=True)


def Run_Evaluation(noiseKind,chosen_ASR):
	preparation_for_run(noiseKind)
	Run_Speech_Recognition(noiseKind,chosen_ASR)
	Run_clean_punctuation(noiseKind)
	Run_Diff(noiseKind)
	Run_cost_function(noiseKind)
	print("just if no app is running")

print(ASR_kind)
print(kind)
t1=threading.Thread(target=Run_Evaluation,args=(kind,ASR_kind))
t2=threading.Thread(target=Run_Evaluation,args=('white',ASR_kind))

t1.start()
time.sleep(0.005)
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()
print(f'Finish in {round(finish-start,2)} second(s)')
