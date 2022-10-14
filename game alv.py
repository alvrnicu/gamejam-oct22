from ctypes import resize
from importlib.abc import ResourceReader
from re import T
from tkinter.tix import ButtonBox
from turtle import Screen, color, title
from tkinter import *
from graphics_lib import *
import random
import time
###Cat reflex game, have cat move on a predetermined track at increasing velocity as a function of time while the user attempts to hit spacebar every time the cat passes
#over a mouse that appears, at random, on the track. Use collision/overlap detection to determine if they get a point or lose a life. Also have a score counter at bottom left or
#something.

WINDOW_WIDTH = 768
WINDOW_HEIGHT = 1024
# mouse_width = 500
# mouse_height = 500
# cat_x = 670
# cat_y = 850
# mouse_x = 100
# mouse_y = 200



#necessary to call Tk() first
t = Tk()

#Set the size of the window and prevent resizing by user
t.geometry("768x1024")
t.maxsize(768, 1024)
t.minsize(768, 1024)

#Little header with name of the game and a message
title_text = Label(t, text = "Welcome to Mousey Hunter!\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
title_text.pack()

#Defining a function to call when Quit button is hit
def quit_button():
        t.destroy()

#Create a scenic background for the game to occur on. See if I can draw my own and insert it somehow
board = Canvas(t, width = 1024, height = 900, bg = '#ADD8E6')
board.place(x = 0, y = 50)
   

#image that will represent the cat on the track. kitty.png is placeholder, will try to draw me own if I have time
image1 = PhotoImage(file = 'kitty.png').subsample(5, 5)
cat_img = image1
rescuer = board.create_image(670, 850, anchor = 's', image = image1)

class Mouse():
        image2 = PhotoImage(file = 'mouse.png').subsample(30, 30)
        mouse_img = image2
        board.create_image(100, 200, image = image2)
        board.create_image(500, 400, image = image2)
        board.create_image(200, 600, image = image2)


score = 0

#Collision Detection b/t cat and mouse
# def collision():
#         xdiff = abs(cat_img.x - mouse_img.x)
#         ydiff = abs(cat_img.y - mouse_img.y)
        
#         if xdiff <=20 and ydiff <=20:
#                 print('CAUGHT ONE!')
#                 score += 1

def moveright(event):
        board.move(rescuer, 10, 0)
        print(score)
        
def moveleft(event):
        board.move(rescuer, -10, 0)
        print(score)

def moveup(event):
        board.move(rescuer, 0, -10)
        print(score)

def movedown(event):
        board.move(rescuer, 0, 10)
        print(score)


board.bind_all("<Right>", moveright)
board.bind_all("<Left>", moveleft)
board.bind_all("<Up>", moveup)
board.bind_all("<Down>", movedown)

print(score)


#Button to exit the game
quit_button = Button(t, text = 'Quit', padx = 15, pady = 5, command = quit_button, bg = "#FFCCCB")
quit_button.place(x = 690, y = 975)

# class Canvas:
#         def pic(rescuer):
#                 #Create a scenic background for the game to occur on. See if I can draw my own and insert it somehow
#                 board = Canvas(t, width = 1024, height = 900, bg = '#ADD8E6')
#                 board.place(x = 0, y = 50)

#                 #custom image that will represent the cat on the track. kitty.png is placeholder
#                 image1 = PhotoImage(file = 'images/kitty.png')

#                 #Resizing cat to more appropriate dimensions for game
#                 image1 = image1.subsample(5, 5)
#                 rescuer = board.create_image(700, 850, anchor = S, image = image1)


# movement_cat()

#Runs the event loop and will listen for button clicks or keypresses while blocking any code that appears after it until it is closed. 
t.mainloop()
