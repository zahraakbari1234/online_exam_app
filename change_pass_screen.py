from tkinter import *
from const import *
from gui_task import *
import os


def change_password_screen(self):
    self = self

    self.change_password_win = Toplevel(self.root)
    self.change_password_win.config(bg="#ffffff")
    self.change_password_win.geometry("480x300+%d+%d" % (self.root.winfo_screenwidth() /
                                                         2-240, self.root.winfo_screenheight()/2-150))
    self.change_password_win.resizable(False, False)
    self.change_password_win.overrideredirect(True)
    self.change_password_win.title("Change Password")

    self.change_password_canvas = Canvas(
        self.change_password_win, width=480, height=300)
    self.change_password_canvas.pack()
    ##############
    self.change_password_frame = PhotoImage(
        file=AppConstants.change_pass_backgnd_add)
    self.change_password_canvas.create_image(-2, -2,
                                             image=self.change_password_frame,
                                             anchor=NW)

##############
    self.password_entry = Entry(self.change_password_canvas, width=15, font=("b_nazanin", 18),
                                bg=AppConstants.cream)
    self.password_entry.pack()
    self.password_entry.place(x=200, y=70)
    self.password_entry.config(show='*')
##############
    self.new_password_entry = Entry(self.change_password_canvas, width=15, font=("b_nazanin", 18),
                                    bg=AppConstants.cream)
    self.new_password_entry.pack()
    self.new_password_entry.place(x=200, y=130)
    self.new_password_entry.config(show='*')
##############
    ##############
    self.verify_new_password_entry = Entry(self.change_password_canvas, width=15, font=("b_nazanin", 18),
                                           bg=AppConstants.cream)
    self.verify_new_password_entry.pack()
    self.verify_new_password_entry.place(x=200, y=190)
    self.verify_new_password_entry.config(show='*')
##############

    self.change_password_enter_button_img = PhotoImage(
        file=AppConstants.enter_button_add)
    self.change_password_enter_button = self.change_password_canvas.create_image(8, 80,
                                                                                 image=self.change_password_enter_button_img,
                                                                                 anchor=NW)

    self.change_password_canvas.tag_bind(
        self.change_password_enter_button, '<Button-1>', self.change_password_enter_func)

################
    self.change_password_cancel_button_img = PhotoImage(
        file=AppConstants.cancel_button_add)
    self.change_password_cancel_button = self.change_password_canvas.create_image(8, 135,
                                                                                  image=self.change_password_cancel_button_img,
                                                                                  anchor=NW)

    self.change_password_canvas.tag_bind(
        self.change_password_cancel_button, '<Button-1>', self.change_password_cancel_func)

################

    self.change_password_exit_img = PhotoImage(
        file=AppConstants.exit_small_button_add)
    self.change_password_exit = self.change_password_canvas.create_image(8, 190,
                                                                         image=self.change_password_exit_img,
                                                                         anchor=NW)

    self.change_password_canvas.tag_bind(
        self.change_password_exit, '<Button-1>', lambda void: os._exit(1))

################
    self.change_password_win.withdraw()
