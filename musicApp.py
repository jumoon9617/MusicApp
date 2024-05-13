import tkinter as tk
import os
import pygame as pg
from tkinter import filedialog

pg.init()

def playMusic(file_path):
    pg.mixer.music.load(file_path)
    pg.mixer.music.play()
    
    while pg.mixer.music.get_busy():
        pg.time.Clock().tick(10)
    
    pg.quit()

def runPlayer():
    print("run_player")

#GUI
root = tk.Tk()
root.geometry("300x300")

#selectボタン
selectButton = tk.Button(root, text = "Run", command = runPlayer)
selectButton.pack(pady=10)
selectButton.place(x=150, y=150)

file_list = tk.Listbox(root, selectmode=tk.SINGLE)
#file_list.pack(pady=10)

root.mainloop()