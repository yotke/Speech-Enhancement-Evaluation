#!/usr/bin/env python3
import tkinter as tk
from tkinter import *
from tkinter import filedialog,Text
from tkinter.ttk import *
import subprocess
import numpy
from decimal import Decimal
import numpy as np
import time
import threading
import speech_recognition as sr
import simpleaudio as sa
import os
from os import path
from os.path import dirname, abspath
import sys
import simpleaudio as sa


root = tk.Tk()
root.title("Evaluation Tool")

L1 = tk.Label(root,text="Options",bd=2,relief="sunken",font=("Helvetica",30))
L1.pack(side="bottom")
apps = []
pwd = os.getcwd()
input_dir=""

def sound_wav_file(AUDIO_FILE):
    # For hearing the wav file from python we use this code
    wave_obj = sa.WaveObject.from_wave_file(AUDIO_FILE)
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait until sound has finished playing


def readLineAndWrite(kind):
    global noise_Error_percent
    global clean_Error_percent
    global processed_Error_percent
    buffer = " "
    string=" "
    perArr = numpy.array([0, 0, 0])
    try:
        file = open(os.getcwd() + "/" + kind + "/TotCost.txt", "r")
        try:
            # Read the entire POST log file into a buffer
            buffer += file.read()
        finally:
            file.close()
    except IOError:
        buffer += "The POST file could not be opened."
        return string
    string = buffer.split("\n")
    print(buffer)
    print(string)

    noise_Error_percent = Decimal(string[9])*100
    clean_Error_percent = Decimal(string[6])*100
    processed_Error_percent = Decimal(string[3])*100

    return [str(Decimal(string[3])*100)+"%"+"     ",str(Decimal(string[6])*100)+"%"+"     ",str(Decimal(string[9])*100)+"%"+"     "]


def myClick_Result():
    global input_result
    input_result = e_result.get()
    t_res = tk.Text(root,width=30,height=10,bd=10)
    string =" "
    string=input_result.split(sep=" ",maxsplit=3)
    t_res.insert(INSERT,"Name:"+string[0]+"\n\n")
    t_res.insert(INSERT, "Type:" + string[1]+"\n\n")
    t_res.insert(INSERT, "Kind:" + string[2] + "\n\n")
    t_res.place(x=250, y=630)
    return input_result

def myClick_Main_Directory():
    global input_dir
    input_dir = e_dir.get()
    input_dir = filedialog.askdirectory()
    e_dir.insert(INSERT,input_dir)
    #t_dir.insert()
    print(input_dir)
    return input_dir

def myClick_Data_Size():
    global Random_data_choise
    global input_Data
    Data_choise = e_Data.get()
    string=Data_choise.split(sep=" ",maxsplit=3)
    input_Data=string[0]
    if (len(string)>1):
        Random_data_choise=string[1]
        print (Random_data_choise)
    else:
        Random_data_choise=""
    return input_Data

def myClick_ASR_Choose():
    global input_ASR
    input_ASR = e_ASR.get()
    print(input_ASR)
    return input_ASR

def myClick_Clean_Sound():
    string=input_result.split(sep=" ",maxsplit=3)
    clean_AUDIO_FILE = path.join(path.dirname(pwd+'/all_wav_files/'), string[0]+".wav")
    sound_wav_file(clean_AUDIO_FILE)


def myClick_Noised_Sound():
    string=input_result.split(sep=" ",maxsplit=3)
    noisy_AUDIO_FILE = path.join(path.dirname(pwd + '/noised/' + chosen_input_Noise + '_noise/'), string[0]+".wav")
    sound_wav_file(noisy_AUDIO_FILE)

def myClick_Processed_Sound():
    string=input_result.split(sep=" ",maxsplit=3)
    DTLN_processed_AUDIO_FILE = path.join(path.dirname(pwd + '/' + chosen_input_Noise + '/my_output/'), string[0]+".wav")
    sound_wav_file(DTLN_processed_AUDIO_FILE)


