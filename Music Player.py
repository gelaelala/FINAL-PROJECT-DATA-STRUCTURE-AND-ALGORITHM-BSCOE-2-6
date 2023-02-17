# program reference before modifications: https://youtu.be/SCos1o368iE

from tkinter import filedialog
from tkinter import *
import pygame
import os
import random

# creating window for the application
window = Tk()
window.title('Music Player')
window.geometry("500x300")

# initialize pygame music mixer
pygame.mixer.init()

# creating menu bar
menubar = Menu (window)
window.config (menu = menubar)

songs = []
current_song = ""
song_number = 0
paused = False

# creating load music command
def load_music():
    global current_song
    window.directory = filedialog.askdirectory()

    """ iterating over files in chosen directory, splitting up filename into the filename itself and filename ext, 
    and if the filename ext is mp3 then add the song into the songs list """
    for song in os.listdir(window.directory):
        name, ext = os.path.splitext(song)
        if ext == '.mp3':
            songs.append(song)

    # add songs into the listbox
    for song in songs:
        songlist.insert ("end", song)
    
    songlist.select_set(0) # selecting the first song on the playlist
    current_song = songs[songlist.curselection()[0]]

def play_music ():
    global current_song, paused

    if not paused:
        pygame.mixer.music.load(os.path.join(window.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False
    
def pause_music ():
    global paused 
    pygame.mixer.music.pause()
    paused = True

def previous_music ():
    global current_song, paused

    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) - 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

def next_music ():
    global current_song, paused

    try:
        songlist.select_clear (0, END)
        songlist.selection_set (songs.index(current_song) + 1)
        current_song = songs[songlist.curselection()[0]]
        play_music ()
    except:
        pass

def shuffle_music ():
    global current_song, paused

    random.shuffle (songs)
    songlist.select_set (songs.index(current_song))
    current_song = songs[songlist.curselection()[song_number]]
    play_music ()

def repeat_music ():
    pass

# organise menu
organize_menu = Menu(menubar, tearoff = False)
organize_menu.add_command(label = 'Select Folder', command = load_music)
menubar.add_cascade (label = 'Organize', menu = organize_menu)

# creating list box for the songs
songlist = Listbox(window, bg = 'black', fg = 'white', width = 100, height = 15)
songlist.pack()

# import images for buttons
play_btn_image = PhotoImage(file = 'play.png')
pause_btn_image = PhotoImage(file = 'pause.png')
previous_btn_image = PhotoImage(file = 'previous.png')
next_btn_image = PhotoImage(file ='next.png')
shuffle_btn_image = PhotoImage(file = 'shuffle.png')
repeat_btn_image = PhotoImage(file = "repeat.png")

# creating frames for control buttons
control_frame = Frame(window)
control_frame.pack()

# creating the buttons themselves inside the frame and making it functional
play_btn = Button (control_frame, image = play_btn_image, borderwidth = 0, command = play_music)
pause_btn = Button (control_frame, image = pause_btn_image, borderwidth = 0, command = pause_music)
previous_btn = Button (control_frame, image = previous_btn_image, borderwidth = 0, command = previous_music)
next_btn = Button (control_frame, image = next_btn_image, borderwidth = 0, command = next_music)
shuffle_btn = Button (control_frame, image = shuffle_btn_image, borderwidth = 0, command = shuffle_music)
repeat_btn = Button (control_frame, image = repeat_btn_image, borderwidth = 0, command = repeat_music)

# displaying the buttons on screen
play_btn.grid (row = 0, column = 2, padx = 7, pady = 10)
pause_btn.grid (row = 0, column = 3, padx = 7, pady = 10)
previous_btn.grid (row = 0, column = 1, padx = 7, pady = 10)
next_btn.grid (row = 0, column = 4, padx = 7, pady = 10)
shuffle_btn.grid (row = 0, column = 0, padx = 7, pady = 10)
repeat_btn.grid (row = 0, column = 5, padx = 7, pady = 10)

# runs the application
window.mainloop()
