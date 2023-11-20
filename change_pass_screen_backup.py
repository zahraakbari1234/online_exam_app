from tkinter import*
from const import*
from login_screen import*
import os


def change_password_screen(void):
    
    self.change_password_win=TopLevel(self.root)
    self.change_password_win = window
    window.config(bg= "#ffffff")
    window.geometry("480x300+%d+%d" %(self.root.winfo_screenwidth()/2-240
                                             ,self.root.winfo_screenheight()/2-150))
    window.resizable(False,False)
    window.overrideredirect(True)
    window.title("Change Password")

    self.canvas = Canvas(window,width=480,height=300)
    self.canvas.pack()
    ##############
    self.frame = PhotoImage(file = AppConstants.change_pass_backgnd_add )
    self.canvas.create_image(-2 , -2 ,
                                  image=self.frame,
                                  anchor = NW )
      
##############
    self.password_entry=Entry(self.canvas,width=15,font = ("b_nazanin" , 18 ),
                                  bg = AppConstants.cream)
    self.password_entry.pack()
    self.password_entry.place(x=200 , y=70)
    self.password_entry.config(show='*')
##############
        ##############
    self.new_password_entry=Entry(self.canvas,width=15,font = ("b_nazanin" , 18 ),
                                  bg = AppConstants.cream)
    self.new_password_entry.pack()
    self.new_password_entry.place(x=200 , y=130)
    self.new_password_entry.config(show='*')
##############
        ##############
    self.verify_new_password_entry=Entry(self.canvas,width=15,font = ("b_nazanin" , 18 ),
                                  bg = AppConstants.cream)
    self.verify_new_password_entry.pack()
    self.verify_new_password_entry.place(x=200 , y=190)
    self.verify_new_password_entry.config(show='*')
##############
 
    self.enter_button_img = PhotoImage(file = AppConstants.enter_button_add )
    self.enter_button = self.canvas.create_image(8 , 80 ,
                                  image=self.enter_button_img,
                                  anchor = NW )

    self.canvas.tag_bind(self.enter_button, '<Button-1>', self.enter_func )
        
################
    self.cancel_button_img = PhotoImage(file = AppConstants.cancel_button_add )
    self.cancel_button = self.canvas.create_image(8 , 135 ,
                                  image=self.cancel_button_img,
                                  anchor = NW )

    self.canvas.tag_bind(self.cancel_button, '<Button-1>', self.cancel_func )
        
################
  
    self.exit_img = PhotoImage(file = AppConstants.exit_small_button_add )
    self.exit= self.canvas.create_image(8 , 190 ,
                                  image=self.exit_img,
                                  anchor = NW )

    self.canvas.tag_bind(self.exit, '<Button-1>',  lambda void : os._exit(1) )
        
################

class change_password_screen:
    
    def __init__(self ):
        self.root = Tk()
        self.root.config(bg= "#ffffff")
        self.root.geometry("480x300+%d+%d" %(self.root.winfo_screenwidth()/2-240
                                             ,self.root.winfo_screenheight()/2-150))
        self.root.resizable(False,False)
        self.root.overrideredirect(True)
        self.root.title("Change Password")

        self.canvas = Canvas(self.root,width=480,height=300)
        self.canvas.pack()

        
##############
        self.frame = PhotoImage(file = AppConstants.change_pass_backgnd_add )
        self.canvas.create_image(-2 , -2 ,
                                  image=self.frame,
                                  anchor = NW )
      
##############
        self.password_entry=Entry(self.canvas,width=15,font = ("b_nazanin" , 18 ),
                                  bg = AppConstants.cream)
        self.password_entry.pack()
        self.password_entry.place(x=200 , y=70)
        self.password_entry.config(show='*')
##############
        ##############
        self.new_password_entry=Entry(self.canvas,width=15,font = ("b_nazanin" , 18 ),
                                  bg = AppConstants.cream)
        self.new_password_entry.pack()
        self.new_password_entry.place(x=200 , y=130)
        self.new_password_entry.config(show='*')
##############
        ##############
        self.verify_new_password_entry=Entry(self.canvas,width=15,font = ("b_nazanin" , 18 ),
                                  bg = AppConstants.cream)
        self.verify_new_password_entry.pack()
        self.verify_new_password_entry.place(x=200 , y=190)
        self.verify_new_password_entry.config(show='*')
##############
 
        self.enter_button_img = PhotoImage(file = AppConstants.enter_button_add )
        self.enter_button = self.canvas.create_image(8 , 80 ,
                                  image=self.enter_button_img,
                                  anchor = NW )

        self.canvas.tag_bind(self.enter_button, '<Button-1>', self.enter_func )
        
################
        self.cancel_button_img = PhotoImage(file = AppConstants.cancel_button_add )
        self.cancel_button = self.canvas.create_image(8 , 135 ,
                                  image=self.cancel_button_img,
                                  anchor = NW )

        self.canvas.tag_bind(self.cancel_button, '<Button-1>', self.cancel_func )
        
################
  
        self.exit_img = PhotoImage(file = AppConstants.exit_small_button_add )
        self.exit= self.canvas.create_image(8 , 190 ,
                                  image=self.exit_img,
                                  anchor = NW )

        self.canvas.tag_bind(self.exit, '<Button-1>',  lambda void : os._exit(1) )
        
################

 
        self.root.mainloop()

    def enter_func(self,event=None):
        pass
    def cancel_func(self,event=None):
       
        self.root.iconify()
        login_screen()
  


        
