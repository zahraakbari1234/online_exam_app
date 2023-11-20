from tkinter import *
from const import *
import os


def result_screen(self):

    self = self
    self.result_win = Toplevel(self.root)
    self.result_win.config(bg="#ffffff")
    self.result_win.geometry("480x300+%d+%d" % (self.result_win.winfo_screenwidth() /
                             2-240, self.result_win.winfo_screenheight()/2-150))
    self.result_win.resizable(False, False)
    self.result_win.overrideredirect(True)
    self.result_win.title("Login")

    self.result_canvas = Canvas(self.result_win, width=480, height=300)
    self.result_canvas.pack()


##############
    self.result_frame = PhotoImage(file=AppConstants.reult_backgnd_add)
    self.result_canvas.create_image(-2, -2,
                                    image=self.result_frame,
                                    anchor=NW)

##############
    self.result_exit_img = PhotoImage(file=AppConstants.exit_small_button_add)
    self.result_exit = self.result_canvas.create_image(200, 210,
                                                       image=self.result_exit_img,
                                                       anchor=NW)

    self.result_canvas.tag_bind(
        self.result_exit, '<Button-1>', lambda void: os._exit(1))

    self.result_win.withdraw()
