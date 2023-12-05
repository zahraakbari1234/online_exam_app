from tkinter import *
from const import *
import os
import time


def questions_screen(self):

    self = self

    self.questions_screen_win = Toplevel(self.root)
    self.questions_screen_win.config(bg="#ffffff")
    self.questions_screen_win.geometry("1000x670+%d+%d" % (self.root.winfo_screenwidth() /
                                                           2-500, self.root.winfo_screenheight()/2-335))
    self.questions_screen_win.resizable(False, False)
    self.questions_screen_win.overrideredirect(True)
    self.questions_screen_win.title("Test")

    self.questions_screen_canvas = Canvas(
        self.questions_screen_win, width=1000, height=670)
    self.questions_screen_canvas.pack()
##############
    self.questions_screen_frame = PhotoImage(
        file=AppConstants.questions_backgnd_add)
    self.questions_screen_canvas.create_image(-2, -2,
                                              image=self.questions_screen_frame,
                                              anchor=NW)

##############
    self.questions_screen_time_date = Label(self.questions_screen_canvas,
                                            text=time.asctime()[11:19]+"\n"+time.asctime()[4:10]+" "+time.asctime()[20:24], bg="#ffffff",
                                            fg="#000000", font=("Bnazanin", 15, "bold"))
    self.questions_screen_time_date.pack()
    self.questions_screen_time_date.place(x=35, y=590)

##############
    try:
        self.question_add = ("assets/Q_%02d.png" % self.Q)
        self.question_img = PhotoImage(file=self.question_add)
        self.questions_screen_canvas.create_image(900, 80,
                                                  image=self.question_img,
                                                  anchor=NE)
    except:
        print("no  q here")

##############
    try:
        self.photo_add = ("assets/QP_%02d.png" % self.Q)
        self.photo_img = PhotoImage(file=self.photo_add)
        self.questions_screen_canvas.create_image(250, 350,
                                                  image=self.photo_img,
                                                  anchor=NW)
    except:

        self.photo_img = PhotoImage(file=AppConstants.no_image_add)
        self.questions_screen_canvas.create_image(250, 350,
                                                  image=self.photo_img,
                                                  anchor=NW)


##############
    self.result = IntVar()
    self.alef = Radiobutton(self.questions_screen_canvas, variable=self.result, value=1,
                            bg="#ffffff", activebackground="#ffffff")
    self.alef.place(x=910, y=180)

    self.be = Radiobutton(self.questions_screen_canvas, variable=self.result, value=2,
                          bg="#ffffff", activebackground="#ffffff")
    self.be.place(x=910, y=212)

    self.jim = Radiobutton(self.questions_screen_canvas, variable=self.result, value=3,
                           bg="#ffffff", activebackground="#ffffff")
    self.jim.place(x=910, y=248)

    self.dul = Radiobutton(self.questions_screen_canvas, variable=self.result, value=4,
                           bg="#ffffff", activebackground="#ffffff")
    self.dul.place(x=910, y=282)

##############
    self.next_q_button_img = PhotoImage(
        file=AppConstants.next_q_button_add)
    self.next_q_button = self.questions_screen_canvas.create_image(23, 210,
                                                                   image=self.next_q_button_img,
                                                                   anchor=NW)

    self.questions_screen_canvas.tag_bind(self.next_q_button,
                                          '<Button-1>', self.next_q_func)

################
    self.prev_q_button_img = PhotoImage(
        file=AppConstants.prev_q_button_add)
    self.prev_q_button = self.questions_screen_canvas.create_image(23, 315,
                                                                   image=self.prev_q_button_img,
                                                                   anchor=NW)

    self.questions_screen_canvas.tag_bind(self.prev_q_button,
                                          '<Button-1>', self.prev_q_func)

################
    self.questions_screen_exit_img = PhotoImage(
        file=AppConstants.exit_large_button_add)
    self.questions_screen_exit = self.questions_screen_canvas.create_image(23, 420,
                                                                           image=self.questions_screen_exit_img,
                                                                           anchor=NW)

    self.questions_screen_canvas.tag_bind(
        self.questions_screen_exit, '<Button-1>', lambda void: os._exit(1))


################
    self.questions_screen_win.withdraw()
    self.update_question_clock()
