#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog,Text
from tkinter.ttk import *
import subprocess
import numpy as np
import time
import threading
import speech_recognition as sr
import simpleaudio as sa
import os
from os import path
from os.path import dirname, abspath
import sys

root = tk.Tk()
apps = []


def myClick():
    global input
    input = e.get()
    return input


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


def runApps():
    for app in apps:
        subprocess.run([app], stdout=subprocess.PIPE,shell=True)


def open_to_check():
    subprocess.run(["./$pwd/Open_test_to_check.sh "+ input], stdout=subprocess.PIPE, shell=True)


def runEditTool():
    subprocess.run(["./$pwd/Run_Edit_Tool.py"], stdout=subprocess.PIPE, shell=True)

def runEditWavTool():
    subprocess.run(["./$pwd/Edit_Tool/Run_Edit_WAV_Tool.py"], stdout=subprocess.PIPE, shell=True)

#def OpenResult():
#    subprocess.run(["./$pwd/Edit_Tool/Run_Edit_Text_Tool.py"], stdout=subprocess.PIPE, shell=True)

def runEditTextTool():
    subprocess.run(["./$pwd/Edit_Tool/Run_Edit_Text_Tool.py"], stdout=subprocess.PIPE, shell=True)


def runEvaluationTool():
    subprocess.run(["./$pwd/Evaluation_Tool/Run_Evaluation_Tool.py"], stdout=subprocess.PIPE, shell=True)


def RunSE():
    filename= filedialog.askopenfilename(initialdir="$pwd",title="Select File",
                                         filetypes=(("python","*.py"),("all files","*.*")))
    app = filename
    print(filename)
    label = tk.Label(frame,text=app,bg="gray")
    label.pack()
    subprocess.run([app], stdout=subprocess.PIPE,shell=True)


### Photos

def photos():
    cwd=os.getcwd()
    os.chdir(dirname(dirname(abspath(__file__))))
    print(os.getcwd())
    Evaluation_photo_button = tk.PhotoImage(file =os.getcwd()+r"/Images/evaluation_button1.png").subsample(12, 16)
    openToCheck_photo_button = tk.PhotoImage(file =os.getcwd()+r"/Images/magnifying-glass-results.png").subsample(8, 9)
    #Edit_photo_button = tk.PhotoImage(file =r"/home/yotam/softwares/project/Images/Edit1.png").subsample(2, 3)
    Edit_Text_photo_button = tk.PhotoImage(file =os.getcwd()+r"/Images/Edit_Text_file_button1.png").subsample(10, 15)
    Edit_wav_photo_button = tk.PhotoImage(file =os.getcwd()+r"/Images/Edit1.png").subsample(2, 3)
    SE_photo_button = tk.PhotoImage(file =os.getcwd()+r"/Images/SpeechEnhancement.png").subsample(3, 2)
    ### Canvas
    head_photo = tk.PhotoImage(file =os.getcwd()+r"/Images/Evaluation.png").subsample(2,2)
    bg_photo = tk.PhotoImage(file =os.getcwd()+r"/Images/watercolor-background-1.png").subsample(2,1)
    os.chdir(cwd)
    return [Evaluation_photo_button,openToCheck_photo_button,Edit_Text_photo_button,Edit_wav_photo_button,SE_photo_button,head_photo,bg_photo]


canvas = tk.Canvas(root, height=700,width=700,bg="#263D42",highlightcolor="blue")

[Evaluation_photo_button,openToCheck_photo_button,Edit_Text_photo_button,Edit_wav_photo_button,SE_photo_button,head_photo,bg_photo]=photos()
### Create text file
canvas.create_text(350,10,fill="darkblue",font="Times 20 italic bold",text="Evaluation App")
### Create background and image
canvas.create_image(1,1,image=bg_photo,anchor="nw")
canvas.create_image(400,350,image=head_photo)

canvas.pack()


### Frames
frame = tk.Frame(root,bg="white")

### Buttons
ok_but = tk.Button(root,text="Enter Your Choice",command=myClick).place(x=275, y=50)
#runEdit_but = tk.Button(root,justify="left",image=Edit_photo_button,text="Run Edit Tool",padx=10,
 #                       pady=5,fg="white",bg="#263D42",command= runEditTool).pack(side="left")

runEvaluation_but = tk.Button(root,justify="left",image=Evaluation_photo_button,
                              text="Run Evaluation Tool",padx=5,pady=5,fg="white",bg="#263D42",command= runEvaluationTool).pack(side="left")
runEdit_Text_but = tk.Button(root,justify="left",image=Edit_Text_photo_button,text="Run Edit Tool",padx=10,
                        pady=5,fg="white",bg="#263D42",command= runEditTextTool).pack(side="left")
runEdit_wav_but = tk.Button(root,justify="left",image=Edit_wav_photo_button,text="Run Edit Tool",padx=10,
                        pady=5,fg="white",bg="#263D42",command= runEditWavTool).pack(side="left")
RunSE_but = tk.Button(root,image=SE_photo_button,text="Run SE Algorithm",padx=10,pady=5,fg="white",
                      bg="#263D42",command= RunSE).pack(side="left")
openToCheck_but = tk.Button(root,image=openToCheck_photo_button,text="Run SE Algorithm",
                            padx=10,pady=5,fg="white",bg="#263D42",command= open_to_check).pack(side="left")

e = Entry(root, width=50)
input = e.get()

e.place(x=175, y=25)

root.mainloop()



