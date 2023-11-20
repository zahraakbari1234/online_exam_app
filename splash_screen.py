from tkinter import *
from const import *
from gui_task import *


class splash_screen:

    def __init__(self):
        self.splash = Tk()
        self.splash.config(bg="#ffffff")
        self.splash.geometry("480x300+%d+%d" % (self.splash.winfo_screenwidth() /
                             2-240, self.splash.winfo_screenheight()/2-150))
        self.splash.resizable(False, False)
        self.splash.overrideredirect(True)

        self.logo = PhotoImage(file=AppConstants.logo_add)
        self.label_splash = Label(self.splash,
                                  image=self.logo, bg="#ffffff",
                                  width=480,
                                  height=150)
        self.label_splash .pack()
        self.label_splash .place(x=0, y=50)

        self.text_ = PhotoImage(file=AppConstants.text_logo_add)
        self.label_splash = Label(self.splash,
                                  image=self.text_, bg="#ffffff",
                                  width=480,
                                  height=100)
        self.label_splash .pack()
        self.label_splash .place(x=10, y=200)

        self.splash.after(10, self.go_login_screen)

        self.splash.mainloop()

    def go_login_screen(self):

        self.splash.destroy()
        gui_task()
