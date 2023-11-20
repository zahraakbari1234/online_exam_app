from tkinter import *
from const import *


class key_screen(self):
    self = self

    def __init__(self):
        self.key = Tk()
        self.key.config(bg="#ffffff")
        self.key.geometry("400x700+%d+%d" % (self.key.winfo_screenwidth() /
                          2-200, self.key.winfo_screenheight()/2-350))
        self.key.resizable(False, False)
        self.key.overrideredirect(True)
        self.key.title("Login")

        self.canvas = Canvas(self.key, width=400, height=700)
        self.canvas.pack()


##############
        self.frame = PhotoImage(file=AppConstants.key_backgnd_add)
        self.canvas.create_image(0, 0,
                                 image=self.frame,
                                 anchor=NW)

##############
        for i in range(self.number_of_q + 1):

            self.key_answers[i] = IntVar()

        self.alef1 = Radiobutton(self.canvas, variable=self.key_answers[1], value=1,
                                 bg="#ffffff", activebackground="#ffffff",
                                 fg="#116D6E")
        self.alef1.place(x=310, y=50)

        self.be1 = Radiobutton(self.canvas, variable=self.key_answers[1], value=2,
                               bg="#ffffff", activebackground="#ffffff",
                               fg="#116D6E")
        self.be1.place(x=230, y=50)

        self.jim1 = Radiobutton(self.canvas, variable=self.key_answers[1], value=3,
                                bg="#ffffff", activebackground="#ffffff",
                                fg="#116D6E")
        self.jim1.place(x=150, y=50)

        self.dol1 = Radiobutton(self.canvas, variable=self.key_answers[1], value=4,
                                bg="#ffffff", activebackground="#ffffff",
                                fg="#116D6E")
        self.dol1.place(x=70, y=50)

        ####
        self.alef2 = Radiobutton(self.canvas, variable=self.key_answers[2], value=1,
                                 bg="#ffffff", activebackground="#ffffff",
                                 fg="#116D6E")
        self.alef2.place(x=310, y=110)

        self.be2 = Radiobutton(self.canvas, variable=self.key_answers[2], value=2,
                               bg="#ffffff", activebackground="#ffffff",
                               fg="#116D6E")
        self.be2.place(x=230, y=110)

        self.jim2 = Radiobutton(self.canvas, variable=self.key_answers[2], value=3,
                                bg="#ffffff", activebackground="#ffffff",
                                fg="#116D6E")
        self.jim2.place(x=150, y=110)

        self.dol2 = Radiobutton(self.canvas, variable=self.key_answers[2], value=4,
                                bg="#ffffff", activebackground="#ffffff",
                                fg="#116D6E")
        self.dol2.place(x=70, y=110)

        ####
        self.alef3 = Radiobutton(self.canvas, variable=self.key_answers[3], value=1,
                                 bg="#ffffff", activebackground="#ffffff",
                                 fg="#116D6E")
        self.alef3.place(x=310, y=170)

        self.be3 = Radiobutton(self.canvas, variable=self.key_answers[3], value=2,
                               bg="#ffffff", activebackground="#ffffff",
                               fg="#116D6E")
        self.be3.place(x=230, y=170)

        self.jim3 = Radiobutton(self.canvas, variable=self.key_answers[3], value=3,
                                bg="#ffffff", activebackground="#ffffff",
                                fg="#116D6E")
        self.jim3.place(x=150, y=170)

        self.dol3 = Radiobutton(self.canvas, variable=self.key_answers[3], value=4,
                                bg="#ffffff", activebackground="#ffffff",
                                fg="#116D6E")
        self.dol3.place(x=70, y=170)
        ####
        self.alef4 = Radiobutton(self.canvas, variable=self.key_answers[4], value=1,
                                 bg="#ffffff", activebackground="#ffffff",
                                 fg="#116D6E")
        self.alef4.place(x=310, y=230)

        self.be4 = Radiobutton(self.canvas, variable=self.key_answers[4], value=2,
                               bg="#ffffff", activebackground="#ffffff",
                               fg="#116D6E")
        self.be4.place(x=230, y=230)

        self.jim4 = Radiobutton(self.canvas, variable=self.key_answers[4], value=3,
                                bg="#ffffff", activebackground="#ffffff",
                                fg="#116D6E")
        self.jim4.place(x=150, y=230)

        self.dol4 = Radiobutton(self.canvas, variable=self.key_answers[4], value=4,
                                bg="#ffffff", activebackground="#ffffff",
                                fg="#116D6E")
        self.dol4.place(x=70, y=230)
        ####
        self.alef5 = Radiobutton(self.canvas, variable=self.key_answers[5], value=1,
                                 bg="#ffffff", activebackground="#ffffff",
                                 fg="#116D6E")
        self.alef5.place(x=310, y=290)

        self.be5 = Radiobutton(self.canvas, variable=self.key_answers[5], value=2,
                               bg="#ffffff", activebackground="#ffffff",
                               fg="#116D6E")
        self.be5.place(x=230, y=290)

        self.jim5 = Radiobutton(self.canvas, variable=self.key_answers[5], value=3,
                                bg="#ffffff", activebackground="#ffffff",
                                fg="#116D6E")
        self.jim5.place(x=150, y=290)

        self.dol5 = Radiobutton(self.canvas, variable=self.key_answers[5], value=4,
                                bg="#ffffff", activebackground="#ffffff",
                                fg="#116D6E")
        self.dol5.place(x=70, y=290)
       ######
        self.alef6 = Radiobutton(self.canvas, variable=self.key_answers[6], value=1,
                                 bg="#ffffff", activebackground="#ffffff",
                                 fg="#116D6E")
        self.alef6.place(x=310, y=350)

        self.be6 = Radiobutton(self.canvas, variable=self.key_answers[6], value=2,
                               bg="#ffffff", activebackground="#ffffff",
                               fg="#116D6E")
        self.be6.place(x=230, y=350)

        self.jim6 = Radiobutton(self.canvas, variable=self.key_answers[6], value=3,
                                bg="#ffffff", activebackground="#ffffff",
                                fg="#116D6E")
        self.jim6.place(x=150, y=350)

        self.dol6 = Radiobutton(self.canvas, variable=self.key_answers[6], value=4,
                                bg="#ffffff", activebackground="#ffffff",
                                fg="#116D6E")
        self.dol6.place(x=70, y=350)

        ####
        self.alef7 = Radiobutton(self.canvas, variable=self.key_answers[7], value=1,
                                 bg="#ffffff", activebackground="#ffffff",
                                 fg="#116D6E")
        self.alef7.place(x=310, y=410)

        self.be7 = Radiobutton(self.canvas, variable=self.key_answers[7], value=2,
                               bg="#ffffff", activebackground="#ffffff",
                               fg="#116D6E")
        self.be7.place(x=230, y=410)

        self.jim7 = Radiobutton(self.canvas, variable=self.key_answers[7], value=3,
                                bg="#ffffff", activebackground="#ffffff",
                                fg="#116D6E")
        self.jim7.place(x=150, y=410)

        self.dol7 = Radiobutton(self.canvas, variable=self.key_answers[7], value=4,
                                bg="#ffffff", activebackground="#ffffff",
                                fg="#116D6E")
        self.dol7.place(x=70, y=410)

        ####
        self.alef8 = Radiobutton(self.canvas, variable=self.key_answers[8], value=1,
                                 bg="#ffffff", activebackground="#ffffff",
                                 fg="#116D6E")
        self.alef8.place(x=310, y=470)

        self.be8 = Radiobutton(self.canvas, variable=self.key_answers[8], value=2,
                               bg="#ffffff", activebackground="#ffffff",
                               fg="#116D6E")
        self.be8.place(x=230, y=470)

        self.jim8 = Radiobutton(self.canvas, variable=self.key_answers[8], value=3,
                                bg="#ffffff", activebackground="#ffffff",
                                fg="#116D6E")
        self.jim8.place(x=150, y=470)

        self.dol8 = Radiobutton(self.canvas, variable=self.key_answers[8], value=4,
                                bg="#ffffff", activebackground="#ffffff",
                                fg="#116D6E")
        self.dol8.place(x=70, y=470)
        ####
        self.alef9 = Radiobutton(self.canvas, variable=self.key_answers[9], value=1,
                                 bg="#ffffff", activebackground="#ffffff",
                                 fg="#116D6E")
        self.alef9.place(x=310, y=530)

        self.be9 = Radiobutton(self.canvas, variable=self.key_answers[9], value=2,
                               bg="#ffffff", activebackground="#ffffff",
                               fg="#116D6E")
        self.be9.place(x=230, y=530)

        self.jim9 = Radiobutton(self.canvas, variable=self.key_answers[9], value=3,
                                bg="#ffffff", activebackground="#ffffff",
                                fg="#116D6E")
        self.jim9.place(x=150, y=530)

        self.dol9 = Radiobutton(self.canvas, variable=self.key_answers[9], value=4,
                                bg="#ffffff", activebackground="#ffffff",
                                fg="#116D6E")
        self.dol9.place(x=70, y=530)
        ####
        self.alef10 = Radiobutton(self.canvas, variable=self.key_answers[10], value=1,
                                  bg="#ffffff", activebackground="#ffffff",
                                  fg="#116D6E")
        self.alef10.place(x=310, y=590)

        self.be10 = Radiobutton(self.canvas, variable=self.key_answers[10], value=2,
                                bg="#ffffff", activebackground="#ffffff",
                                fg="#116D6E")
        self.be10.place(x=230, y=590)

        self.jim10 = Radiobutton(self.canvas, variable=self.key_answers[10], value=3,
                                 bg="#ffffff", activebackground="#ffffff",
                                 fg="#116D6E")
        self.jim10.place(x=150, y=590)

        self.dol10 = Radiobutton(self.canvas, variable=self.key_answers[10], value=4,
                                 bg="#ffffff", activebackground="#ffffff",
                                 fg="#116D6E")
        self.dol10.place(x=70, y=590)
################
        self.enter_button_img = PhotoImage(file=AppConstants.enter_button_add)
        self.enter_button = self.canvas.create_image(210, 650,
                                                     image=self.enter_button_img,
                                                     anchor=NW)

        self.canvas.tag_bind(self.enter_button, '<Button-1>', self.enter_func)

################
        self.cancel_button_img = PhotoImage(
            file=AppConstants.cancel_button_add)
        self.cancel_button = self.canvas.create_image(110, 650,
                                                      image=self.cancel_button_img,
                                                      anchor=NW)

        self.canvas.tag_bind(self.cancel_button,
                             '<Button-1>', self.cancel_func)

################

        self.key.mainloop()

    def cancel_func(self, event=None):
        pass
        # self.key.destroy()
        # login_screen()

    def enter_func(self, event=None):
        for i in range(self.number_of_q + 1):
            print(self.key_answers[i].get())

        # self.key.destroy()
        # login_screen().re-instantiate()
