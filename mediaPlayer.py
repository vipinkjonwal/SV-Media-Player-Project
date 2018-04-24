from tkinter import *
import pygame
from doublyLinkedList import *

dlist = Doublylinkedlist()
root = Tk()
pygame.mixer.init()

def playMusic():
    #play.destroy()
    pygame.mixer.music.load(dlist.head.data)
    pygame.mixer.music.play()


def stopMusic():
    pygame.mixer.music.stop()


def pauseMusic():
    pygame.mixer.music.pause()


def unpauseMusic():
    pygame.mixer.music.unpause()


def prevMusic():
    pygame.mixer.music.load(dlist.getPrev())
    pygame.mixer.music.play()


def nextMusic():
    pygame.mixer.music.load(dlist.getNext())
    pygame.mixer.music.play()


def loadMediaPlayer(dirPath):
    listFiles = dlist.getFileName(dirPath)
    for i in listFiles:
        dlist.insert(i)


def mediaPlayerCanvas():
    root.title("SV Music")
    canvas = Canvas(root,width = 300,height = 300)
    canvas.pack()
    canvas.configure(background='black')
    root.configure(background='black')

    stopPhoto = (PhotoImage(file="Images/stop.png"))
    playPhoto = PhotoImage(file="Images/play.png")
    pausePhoto = PhotoImage(file="Images/pause.png")
    playAgainPhoto = PhotoImage(file="Images/playagain.png")
    nextPhoto = PhotoImage(file="Images/next.png")
    prevPhoto = PhotoImage(file="Images/prev.png")

    play = Button(root,image = playPhoto,command = playMusic)
    stop = Button(root,image = stopPhoto,command = stopMusic)
    pause = Button(root,image = pausePhoto,command = pauseMusic)
    unPause = Button(root,image = playAgainPhoto,command = unpauseMusic)
    next = Button(root,image = nextPhoto,command = nextMusic)
    prev = Button(root,image = prevPhoto,command = prevMusic)

    prev.pack(side = LEFT)
    play.pack(side = LEFT)
    pause.pack(side = LEFT)
    stop.pack(side = LEFT)
    next.pack(side = LEFT)
    unPause.pack(side = RIGHT)

if __name__ == '__main__':
    loadMediaPlayer("C:\\Users\\vkjof\Documents\pythonCodesGitHub")
    mediaPlayerCanvas()
    root.mainloop()

#button_frame.columnconfigure(0,weight=1)
#button_frame.columnconfigure(1,weight=1)
