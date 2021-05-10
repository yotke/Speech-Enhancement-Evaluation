import numpy as np
import time
import threading
import subprocess
import speech_recognition as sr
import simpleaudio as sa
from os import path
import sys
import os
# time start





def main_speech_recognition():
    #input name of wav file
    input=sys.argv[1];
    #input kind of noise.
    kind=sys.argv[2];
    #input ASR kind of noise.
    ASR_kind=sys.argv[3];
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()
    start = time.perf_counter()

    #babble_noised
    file_name = input+".wav"
    pwd=os.getcwd()
    clean_AUDIO_FILE = path.join(path.dirname(pwd+'/all_wav_files/'), file_name)
    noisy_AUDIO_FILE = path.join(path.dirname(pwd+'/noised/'+kind+'_noise/'), file_name)
    DTLN_processed_AUDIO_FILE = path.join(path.dirname(pwd+'/'+kind+'/my_output/'), file_name)

    clean_output_file = path.join(path.dirname(pwd+'/tmp/'+kind+'/clean_signal/'), input)
    noisy_output_file = path.join(path.dirname(pwd+'/tmp/'+kind+'/noised_signal/'), input)
    DTLN_processed_output_file = path.join(path.dirname(pwd+'/tmp/'+kind+'/processed_noised_signal/'), input)

    #sound_wav_file(noisy_AUDIO_FILE)
    #sound_wav_file(DTLN_processed_AUDIO_FILE)

    #create_text_file_from_wav(r,clean_AUDIO_FILE,clean_output_file)
    #create_text_file_from_wav(r,noisy_AUDIO_FILE,noisy_output_file)
    #create_text_file_from_wav(r,DTLN_processed_AUDIO_FILE,DTLN_processed_output_file)

    #threads run for more fast opration.
    if ASR_kind == "sphinx" or ASR_kind == "Sphinx":
        t1=threading.Thread(target=create_text_file_from_wav,args=(r,clean_AUDIO_FILE,clean_output_file,'Clean'))
        t2=threading.Thread(target=create_text_file_from_wav,args=(r,noisy_AUDIO_FILE,noisy_output_file,'Noisy'))
        t3=threading.Thread(target=create_text_file_from_wav,args=(r,DTLN_processed_AUDIO_FILE,DTLN_processed_output_file,'Processed'))
    if ASR_kind == "baidu" or ASR_kind == "Baidu":
        t1=threading.Thread(target=Baidu_Algorithm,args=(r,clean_AUDIO_FILE,clean_output_file,'Clean'))
        t2=threading.Thread(target=Baidu_Algorithm,args=(r,noisy_AUDIO_FILE,noisy_output_file,'Noisy'))
        t3=threading.Thread(target=Baidu_Algorithm,args=(r,DTLN_processed_AUDIO_FILE,DTLN_processed_output_file,'Processed'))


    t1.start()
    time.sleep(0.005)
    t2.start()
    time.sleep(0.005)
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    finish = time.perf_counter()
    print(f'Finish in {round(finish-start,2)} second(s)')



def create_text_file_from_wav(r,AUDIO_FILE,output_file,type_):
    # Reading Audio file as source
    # listening the audio file and store in audio_text variable

    audio_text = subscription_create_from_signal(r,AUDIO_FILE)
    #time.sleep(1)
    try:
        # using recognize sphinx recognition
        text = recognize(r,audio_text,type_)
    except:
        print('Sorry.. run again...')
    whrite_file(output_file, text)


def sound_wav_file(AUDIO_FILE):
    # For hearing the wav file from python we use this code
    wave_obj = sa.WaveObject.from_wave_file(AUDIO_FILE)
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait until sound has finished playing


def subscription_create_from_signal(r,AUDIO_FILE):
    with sr.WavFile(AUDIO_FILE) as source:
        r.adjust_for_ambient_noise(source, duration=0.1)
        audio_text = r.record(source)
    return audio_text


def recognize(r,audio_text,type_):
    Text = r.recognize_sphinx(audio_text)
    print(type_+' file output:')
    print(Text)
    return Text


def whrite_file(output_file,__text__):
    text_file = open(output_file+".txt","w")
    text_file.write(__text__)
    text_file.close() #to change file access modes


def Baidu_Algorithm(r,AUDIO_FILE,output_file,type_):

    pwd = os.getcwd();
    subprocess.run([pwd+"/Baidu "+AUDIO_FILE+" "+output_file],stdout=subprocess.PIPE, shell=True)

#deepspeech --model deepspeech-0.9.1-models.pbmm --scorer deepspeech-0.9.1-models.scorer 		--audio $Var >>$path/Text/$full_Name


main_speech_recognition()