def text():
    canvas.create_text(100,10,fill="darkblue",font="Times 20 italic bold",text="Click the bubbles that are multiples of two.")
    canvas.update


def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
    filename= filedialog.askopenfilename(initialdir="$pwd",title="Select File",
                                         filetypes=(("python","*.py"),("all files","*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame,text=app,bg="gray")
        label.pack()


def choosenNoise():
    global chosen_input_Noise
    chosen_input_Noise = e_Noise.get()

def choosenNoisePower():
    global chosen_input_Noise_power
    chosen_input_Noise_power = e_Noise_power.get()

def runApps():
    for app in apps:
        subprocess.run([app], stdout=subprocess.PIPE,shell=True)

def open_to_check():
    subprocess.run(["./$pwd/Open_test_to_check.sh "+ input_result], stdout=subprocess.PIPE, shell=True)


def runPartFilesCreate():
    #if os.path.exists("part_wav_files/*.") == True:
     #   os.remove("part_wav_files/*.wav")
    subprocess.run(["./$pwd/Edit_Tool/move_part_wav_files all_wav_files "+input_Data+" "+Random_data_choise], stdout=subprocess.PIPE, shell=True)
    subprocess.run(["./$pwd/Edit_Tool/move_part_Text_files part_wav_files "+input_Data], stdout=subprocess.PIPE, shell=True)

def create_part_data_from_Noise_dataset():
    Noised_dir = filedialog.askdirectory()
    #n_kind="babble"
    subprocess.run(["./$pwd/Edit_Tool/create_part_data_from_Noise_dataset "+Noised_dir+" "+input_Data+" "+chosen_input_Noise], stdout=subprocess.PIPE, shell=True)


def runEditTool():
    subprocess.run(["./$pwd/Run_Edit_Tool.py"], stdout=subprocess.PIPE, shell=True)

def runEditWavTool():
    subprocess.run(["./$pwd/Edit_Tool/Run_Edit_WAV_Tool.py "+"\""+input_dir+"\""], stdout=subprocess.PIPE, shell=True)

#def OpenResult():
#    subprocess.run(["./$pwd/Edit_Tool/Run_Edit_Text_Tool.py"], stdout=subprocess.PIPE, shell=True)

def runEditTextTool():
    subprocess.run(["./$pwd/Edit_Tool/Run_Edit_Text_Tool.py "+"\""+input_dir+"\""], stdout=subprocess.PIPE, shell=True)


def score_calculator():
    noise_succ_percent = 100 - noise_Error_percent
    print(noise_succ_percent)
    clean_succ_percent = 100 - clean_Error_percent
    print(clean_succ_percent)
    processed_succ_percent = 100 - processed_Error_percent
    print(processed_succ_percent)
    Score_Enhancement = (processed_succ_percent/clean_succ_percent - noise_succ_percent/clean_succ_percent)*100
    percent_success_Enhancement = ((processed_succ_percent - noise_succ_percent)/noise_succ_percent)*100
    success_Enhancement_normalized = Score_Enhancement #/ clean_succ_percent))
    return success_Enhancement_normalized


def MOS_Claculator(Noise_kind):
    global noise_mos
    noise_mos= [0,0,0]
    noise_MOS_Evaluation = [0,0,0]
    os.system("dos2unix $PWD/Evaluation_Tool/dnsmos.py")
    p1=subprocess.run(["./$pwd/Evaluation_Tool/dnsmos.py --testset_dir part_wav_files"], capture_output=True, shell=True)
    p2=subprocess.run(["./$pwd/Evaluation_Tool/dnsmos.py --testset_dir noised/"+Noise_kind+"_noise"], capture_output=True, shell=True)
    p3=subprocess.run(["./$pwd/Evaluation_Tool/dnsmos.py --testset_dir "+Noise_kind+"/my_output"], capture_output=True, shell=True)

    if(p1!= 0):
        noise_MOS_Evaluation =[p1,p2,p3]
        noise_mos=[p1,p2,p3]
    return noise_MOS_Evaluation

def runEval_process():
    subprocess.run(["./$pwd/Evaluation_Tool/Run_Evaluation_Tool_multi_threads.py "+chosen_input_Noise+" "+input_ASR+" check"], stdout=subprocess.PIPE, shell=True)

def runEvaluationTool():
    t1=threading.Thread(target=runEval_process,)
    t2=threading.Thread(target=MOS_Claculator,args=(chosen_input_Noise,))
    t1.start()
    time.sleep(0.005)
    t2.start()

    #noise_mos= MOS_Claculator(chosen_input_Noise);
    t1.join()
    t2.join()
    #print(noise_mos[0].stdout.decode());
    noise_mos_p1=noise_mos[0].stdout.decode()
    noise_mos_p2=noise_mos[1].stdout.decode()
    noise_mos_p3=noise_mos[2].stdout.decode()
    if noise_mos[0].stdout.decode()=="":
        #noise_mos=[0,0,0]
        noise_mos_p1=0
        noise_mos_p2=0
        noise_mos_p3=0
    #white_mos = MOS_Claculator("white")
    t_result = tk.Text(root, width=80, height=20, bd=10, padx=5, pady=5)
    t_result.place(x=200,y=200)
    noise_string = readLineAndWrite(chosen_input_Noise);
    success_Enhancement_normalized_noise= score_calculator()
    white_string = readLineAndWrite("white");
    success_Enhancement_normalized_white= score_calculator()
    kind1=""
    kind2=""
    if(noise_string[0]!=" "):
        kind1 =chosen_input_Noise+"      "
    else:
        noise_string=["","",""]
    if(white_string!=" "):
        kind2 = "white      "
    else:
        white_string=["","",""]
    #print(noise_mos[0].stdout.decode())
    t_result.insert(INSERT,"Recognition Error Percentage Evaluation Tool Output:\n\n ")
    t_result.insert(INSERT,"                   "+kind1+" "+"Mos         "+kind2+"\n\n")
    t_result.insert(INSERT,"Clean Signal:       "+noise_string[1]+" "+str("%.2f" % float(noise_mos_p1))+"       "+white_string[1]+"\n\n")
    t_result.insert(INSERT,"Noised Signal:      "+noise_string[2]+" "+str("%.2f" % float(noise_mos_p2))+"       "+white_string[2]+"\n\n")
    t_result.insert(INSERT,"Processed Signal:   "+noise_string[0]+" "+str("%.2f" % float(noise_mos_p3))+"      "+white_string[0]+"\n\n")
    t_result.insert(INSERT,"Algorithm Score:    "+str("%.2f" % success_Enhancement_normalized_noise)+"          "+"          "+str("%.2f" % success_Enhancement_normalized_white)+"\n\n")


def RunSE():
    filename= filedialog.askopenfilename(initialdir="$pwd",title="Select File",
                                         filetypes=(("python","*.py"),("all files","*.*")))
    app = filename
    print(filename)
    label = tk.Label(frame,text=app,bg="gray")
    label.pack()
    subprocess.run([app+" "+chosen_input_Noise], stdout=subprocess.PIPE,shell=True)


def RunAddNoise():
    subprocess.run(["./$pwd/run_Add_Noise.sh "+chosen_input_Noise+" "+chosen_input_Noise_power], stdout=subprocess.PIPE, shell=True)

def ShowRandomSignalSpectrum():
    subprocess.run(["./$pwd/Find_Spectrum "+chosen_input_Noise], stdout=subprocess.PIPE, shell=True)


### Photos




def photos():
    cwd=os.getcwd()
    os.chdir(dirname(dirname(abspath(__file__))))
    print(os.getcwd())
    #/home/yotam/softwares/project/Images
    #os.getcwd()+
    Evaluation_photo_button = tk.PhotoImage(file =os.getcwd()+r"/Images/evaluation_button1.png").subsample(12, 16)
    openToCheck_photo_button = tk.PhotoImage(file =os.getcwd()+r"/Images/magnifying-glass-results.png").subsample(8, 9)
    addNoise_photo_button = tk.PhotoImage(file =os.getcwd()+r"/Images/SpeechEnhancement.png").subsample(3, 2)
    #Edit_photo_button = tk.PhotoImage(file =r"/home/yotam/softwares/project/Images/Edit1.png").subsample(2, 3)
    Edit_Text_photo_button = tk.PhotoImage(file =os.getcwd()+r"/Images/Edit_Text_file_button1.png").subsample(10, 15)
    Edit_wav_photo_button = tk.PhotoImage(file =os.getcwd()+r"/Images/Edit1.png").subsample(2, 3)
    SE_photo_button = tk.PhotoImage(file =os.getcwd()+r"/Images/noise_cancelling_final_logo2.png").subsample(6, 9)
    DataSize_photo_button = tk.PhotoImage(file =os.getcwd()+r"/Images/DtataSize.png").subsample(5, 7)
    DataNoised_photo_button = tk.PhotoImage(file =os.getcwd()+r"/Images/noised_data_creation.png").subsample(2, 3)
    signalSpectrum_photo_button = tk.PhotoImage(file =os.getcwd()+r"/Images/SignalSpectrum.png").subsample(4, 6)
    ### Canvas
    head_photo = tk.PhotoImage(file =os.getcwd()+r"/Images/Evaluation.png").subsample(2,2)
    bg_photo = tk.PhotoImage(file =os.getcwd()+r"/Images/watercolor-background-1.png").subsample(1,1)
    os.chdir(cwd)
    return [Evaluation_photo_button,openToCheck_photo_button,addNoise_photo_button,Edit_Text_photo_button,Edit_wav_photo_button,SE_photo_button,DataSize_photo_button,DataNoised_photo_button,signalSpectrum_photo_button,head_photo,bg_photo]







canvas = tk.Canvas(root, height=850,width=1000,bg="#263D42",highlightcolor="blue")

[Evaluation_photo_button,openToCheck_photo_button,addNoise_photo_button,Edit_Text_photo_button,Edit_wav_photo_button,SE_photo_button,DataSize_photo_button,DataNoised_photo_button,signalSpectrum_photo_button,head_photo,bg_photo]=photos()


### Create text file
### Create background and image
canvas.create_image(1,1,image=bg_photo,anchor="nw")
canvas.create_image(450,400,image=head_photo)

canvas.create_text(200,35,fill="black",font=("Helvetica",20),text="Choose Data Directory:")
canvas.create_text(170,120,fill="black",font=("Helvetica",20),text="Choose Data Size:")
canvas.create_text(250,520,fill="black",font=("Helvetica",20),text="Choose Result Name,Type & Kind:")


canvas.pack()


### Frames
frame = tk.Frame(root,bg="white")

### Buttons
#runEdit_but = tk.Button(root,justify="left",image=Edit_photo_button,text="Run Edit Tool",padx=10,
 #                       pady=5,fg="white",bg="#263D42",command= runEditTool).pack(side="left")
runEdit_wav_but = tk.Button(root,justify="left",image=Edit_wav_photo_button,text="Run Edit Tool",padx=10,
                        pady=5,fg="white",bg="#263D42",command= runEditWavTool).pack(side="left",padx=5)
runEdit_Text_but = tk.Button(root,justify="left",image=Edit_Text_photo_button,text="Run Edit Tool",padx=10,
                        pady=5,fg="white",bg="#263D42",command= runEditTextTool).pack(side="left",padx=5)
RunPartWav_but = tk.Button(root,image=DataSize_photo_button,text="open to check",
                            padx=10,pady=5,fg="white",bg="#263D42",command= runPartFilesCreate).pack(side="left",padx=5)
part_data_from_Noise_but = tk.Button(root,image=DataNoised_photo_button,text="open to check",
                            padx=10,pady=5,fg="white",bg="#263D42",command= create_part_data_from_Noise_dataset).pack(side="left",padx=5)
addNoise_but = tk.Button(root,image=addNoise_photo_button,text="Add noise",padx=10,pady=5,fg="white",bg="#263D42",command= RunAddNoise).pack(side="left",padx=5)
RunSE_but = tk.Button(root,image=SE_photo_button,text="Run SE Algorithm",padx=10,pady=5,fg="white",
                      bg="#263D42",command= RunSE).pack(side="left",padx=5)
RandomSigSpectrum_but = tk.Button(root,image=signalSpectrum_photo_button,text="open to check",
                            padx=10,pady=5,fg="white",bg="#263D42",command= ShowRandomSignalSpectrum).pack(side="left",padx=5)


runEvaluation_but = tk.Button(root,justify="left",image=Evaluation_photo_button,
                              text="Run Evaluation Tool",padx=5,pady=5,fg="white",bg="#263D42",command= runEvaluationTool).pack(side="left",padx=5,pady=10)


openToCheck_but = tk.Button(root,image=openToCheck_photo_button,text="open to check",
                            padx=10,pady=5,fg="white",bg="#263D42",command= open_to_check).pack(side="left",padx=5)




X_b=50
Y_b=65
diff_b=50

### Input buttons
ok_but1 = tk.Button(root,text="Main Directory",command=myClick_Main_Directory,fg="white",bg="#263D42").place(x=X_b, y=Y_b)
ok_but2 = tk.Button(root,text="New Data Size",command=myClick_Data_Size,fg="white",bg="#263D42").place(x=X_b, y=Y_b+25+diff_b)
ok_but3 = tk.Button(root,text="Result Input",command=myClick_Result,fg="white",bg="#263D42").place(x=X_b, y=Y_b+370+2*diff_b)
ok_but4 = tk.Button(root,text="Clean Sound",command=myClick_Clean_Sound,fg="white",bg="#263D42").place(x=X_b, y=Y_b+400+2*diff_b)
ok_but5 = tk.Button(root,text="Noised Sound",command=myClick_Noised_Sound,fg="white",bg="#263D42").place(x=X_b+150, y=Y_b+400+2*diff_b)
ok_but6 = tk.Button(root,text="Processed Sound",command=myClick_Processed_Sound,fg="white",bg="#263D42").place(x=X_b+300, y=Y_b+400+2*diff_b)
ok_but7 = tk.Button(root,text="Chosen Noise Input",command=choosenNoise,fg="white",bg="#263D42").place(x=X_b, y=Y_b+350+diff_b)
ok_but8 = tk.Button(root,text="Chosen Noise Ratio(db)",command=choosenNoisePower,fg="white",bg="#263D42").place(x=X_b+400, y=Y_b+350+diff_b)
ok_but9 = tk.Button(root,text="Chosen ASR",command=myClick_ASR_Choose,fg="white",bg="#263D42").place(x=X_b+520, y=Y_b+420+diff_b)

#ok_but = tk.Button(root,text="Result Input",command=myClick).place(x=100, y=50)

X_e=200
Y_e=70
diff_e=50
### Enteries
e_dir = tk.Entry(root, width=50)
#t_dir = tk.Text(root,width=50,height=10,bd=25,padx=5,pady=5)
e_dir.place(x=X_e+20, y=Y_e)
#t_dir.place(x=X_e, y=Y_e)

e_Data = tk.Entry(root, width=30)
e_Data.place(x=X_e+20, y=Y_e+25+diff_e)

e_result = tk.Entry(root, width=50)
e_result.place(x=X_e, y=Y_e+370+2*diff_e)

e_Noise = tk.Entry(root, width=30)
e_Noise.place(x=X_e+20, y=Y_e+350+diff_e)

e_Noise_power = tk.Entry(root, width=30)
e_Noise_power.place(x=X_e+440, y=Y_e+350+diff_e)

e_ASR = tk.Entry(root, width=30)
e_ASR.place(x=X_e+500, y=Y_e+420+diff_e)

## Headlines:




root.mainloop()


def photos_do():
    cwd=os.getcwd()
    #os.chdir(dirname(dirname(abspath(__file__))))

    print(os.getcwd())
    #/home/yotam/softwares/project/Images
    #os.getcwd()+
    Evaluation_photo_button = tk.PhotoImage(file =r"/home/yotam/softwares/project/Images/evaluation_button1.png").subsample(12, 16)
    openToCheck_photo_button = tk.PhotoImage(file =r"/home/yotam/softwares/project/Images/magnifying-glass-results.png").subsample(8, 9)
    addNoise_photo_button = tk.PhotoImage(file =r"/home/yotam/softwares/project/Images/SpeechEnhancement.png").subsample(3, 2)
    #Edit_photo_button = tk.PhotoImage(file =r"/home/yotam/softwares/project/Images/Edit1.png").subsample(2, 3)
    Edit_Text_photo_button = tk.PhotoImage(file =r"/home/yotam/softwares/project/Images/Edit_Text_file_button1.png").subsample(10, 15)
    Edit_wav_photo_button = tk.PhotoImage(file =r"/home/yotam/softwares/project/Images/Edit1.png").subsample(2, 3)
    SE_photo_button = tk.PhotoImage(file =r"/home/yotam/softwares/project/Images/noise_cancelling_final_logo2.png").subsample(6, 9)
    DataSize_photo_button = tk.PhotoImage(file =r"/home/yotam/softwares/project/Images/DtataSize.png").subsample(5, 7)
    DataNoised_photo_button = tk.PhotoImage(file =r"/home/yotam/softwares/project/Images/noised_data_creation.png").subsample(5, 7)

    ### Canvas
    head_photo = tk.PhotoImage(file =r"/home/yotam/softwares/project/Images/Evaluation.png").subsample(2,2)
    bg_photo = tk.PhotoImage(file =r"/home/yotam/softwares/project/Images/watercolor-background-1.png").subsample(2,1)
    os.chdir(cwd)
    return [Evaluation_photo_button,openToCheck_photo_button,addNoise_photo_button,Edit_Text_photo_button,Edit_wav_photo_button,SE_photo_button,DataSize_photo_button,DataNoised_photo_button,head_photo,bg_photo]


#subprocess.run(["./$pwd/dnsmos.py --testset_dir part_wav_files >$PWD/MOS/"+Noise_kind+"/clean"], capture_output=True, shell=True)
#    subprocess.run(["./$pwd/dnsmos.py --testset_dir noised/"+Noise_kind+" >$PWD/MOS/"+Noise_kind+"/noisy"], capture_output=True, shell=True)
#    subprocess.run(["./$pwd/dnsmos.py --testset_dir "+Noise_kind+"/my_output >$PWD/MOS/"+Noise_kind+"/processed"], capture_output=True, shell=True)


'''
    while True:
        count += 1

        # Get next line from file
        i=0;
        while(i<=2):
            string[0] = line;
            i+=1
        while (i <= 4):
            string[0] = line;
            i += 1
            line = file.readline()
        if(line == "Signals processed by SE algorithm:"):
            line = file.readline();
            print(line)
            string[0]= line;
        if(line == "Clean signals precessed:"):
            line = file.readline();
            print(line)
            string[1] = line;
        if(line =="Noised signals without SE processing:"):
            line = file.readline();
            print(line)
            string[2] = line;
        # if line is empty
        # end of file is reached
        if not line:
            break
    file.close()
'''
