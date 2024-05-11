import tkinter as tk
import os
from playsound import playsound
from tkinter import filedialog

def playMusic():
    playsound("")

def runPlayer():
    print("run_player")

#GUI
root = tk.Tk()
root.geometry("250x250")

#Runボタン
runButton = tk.Button(root, text = "Run", command = runPlayer)
runButton.place(x=110, y=30)

root.mainloop()