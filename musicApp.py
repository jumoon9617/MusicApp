import tkinter as tk
import os
import pygame as pg
from tkinter import filedialog

selected_file=None

#pygameの初期化
pg.init()
pg.mixer.init()

#mp3ファイルのリスト
def loadMusicFiles():
    music_folder = "music_files"
    music_files = [f for f in os.listdir(music_folder) if f.endswith('.mp3')]
    return music_files

#音楽選択メソッド
def selectMusic():
    global selected_file
    selected_file = filedialog.askopenfilename(initialdir="music_files", title="Select Music File", filetypes=(("MP3 files", "*.mp3"), ("All files", "*.*")))
    #print("Selected music:", selected_file)

#音楽再生メソッド
def playMusic():
    music_folder = "music_files"
    file_path = os.path.join(music_folder, selected_file)
    pg.mixer.music.load(file_path)
    pg.mixer.music.play()
    
    # while pg.mixer.music.get_busy():
    #     pg.time.Clock().tick(10)
    
    # pg.quit()

#再生停止
def stopMusic():
    pg.mixer.music.stop()

#GUI
root = tk.Tk()
root.geometry("400x300")
root.title("Music Player")

def onSelect(event):
    global selected_file
    selected_index = listbox.curselection()
    if selected_index:
        selected_file = listbox.get(selected_index[0])

#音楽リスト
music_files = loadMusicFiles()
listbox = tk.Listbox(root, selectmode=tk.SINGLE)
for file in music_files:
    listbox.insert(tk.END, file)
listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
listbox.bind('<<ListboxSelect>>', onSelect)

# playボタン
playButton = tk.Button(root, text="Play Music", command=playMusic)
playButton.pack(pady=10)

# stopボタン
stopButton = tk.Button(root, text="Stop Music", command=stopMusic)
stopButton.pack(pady=10)

#selectイベント
listbox.bind("<<ListboxSelect>>", onSelect)

#メインループ
root.mainloop()