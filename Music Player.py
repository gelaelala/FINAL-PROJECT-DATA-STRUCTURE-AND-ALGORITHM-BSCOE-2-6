from tkinter import *
import pygame
import os

# creating window for the application
window = Tk()
window.title('Music Player')
window.geometry("500x300")

# initialize pygame music mixer
pygame.mixer.init()

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
