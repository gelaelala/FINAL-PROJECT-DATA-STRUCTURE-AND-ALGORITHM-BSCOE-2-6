# program reference before modifications: https://youtu.be/SCos1o368iE

from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from mutagen.mp3 import MP3
import pygame
import os
import random
import time

# creating window for the application
window = Tk()
window.title('Music Player')
#window.geometry("450x300")
window.minsize(width = 450, height = 300) # once program opens, the window size will be this (window can't be smaller than the minsize)
window.resizable (True, True) # can resize the window according to the user as well as make it fullscreen

# initialize pygame music mixer
pygame.mixer.init()

# creating menu bar
menubar = Menu (window)
window.config (menu = menubar)

songs = []
current_song = ""
song_number = 0
paused = False
volume = ''

# creating function for getting the total length of the song and to display on screen
def song_time ():
    global current_song, paused
    
    current_time = pygame.mixer.music.get_pos() / 1000
    current_time_cnvrt = time.strftime("%M:%S", time.gmtime(current_time))

    current_song = songs[songlist.curselection()[0]]
    path = os.path.realpath(current_song)
    song = MP3(path)
    total_length = song.info.length
    total_length_cnvrt = time.strftime("%M:%S", time.gmtime(total_length))
    
    time_song.config(text = f'{current_time_cnvrt} / {total_length_cnvrt}')
    time_song.after(1000, song_time)

# creating load music command
def load_music():
    global current_song
    files = filedialog.askdirectory()
    os.chdir(files)

    """ iterating over files in chosen directory, splitting up filename into the filename itself and filename ext, 
    and if the filename ext is mp3 then add the song into the songs list """
    for song in os.listdir(files):
        if song.endswith(".mp3"):
            realdir = os.path.realpath(song)
            songs.append(song)

    # add songs into the listbox
    for song in songs:
        songlist.insert ("end", song)
    
    songlist.select_set(0) # selecting the first song on the playlist
    current_song = songs[songlist.curselection()[0]]

def add_song ():
    pass
    '''
    global current_song
    files = filedialog.askopenfilename(initialdir = "/", title = "Select Audio/s", filetypes = (("mp3 File", "*.mp3"), (".wav File", "*.wav")))

    songlist.insert ("end", files)
    '''

def remove_song ():
    global current_song

    songlist.delete (ANCHOR)
    pygame.mixer.music.stop()
    songlist.selection_set (songs.index(current_song) + 1)
    current_song = songs[songlist.curselection()[0]]
    play_music()

def remove_playlist ():
    songlist.delete (0, "end")
    pygame.mixer.music.stop ()

def play_music ():
    global current_song, paused

    if not paused:
        pygame.mixer.music.load(current_song)
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False
    
    song_time()
    
def pause_music ():
    global paused 
    pygame.mixer.music.pause()
    paused = True

def previous_music ():
    global current_song, paused

    try:
        songlist_length = songlist.size()
        if songs.index(current_song) == 0:
            songlist.selection_set(songlist_length- 1)
            current_song = songs[songlist.curselection()[-1]]
            play_music() 
        else:
            songlist.selection_clear(0, END)
            songlist.selection_set(songs.index(current_song) - 1)
            current_song = songs[songlist.curselection()[0]]
            play_music()
    except:
        pass

def next_music ():
    global current_song, paused

    try:
        songlist_length = songlist.size()
        if songlist_length-1 == songs.index(current_song):
            songlist.selection_set(0)
            current_song = songs[songlist.curselection()[0]]
            play_music() 
        else:
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
    global current_song, paused

    pygame.mixer.music.play (-1) # song will be indefinitely repeated

def music_volume (vol):
    pygame.mixer.music.set_volume(volume_control.get())

def time_bar (bar):
    pass


# select folder menu
select_menu = Menu(menubar, tearoff = False)
select_menu.add_command(label = 'Select Folder', command = load_music)
menubar.add_cascade (label = 'Playlist', menu = select_menu)

# manually add songs
addSong_menu = Menu(menubar, tearoff = False)
addSong_menu.add_command(label = 'Add Song', command = add_song)
menubar.add_cascade (label = "Add", menu = addSong_menu)

# remove songs from the playlist/remove entire playlist
removeSong_menu = Menu (menubar, tearoff = False)
removeSong_menu.add_command (label = "Remove Song", command = remove_song)
removeSong_menu.add_command (label = "Remove Playlist", command = remove_playlist)
menubar.add_cascade (label = "Remove", menu = removeSong_menu)

# creating list box for the songs
songlist = Listbox(window, bg = 'black', fg = 'white', selectbackground = "gray")
songlist.pack(fill = BOTH, expand = True)

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

# creating label for total lenght of the song and its current time
time_song = Label(window, text = "", bd = 2, anchor = W)
time_song.pack (fill = X, side = BOTTOM, ipady = 10)


# creating the buttons themselves inside the frame and making it functional
play_btn = Button (control_frame, image = play_btn_image, borderwidth = 0, command = play_music)
pause_btn = Button (control_frame, image = pause_btn_image, borderwidth = 0, command = pause_music)
previous_btn = Button (control_frame, image = previous_btn_image, borderwidth = 0, command = previous_music)
next_btn = Button (control_frame, image = next_btn_image, borderwidth = 0, command = next_music)
shuffle_btn = Button (control_frame, image = shuffle_btn_image, borderwidth = 0, command = shuffle_music)
repeat_btn = Button (control_frame, image = repeat_btn_image, borderwidth = 0, command = repeat_music)
volume_control = ttk.Scale(control_frame, from_ = 1, to = 0, value = 1, orient = HORIZONTAL, length = 125, command = music_volume)
timebar = ttk.Scale(control_frame, from_ = 0, to = 100, orient = HORIZONTAL, value = 0, length = 430, command = time_bar)

# displaying the buttons on screen
play_btn.grid (row = 0, column = 2, padx = 7, pady = 15, sticky = NSEW)
pause_btn.grid (row = 0, column = 3, padx = 7, pady = 15, sticky = NSEW)
previous_btn.grid (row = 0, column = 1, padx = 7, pady = 15, sticky = NSEW)
next_btn.grid (row = 0, column = 4, padx = 7, pady = 15, sticky = NSEW)
shuffle_btn.grid (row = 0, column = 0, padx = 7, pady = 15, sticky = NSEW)
repeat_btn.grid (row = 0, column = 5, padx = 7, pady = 15, sticky = NSEW)
volume_control.grid (row = 0, column = 6, padx = 7, pady = 15, sticky = NSEW)
timebar.grid (row = 1, column = 0, columnspan = 7, pady = 10)

# runs the application
window.mainloop()