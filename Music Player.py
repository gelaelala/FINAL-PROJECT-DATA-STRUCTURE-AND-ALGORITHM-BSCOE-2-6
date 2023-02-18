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
window.geometry("700x300")
window.resizable (True, True)

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

'''
# creating function for getting the total length of the song and to display on screen
def total_length ():
    global current_song, paused
    
    current_song = songs[songlist.curselection()[0]]
    song_mp3 = MP3(current_song)
    song_length = song_mp3.info.length
    convert_song_length = time.strftime('%M:%S', time.gmtime(song_length))

    time_bar.config(text = convert_song_length)
'''

# creating load music command
def load_music():
    global current_song
    window.directory = filedialog.askdirectory()

    """ iterating over files in chosen directory, splitting up filename into the filename itself and filename ext, 
    and if the filename ext is mp3 then add the song into the songs list """
    for song in os.listdir(window.directory):
        name, ext = os.path.splitext(song)
        if ext == '.mp3' or '.wav':
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
        pygame.mixer.music.load(os.path.join(window.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False
    
    #total_length ()
    
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

'''
# creating frame for total lenght of the song and its current time
time_bar = Label(window, text = "", padx = 10, anchor = W)
time_bar.pack(fill = X, side = BOTTOM, pady = 2)
'''

# creating the buttons themselves inside the frame and making it functional
play_btn = Button (control_frame, image = play_btn_image, borderwidth = 0, command = play_music)
pause_btn = Button (control_frame, image = pause_btn_image, borderwidth = 0, command = pause_music)
previous_btn = Button (control_frame, image = previous_btn_image, borderwidth = 0, command = previous_music)
next_btn = Button (control_frame, image = next_btn_image, borderwidth = 0, command = next_music)
shuffle_btn = Button (control_frame, image = shuffle_btn_image, borderwidth = 0, command = shuffle_music)
repeat_btn = Button (control_frame, image = repeat_btn_image, borderwidth = 0, command = repeat_music)
volume_control = ttk.Scale(control_frame, from_ = 1, to = 0, value = 1, orient = HORIZONTAL, length = 125, command = music_volume)

# displaying the buttons on screen
play_btn.grid (row = 0, column = 2, padx = 7, pady = 10, sticky = NSEW)
pause_btn.grid (row = 0, column = 3, padx = 7, pady = 10, sticky = NSEW)
previous_btn.grid (row = 0, column = 1, padx = 7, pady = 10, sticky = NSEW)
next_btn.grid (row = 0, column = 4, padx = 7, pady = 10, sticky = NSEW)
shuffle_btn.grid (row = 0, column = 0, padx = 7, pady = 10, sticky = NSEW)
repeat_btn.grid (row = 0, column = 5, padx = 7, pady = 10, sticky = NSEW)
volume_control.grid (row = 0, column = 6, padx = 7, pady = 10, sticky = NSEW)

# runs the application
window.mainloop()