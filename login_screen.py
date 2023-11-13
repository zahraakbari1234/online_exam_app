from tkinter import*
from const import*
from change_pass_screen import *
from profile_screen import *
import os


class login_screen:
    
    def __init__(self ):
        self.login = Tk()
        self.login.config(bg= "#ffffff")
        self.login.geometry("480x300+%d+%d" %(self.login.winfo_screenwidth()/2-240
                                             ,self.login.winfo_screenheight()/2-150))
        self.login.resizable(False,False)
        self.login.overrideredirect(True)
        self.login.title("Login")

        self.login_canvas = Canvas(self.login,width=480,height=300)
        self.login_canvas.pack()

        
##############
        self.frame = PhotoImage(file = AppConstants.login_backgnd_add )
        self.login_canvas.create_image(-2 , -2 ,
                                  image=self.frame,
                                  anchor = NW )
      
##############
        self.password_entry=Entry(self.login_canvas,width=15,font = ("b_nazanin" , 18 ),
                                  bg = AppConstants.cream)
        self.password_entry.pack()
        self.password_entry.place(x=200 , y=70)
        self.password_entry.config(show='*')
##############
        self.save = BooleanVar()
        self.check1= Checkbutton(self.login_canvas , bg="#ffffff" ,activebackground = "#ffffff")
        self.check1.pack()
        self.check1.place(x=420 , y=157)
        self.check1.config(variable = self.save , onvalue = 1 , offvalue = 0 )
        self.save.set(1)
################
        self.answers_button_img = PhotoImage(file = AppConstants.answers_button_add )
        self.answer_button = self.login_canvas.create_image(8 , 60 ,
                                  image=self.answers_button_img,
                                  anchor = NW )

        self.login_canvas.tag_bind(self.answer_button, '<Button-1>', self.answers_func )
        
################
        self.login_button_img = PhotoImage(file = AppConstants.login_button_add )
        self.login_button = self.login_canvas.create_image(8 , 110 ,
                                  image=self.login_button_img,
                                  anchor = NW )

        self.login_canvas.tag_bind(self.login_button, '<Button-1>', self.login_func )
        
################
        self.chng_pass_img = PhotoImage(file = AppConstants.chng_pass_add )
        self.chng_pass= self.login_canvas.create_image(8 , 160 ,
                                  image=self.chng_pass_img,
                                  anchor = NW )

        self.login_canvas.tag_bind(self.chng_pass, '<Button-1>', self.chng_pass_func )
        
################
        self.exit_img = PhotoImage(file = AppConstants.exit_small_button_add )
        self.exit= self.login_canvas.create_image(8 , 210 ,
                                  image=self.exit_img,
                                  anchor = NW )

        self.login_canvas.tag_bind(self.exit, '<Button-1>',  lambda void : os._exit(1) )
        
################

 
        self.login.mainloop()

    def answers_func(self,event=None):
        pass
    def login_func(self,event=None):
        self.login .destroy()
        profile_screen()
    def chng_pass_func(self,event=None):
        self.login .destroy()
        change_password_screen()



        
