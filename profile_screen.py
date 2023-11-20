from tkinter import *
from const import *
import os
import time


def profile_screen(self):

    self = self

    self.profile_win = Toplevel(self.root)
    self.profile_win.config(bg="#ffffff")
    self.profile_win.geometry("480x300+%d+%d" % (self.profile_win.winfo_screenwidth() /
                              2-240, self.profile_win.winfo_screenheight()/2-150))
    self.profile_win.resizable(False, False)
    self.profile_win.overrideredirect(True)
    self.profile_win.title("Profile")

    self.profile_canvas = Canvas(self.profile_win, width=480, height=300)
    self.profile_canvas.pack()
    #############
    self.profile_time_date = Label(self.profile_canvas,
                                   text=time.asctime()[11:19]+"\n"+time.asctime()[4:9]+" "+time.asctime()[20:24], bg="#ffffff",
                                   fg="#000000", font=("Bnazanin", 10, "bold"))
    self.profile_time_date.pack()
    self.profile_time_date.place(x=8, y=250)

    ##############
    self.profile_frame = PhotoImage(file=AppConstants.profile_backgnd_add)
    self.profile_canvas.create_image(-2, -2,
                                     image=self.profile_frame,
                                     anchor=NW)

    ##############
    self.name_entry = Entry(self.profile_canvas, width=15, font=("b_nazanin", 18),
                            bg=AppConstants.cream)
    self.name_entry.pack()
    self.name_entry.place(x=210, y=50)

    ##############
    ##############
    self.sirname_entry = Entry(self.profile_canvas, width=15, font=("b_nazanin", 18),
                               bg=AppConstants.cream)
    self.sirname_entry.pack()
    self.sirname_entry.place(x=210, y=120)
    ##############
    ##############
    self.id_entry = Entry(self.profile_canvas, width=15, font=("b_nazanin", 18),
                          bg=AppConstants.cream)
    self.id_entry.pack()
    self.id_entry.place(x=210, y=190)
    ##############
    self.info_ok = BooleanVar()
    self.check1 = Checkbutton(
        self.profile_canvas, bg="#ffffff", activebackground="#ffffff")
    self.check1.pack()
    self.check1.place(x=420, y=235)
    self.check1.config(variable=self.info_ok, onvalue=1, offvalue=0)
    self.info_ok.set(0)
    ##############
    self.start_button_img = PhotoImage(file=AppConstants.start_button_add)
    self.start_button = self.profile_canvas.create_image(8, 105,
                                                         image=self.start_button_img,
                                                         anchor=NW)

    self.profile_canvas.tag_bind(
        self.start_button, '<Button-1>', self.profile_start_func)

    ################

    self.profile_exit_img = PhotoImage(file=AppConstants.exit_small_button_add)
    self.profile_exit = self.profile_canvas.create_image(8, 160,
                                                         image=self.profile_exit_img,
                                                         anchor=NW)

    self.profile_canvas.tag_bind(
        self.profile_exit, '<Button-1>', lambda void: os._exit(1))

    ################
    self.profile_win.withdraw()
    self.update_profile_clock()
