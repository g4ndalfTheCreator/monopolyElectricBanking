"""
This creates new window that displays who has won.
Monopoly electric banking version 0.01

Creator: Samuli Tolvanen
"""

from tkinter import *

class Display_winner:

    def __init__(self, winner_txt):

        # Starup and defining window
        self.__congrats_window = Tk()

        # Creating label text
        self.__removal_txt = Label(self.__congrats_window, text=winner_txt, relief=RAISED,
                                   height=2, width=40, background="gold")
        # Crearing Ok buttom
        self.__ok = Button(self.__congrats_window, text="Ok, thanks!",width=40, background="cyan",
                           command=self.end_window)
        # Placements:
        self.__removal_txt.pack()
        self.__ok.pack()

        self.__congrats_window.mainloop()

    def end_window(self):
        self.__congrats_window.destroy()
