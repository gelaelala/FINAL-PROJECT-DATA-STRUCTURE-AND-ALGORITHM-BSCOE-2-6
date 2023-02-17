from tkinter import filedialog
from tkinter import *
import pygame
import os

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

# creating frames for control buttons
control_frame = Frame(window)
control_frame.pack()

# creating the buttons themselves inside the frame
play_btn = Button (control_frame, image = play_btn_image, borderwidth = 0)
pause_btn = Button (control_frame, image = pause_btn_image, borderwidth = 0)
previous_btn = Button (control_frame, image = previous_btn_image, borderwidth = 0)
next_btn = Button (control_frame, image = next_btn_image, borderwidth = 0)

# displaying the buttons on screen
play_btn.grid (row = 0, column = 1, padx = 7, pady = 10)
pause_btn.grid (row = 0, column = 2, padx = 7, pady = 10)
previous_btn.grid (row = 0, column = 3, padx = 7, pady = 10)
next_btn.grid (row = 0, column = 0, padx = 7, pady = 10)

# runs the application
window.mainloop()
