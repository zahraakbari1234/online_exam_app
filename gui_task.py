from tkinter import *
from const import *
from change_pass_screen import *
from profile_screen import *
from questions_screen import *
from login_screen import *
# from key_screen import *
import os


class gui_task:

    number_of_q = 10
    result = 0
    Q = 1

    key_answers = [0 for i in range(number_of_q+1)]

    result_list = [0 for i in range(number_of_q+1)]

    def __init__(self):

        login_screen(self=self)
        profile_screen(self=self)
        change_password_screen(self=self)
        self.root.mainloop()

    def answers_func(self, event=None):
        pass
        # self.Q = 1
        # self.root.withdraw()
        # key_screen(self=self)
        # self.key_screen_win.deiconify()
        # self.key_screen_canvas.update_idletasks()

    def login_func(self, event=None):
        self.root.withdraw()
        profile_screen(self=self)
        self.profile_win.deiconify()
        self.profile_canvas.update_idletasks()

    def chng_pass_func(self, event=None):
        self.root.withdraw()
        self.change_password_win.deiconify()
        self.change_password_canvas.update_idletasks()

    def change_password_enter_func(self, event=None):
        self.root.update()
        self.root.deiconify()
        self.login_canvas.update_idletasks()
        self.change_password_win.withdraw()

    def change_password_cancel_func(self, event=None):
        self.root.update()
        self.root.deiconify()
        self.login_canvas.update_idletasks()
        self.change_password_win.withdraw()

    def update_profile_clock(self):
        self.profile_time_date.config(
            text=time.asctime()[11:19]+"\n"+time.asctime()[4:9]+" "+time.asctime()[20:24], bg="#ffffff",)
        self.profile_win.update()
        self.profile_win.after(10, self.update_profile_clock)

    def update_question_clock(self):
        self.questions_screen_time_date.config(
            text=time.asctime()[11:19]+"\n"+time.asctime()[4:9]+" "+time.asctime()[20:24], bg="#ffffff",)
        self.questions_screen_win.update()
        self.questions_screen_win.after(10, self.update_question_clock)

    def profile_start_func(self, event=None):
        self.Q = 1
        self.profile_win.withdraw()
        questions_screen(self=self)
        self.questions_screen_win.deiconify()
        self.questions_screen_canvas.update_idletasks()

    def next_q_func(self, event=None):

        if (self.Q < self.number_of_q):
            print(self.result.get())
            self.result_list[self.Q] = self.result.get()
            print(self.result_list)
            self.Q += 1
            try:
                self.question_add = ("assets/Q_%02d.png" % self.Q)
                self.question_img = PhotoImage(file=self.question_add)
                self.questions_screen_canvas.create_image(900, 80,
                                                          image=self.question_img,
                                                          anchor=NE)
            except:
                print("no q ")

            try:
                self.photo_add = ("assets/QP_%02d.png" % self.Q)
                self.photo_img = PhotoImage(file=self.photo_add)
                self.questions_screen_canvas.create_image(250, 350,
                                                          image=self.photo_img,
                                                          anchor=NW)

                self.questions_screen_canvas.update_idletasks()
            except:

                self.photo_img = PhotoImage(file=AppConstants.no_image_add)
                self.questions_screen_canvas.create_image(250, 350,
                                                          image=self.photo_img,
                                                          anchor=NW)

                self.questions_screen_canvas.update_idletasks()

            if (self.Q == self.number_of_q):
                self.finish_button_img = PhotoImage(
                    file=AppConstants.finish_button_add)
                self.finish_button = self.questions_screen_canvas.create_image(23, 210,
                                                                               image=self.finish_button_img,
                                                                               anchor=NW)
                self.questions_screen_canvas.tag_bind(self.finish_button,
                                                      '<Button-1>', self.finish_func)

    def finish_func(self, event=None):
        print(self.result.get())  # test
        self.result_list[self.Q] = self.result.get()
        print(self.result_list)  # test
        self.questions_screen_win.withdraw()
        # result_screen(self=self)

    def prev_q_func(self, event=None):

        # if (self.Q == self.number_of_q):
        #     self.next_q_button_img = PhotoImage(
        #         file=AppConstants.next_q_button_add)
        #     self.next_q_button = self.canvas.create_image(23, 210,
        #                                                   image=self.next_q_button_img,
        #                                                   anchor=NW)

        #     self.canvas.tag_bind(self.next_q_button,
        #                          '<Button-1>', self.next_q_func)

        if (self.Q > 1):
            print(self.result.get())  # test
            self.result_list[self.Q] = self.result.get()
            print(self.result_list)  # test
            self.Q -= 1
            try:
                self.question_add = ("assets/Q_%02d.png" % self.Q)
                self.question_img = PhotoImage(file=self.question_add)
                self.questions_screen_canvas.create_image(900, 80,
                                                          image=self.question_img,
                                                          anchor=NE)
            except:
                print("no q ")

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
