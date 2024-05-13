import tkinter as tk
import os
import pygame as pg
from tkinter import filedialog

pg.init()

def playMusic():
    music_folder = "music_files"
    music_file = "ゆきうさだるま.mp3"
    folder_path = os.path.abspath(music_folder)
    file_path = os.path.join(folder_path, music_file)

    pg.mixer.music.load(file_path)
    pg.mixer.music.play()
    
    
    # while pg.mixer.music.get_busy():
    #     pg.time.Clock().tick(10)
    
    # pg.quit()

def stopMusic():
    pg.mixer.music.stop()

#GUI
root = tk.Tk()
root.geometry("300x300")

# selectボタン
#selectButton = tk.Button(root, text="Select Music", command=selectMusic)
#selectButton.pack(pady=10)

# playボタン
playButton = tk.Button(root, text="Play Music", command=playMusic)
playButton.pack(pady=10)

# stopボタン
stopButton = tk.Button(root, text="Stop Music", command=stopMusic)
stopButton.pack(pady=10)

root.mainloop()