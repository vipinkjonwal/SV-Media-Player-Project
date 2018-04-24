from tkinter import *
import time
import pygame
from doublyLinkedList import *

dlist = Doublylinkedlist()
root = Tk()
pygame.mixer.init()



def playmusic():
    #play.destroy()
    pygame.mixer.music.load(dlist.head.data)
    pygame.mixer.music.play()
def stopmusic():
    pygame.mixer.music.stop()
def pausemusic():
    pygame.mixer.music.pause()
def unpausemusic():
    pygame.mixer.music.unpause()
def prevmusic():
    pygame.mixer.music.load(dlist.getPrev())
    pygame.mixer.music.play()
def nextmusic():
    pygame.mixer.music.load(dlist.getNext())
    pygame.mixer.music.play()

root.title("SV Music")
canvas = Canvas(root,width = 300,height = 300)
canvas.pack()
canvas.configure(background='black')
root.configure(background='black')

stopphoto = (PhotoImage(file="Images/stop.png"))
playphoto = PhotoImage(file="Images/play.png")
pausephoto = PhotoImage(file="Images/pause.png")
playagainphoto = PhotoImage(file="Images/playagain.png")
nextphoto = PhotoImage(file="Images/next.png")
prevphoto = PhotoImage(file="Images/prev.png")



play = Button(root,image=playphoto,command=playmusic,padx=5,pady=5)
stop = Button(root,image=stopphoto,command=stopmusic)
pause = Button(root,image = pausephoto,command=pausemusic)
unpause = Button(root,image = playagainphoto,command=unpausemusic)
next = Button(root,image = nextphoto,command=nextmusic)
prev = Button(root,image = prevphoto,command=prevmusic)

prev.pack(side = LEFT)
play.pack(side = LEFT)

pause.pack(side = LEFT)
stop.pack(side = LEFT)
next.pack(side = LEFT)
unpause.pack(side = RIGHT)

if __name__ == '__main__':

    listFiles = dlist.getFileName("C:\\Users\\vkjof\Documents\pythonCodesGitHub")
    for i in listFiles:
        dlist.insert(i)
    root.mainloop()

#button_frame.columnconfigure(0,weight=1)
#button_frame.columnconfigure(1,weight=1)
