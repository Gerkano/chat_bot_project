
from tkinter import *
from tkinter import Tk
from PIL import Image, ImageTk, ImageSequence
import time

#This class runs a gif after a reset memory is initiated
class ResetGIF:
        
    def play_gif(self) -> None:
        gif_image = Image.open("images/erase_memory.gif")
        self.label = Label(self)
        self.label.place(x=150, y=20)
        for img in ImageSequence.Iterator(gif_image):
            img = ImageTk.PhotoImage(gif_image)
            self.label.config(image=img)
            self.update()
            time.sleep(0.02)
        self.label.pack()
 




