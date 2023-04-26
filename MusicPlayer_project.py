import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

music_player = tkr.Tk()
music_player.title("MUSIC BOT")
music_player.geometry("900x450")
directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()

play_list = tkr.Listbox(music_player, font="Arial 12 italic", bg='white', selectmode=tkr.SINGLE)
for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1
pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()
def queue():
    pygame.mixer.music.queue()
Button1 = tkr.Button(music_player, width=5, height=3, font="Arial 12 bold", text="PLAY", command=play, bg="green", fg="white")
Button2 = tkr.Button(music_player, width=5, height=3, font="Arial 12 bold", text="STOP", command=stop, bg="red", fg="white")
Button3 = tkr.Button(music_player, width=5, height=3, font="Arial 12 bold", text="PAUSE", command=pause, bg="blue", fg="white")
Button4 = tkr.Button(music_player, width=5, height=3, font="Arial 12 bold", text="UNPAUSE", command=unpause, bg="blue", fg="white")
Button5 = tkr.Button(music_player, width=5, height=3, font="Arial 12 bold", text="QUEUE", command=queue, bg="black", fg="white")
Button6 = tkr.Button(music_player, width=5, height=3, font="Arial 12 bold", text="NEXT", command=next, bg="blue", fg="white")

var = tkr.StringVar() 
song_title = tkr.Label(music_player, font="Helvetica 12 bold", textvariable=var)

song_title.pack()
Button1.pack(side="left", padx=5)
Button2.pack(side="left", padx=5)
Button3.pack(side="left", padx=5)
Button4.pack(side="left", padx=5)
Button5.pack(fill="both", expand="no")
Button6.pack(fill="both", expand="no")
play_list.pack(fill="both", expand="yes")
music_player.mainloop()