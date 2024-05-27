import tkinter as tk
import os
import pygame as pg
from tkinter import filedialog

selected_file = None
loop = False
paused = False
pause_position = 0.0

# pygameの初期化
pg.init()
pg.mixer.init()

# mp3ファイルのリスト
def loadMusicFiles():
    music_folder = "music_files"
    music_files = [f for f in os.listdir(music_folder) if f.endswith('.mp3')]
    return music_files

# 音楽選択メソッド
def selectMusic():
    global selected_file
    selected_file = filedialog.askopenfilename(initialdir="music_files", title="Select Music File", filetypes=(("MP3 files", "*.mp3"), ("All files", "*.*")))
    if selected_file:
        currentMusicLabel.config(text=f"Selected: {os.path.basename(selected_file)}")
        print("Selected music:", selected_file)

# 音楽再生メソッド
def playMusic(start_pos=0.0):
    global selected_file, paused, pause_position
    if selected_file:
        music_folder = "music_files"
        file_path = os.path.join(music_folder, selected_file)
        pg.mixer.music.load(file_path)
        pg.mixer.music.play(-1 if loop else 0, start=start_pos)
        currentMusicLabel.config(text=f"Playing: {os.path.basename(selected_file)}")
        paused = False
        pause_position = 0.0

# 再生停止
def stopMusic():
    global paused, pause_position
    pg.mixer.music.stop()
    currentMusicLabel.config(text="No music playing")
    paused = False
    pause_position = 0.0

# 一時停止
def pauseMusic():
    global paused, pause_position
    if paused:
        pg.mixer.music.play(-1 if loop else 0, start=pause_position)
        currentMusicLabel.config(text=f"Playing: {os.path.basename(selected_file)}")
        pauseButton.config(text="Pause Music")
    else:
        pause_position = pg.mixer.music.get_pos() / 1000.0
        pg.mixer.music.pause()
        currentMusicLabel.config(text="Paused")
        pauseButton.config(text="Restart Music")
    paused = not paused

# 音量調整
def setVolume(val):
    volume = float(val) / 100
    pg.mixer.music.set_volume(volume)

# ループ再生の切り替え
def changeLoop():
    global loop
    loop = not loop
    loopButton.config(text="Loop: On" if loop else "Loop: Off")
    if pg.mixer.music.get_busy():
        current_pos = pg.mixer.music.get_pos() / 1000.0
        pg.mixer.music.stop()
        playMusic(start_pos=current_pos)

# GUI
root = tk.Tk()
root.geometry("400x500")
root.title("Music Player")

def onSelect(event):
    global selected_file
    selected_index = listbox.curselection()
    if selected_index:
        selected_file = listbox.get(selected_index[0])
        currentMusicLabel.config(text=f"Selected: {selected_file}")

# 音楽リスト
music_files = loadMusicFiles()
listbox = tk.Listbox(root, selectmode=tk.SINGLE)
for file in music_files:
    listbox.insert(tk.END, file)
listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
listbox.bind('<<ListboxSelect>>', onSelect)

# 再生中の音楽ラベルの表示
currentMusicLabel = tk.Label(root, text="No music playing")
currentMusicLabel.pack(pady=5)

# playボタン
playButton = tk.Button(root, text="Play Music", command=playMusic)
playButton.pack(pady=10)

# stopボタン
stopButton = tk.Button(root, text="Stop Music", command=stopMusic)
stopButton.pack(pady=10)

# pauseボタン
pauseButton = tk.Button(root, text="Pause Music", command=pauseMusic)
pauseButton.pack(pady=10)

# loopボタン
loopButton = tk.Button(root, text="Loop: Off", command=changeLoop)
loopButton.pack(pady=10)

# ボリューム調整スライダー
volumeSlider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="Volume", command=setVolume)
volumeSlider.set(50)
volumeSlider.pack(pady=10)

# selectイベント
listbox.bind("<<ListboxSelect>>", onSelect)

# メインループ
root.mainloop()
