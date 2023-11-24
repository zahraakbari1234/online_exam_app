from tkinter import *
from const import *
import os


def message_screen(self):

    self = self

    self.message_win = Toplevel(self.root)
    self.message_win.config(bg="#ffffff")
    self.message_win.geometry("229x94+%d+%d" % (self.message_win.winfo_screenwidth() /
                              2-114, self.message_win.winfo_screenheight()/2-47))
    self.message_win.resizable(False, False)
    self.message_win.overrideredirect(True)
    self.message_win.title("Profile")

    self.message_canvas = Canvas(self.message_win, width=480, height=300)
    self.message_canvas.pack()

    ##############
    self.message_frame = PhotoImage(file=AppConstants.chng_ramz_add)
    self.message_canvas.create_image(0, 0,
                                     image=self.message_frame,
                                     anchor=NW)

    self.message_win.withdraw()
