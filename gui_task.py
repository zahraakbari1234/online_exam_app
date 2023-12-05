from tkinter import *
from const import *
from change_pass_screen import *
from profile_screen import *
from questions_screen import *
from login_screen import *
from key_screen import *
from result_screen import *
from pass_msg import *
import os
import bcrypt


class gui_task:

    number_of_q = 10
    result = 0
    Q = 1
    score = 0

    pass_student = "1234"
    pass_teacher = "4321"

    password_file_txt = ""
    key_file_txt = ""
    result_file_txt = ""

    key_answers = [0 for i in range(number_of_q+1)]

    result_list = [0 for i in range(number_of_q+1)]
    key_answers_list = [0 for i in range(number_of_q+1)]

    def __init__(self):

        self.read_password()
        self.read_key()

        login_screen(self=self)
        profile_screen(self=self)
        change_password_screen(self=self)
        key_screen(self=self)
        result_screen(self=self)
        questions_screen(self=self)
        message_screen(self=self)
        self.root.mainloop()

    def answers_func(self, event=None):

        self.entered_password = self.password.get()
        # Encode the entered password
        self.entered_password_encoded = self.entered_password.encode('utf-8')

        print(self.entered_password_encoded)  # test

        if bcrypt.checkpw(self.entered_password_encoded, self.hashed_pass_teacher):

            self.Q = 1
            self.root.withdraw()
            self.key_win.deiconify()
            self.key_canvas.update_idletasks()

        else:
            print("enter password again")

    def login_func(self, event=None):

        self.entered_password = self.password.get()
        # Encode the entered password
        self.entered_password_encoded = self.entered_password.encode('utf-8')

        print(self.entered_password_encoded)  # test

        if ((bcrypt.checkpw(self.entered_password_encoded, self.hashed_pass_student)) or
                (bcrypt.checkpw(self.entered_password_encoded, self.hashed_pass_teacher))):

            self.root.withdraw()
            self.profile_win.deiconify()
            self.profile_canvas.update_idletasks()

        else:
            print("cant login try again")

    def chng_pass_func(self, event=None):
        self.password_entry.delete(0, END)
        self.root.withdraw()
        self.change_password_win.deiconify()
        self.change_password_canvas.update_idletasks()

    def change_password_enter_func(self, event=None):

        self.entered_password = self.password.get()
        self.entered_new_password = self.new_password.get()
        self.entered_verify_new_password = self.verify_new_password.get()

        # Encode the entered password
        self.entered_password_encoded = self.entered_password.encode('utf-8')

        if bcrypt.checkpw(self.entered_password_encoded, self.hashed_pass_student):
            if (self.entered_new_password == self.entered_verify_new_password):
                self.pass_student = self.entered_new_password

                self.message_win.deiconify()
                self.message_canvas.update_idletasks()
                self.root.after(4000, self.hide_masg)

                self.save_password()

        elif bcrypt.checkpw(self.entered_password_encoded, self.hashed_pass_teacher):
            if (self.entered_new_password == self.entered_verify_new_password):
                self.pass_teacher = self.entered_new_password

                self.message_win.deiconify()
                self.message_canvas.update_idletasks()
                self.root.after(4000, self.hide_msg)

                self.save_password()

        else:
            print("enter correct arguments")

    def change_password_cancel_func(self, event=None):
        self.password_entry.delete(0, END)
        self.new_password_entry.delete(0, END)
        self.verify_new_password_entry.delete(0, END)
        self.root.update()
        self.root.deiconify()
        self.login_canvas.update_idletasks()
        self.change_password_win.withdraw()

    def update_profile_clock(self):
        self.profile_time_date.config(
            text=time.asctime()[11:19]+"\n"+time.asctime()[4:10]+" "+time.asctime()[20:24], bg="#ffffff",)
        self.profile_win.update()
        self.profile_win.after(10, self.update_profile_clock)

    def update_question_clock(self):
        self.questions_screen_time_date.config(
            text=time.asctime()[11:19]+"\n"+time.asctime()[4:10]+" "+time.asctime()[20:24], bg="#ffffff",)
        self.questions_screen_win.update()
        self.questions_screen_win.after(10, self.update_question_clock)

    def profile_start_func(self, event=None):
        self.name = self.name_entry.get()
        self.sirname = self.sirname_entry.get()
        self.id = self.id_entry.get()

        print(self.name)  # test
        print(self.sirname)  # test
        print(self.id)  # test

        if (self.name != "" and self.sirname != "" and self.id != ""):
            if (self.info_ok.get()):
                self.Q = 1
                self.profile_win.withdraw()
                self.questions_screen_win.deiconify()
                self.questions_screen_canvas.update_idletasks()

        else:
            print("enter arqument")

    def next_q_func(self, event=None):

        if (self.Q < self.number_of_q):
            print(self.result.get())
            self.result_list[self.Q] = self.result.get()
            self.result.set(0)
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
        self.score = self.calculate_score(
            self.result_list, self.key_answers_list)
        self.score_label.config(text=self.score)
        self.show_emoji()
        self.save_student_info()
        self.result_win.deiconify()
        self.result_canvas.update_idletasks()

    def prev_q_func(self, event=None):

        if (self.Q == self.number_of_q):
            self.next_q_button_img = PhotoImage(
                file=AppConstants.next_q_button_add)
            self.next_q_button = self.questions_screen_canvas.create_image(23, 210,
                                                                           image=self.next_q_button_img,
                                                                           anchor=NW)

            self.questions_screen_canvas.tag_bind(self.next_q_button,
                                                  '<Button-1>', self.next_q_func)

        if (self.Q > 1):
            print(self.result.get())  # test
            self.result_list[self.Q] = self.result.get()
            self.result.set(0)
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

    def key_cancel_func(self, event=None):
        self.password_entry.delete(0, END)
        self.root.update()
        self.root.deiconify()
        self.login_canvas.update_idletasks()
        self.key_win.withdraw()

    def key_enter_func(self, event=None):
        self.password_entry.delete(0, END)
        for i in range(self.number_of_q + 1):
            self.key_answers_list[i] = self.key_answers[i].get()
            self.save_key()
            print(self.key_answers[i].get())  # test

        print(self.key_answers_list)  # test

        self.root.update()
        self.root.deiconify()
        self.login_canvas.update_idletasks()
        self.key_win.withdraw()

    def calculate_score(self, result_list, key_answers_list):

        self.result_list = result_list
        self.key_answers_list = key_answers_list
        score = 0

        for i in range(1, self.number_of_q+1):
            if (self.result_list[i] == self.key_answers_list[i]):
                score += 1

        print(score)
        return score

    def show_emoji(self):

        if (self.score > self.number_of_q - 3):
            self.emoji_img = PhotoImage(file=AppConstants.excellent_emoji_add)
            self.result_emoji = self.result_canvas.create_image(130, 110,
                                                                image=self.emoji_img,
                                                                anchor=NW)

        elif (self.score > self.number_of_q - 6):
            self.emoji_img = PhotoImage(file=AppConstants.good_emoji_add)
            self.result_emoji = self.result_canvas.create_image(130, 110,
                                                                image=self.emoji_img,
                                                                anchor=NW)

        elif (self.score > self.number_of_q - 8):
            self.emoji_img = PhotoImage(file=AppConstants.bad_emoji_add)
            self.result_emoji = self.result_canvas.create_image(130, 110,
                                                                image=self.emoji_img,
                                                                anchor=NW)

        elif (self.score < self.number_of_q - 8):
            self.emoji_img = PhotoImage(file=AppConstants.oops_emoji_add)
            self.result_emoji = self.result_canvas.create_image(130, 110,
                                                                image=self.emoji_img,
                                                                anchor=NW)

    def save_student_info(self):
        f = open(AppConstants.result_database_add, 'a')
        f.write('name=%s sirname=%s id=%s score=%d time=%s !\n\n' %
                (self.name, self.sirname, self.id, self.score, time.asctime()[11:19]))
        f.close()

    def save_password(self):

        # Encode the stored password
        self.pass_student_encoded = self.pass_student.encode('utf-8')
        self.pass_teacher_encoded = self.pass_teacher.encode('utf-8')
        # Hash the password
        self.hashed_pass_student = bcrypt.hashpw(
            self.pass_student_encoded, bcrypt.gensalt())
        self.hashed_pass_teacher = bcrypt.hashpw(
            self.pass_teacher_encoded, bcrypt.gensalt())

        f = open(AppConstants.password_database_add, 'w')
        f.write('student_pass=%s\nteacher_pass=%s' %
                (self.hashed_pass_student, self.hashed_pass_teacher))
        f.close()

    def save_key(self):
        f = open(AppConstants.key_database_add, 'w')
        for i in range(1, self.number_of_q + 1):
            f.write('Q%02d=%d\n' %
                    (i, self.key_answers[i].get()))
        f.close()

    def read_password(self):
        try:

            f = open(AppConstants.password_database_add, 'r')
            self.password_file_txt = f.read()
            f.close()

            self.pass_student_index = self.password_file_txt.find(
                'student_pass=')
            self.pass_teacher_index = self.password_file_txt.find(
                'teacher_pass=')

            self.hashed_pass_student = self.password_file_txt[self.pass_student_index + 15:
                                                              self.pass_teacher_index-2]

            self.hashed_pass_teacher = self.password_file_txt[
                self.pass_teacher_index + 15: self.pass_teacher_index + 15 + 60]

            # Encode the stored password
            self.hashed_pass_student = self.hashed_pass_student.encode('utf-8')
            self.hashed_pass_teacher = self.hashed_pass_teacher.encode('utf-8')

            print(self.password_file_txt)  # test
            print(self.hashed_pass_student)  # test
            print(self.hashed_pass_teacher)  # test

        except:
            self.save_password()

    def read_key(self):
        try:

            f = open(AppConstants.result_database_add, 'r')
            self.key_file_txt = f.read()
            f.close()

            for i in range(1, self.number_of_q+1):
                self.Q_index = self.key_file_txt.find('Q%02d=' % i)
                self.key_answers_list[i] = int(
                    self.key_file_txt[self.Q_index + 4])

            print(self.key_file_txt)  # test
            print(self.key_answers_list)  # test

        except:
            pass

    def hide_masg(self):

        self.password_entry.delete(0, END)
        self.new_password_entry.delete(0, END)
        self.verify_new_password_entry.delete(0, END)

        self.message_win.withdraw()
        self.root.update()
        self.root.deiconify()
        self.login_canvas.update_idletasks()
        self.change_password_win.withdraw()
