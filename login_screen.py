from tkinter import*
from const import*


class login_screen:
    
    def __init__(self ):
        self.login = Tk()
        
        self.login.config(bg= AppConstants.yellow_color)
        self.login.geometry("480x300+%d+%d" %(self.login.winfo_screenwidth()/2-240
                                             ,self.login.winfo_screenheight()/2-150))
        self.login.resizable(False,False)
        self.login.title("Login")
        self.icon_img = PhotoImage(file = AppConstants.key_add )
        self.login.iconphoto(self.login,self.icon_img)
        
##############
        self.frame = PhotoImage(file = AppConstants.frame_add )
        self.label_frame = Label(self.login ,
                                  image=self.frame,bg=AppConstants.yellow_color,
                                  width = 480
                                , height = 300)
        self.label_frame .pack()
        self.label_frame .place(x=-2 , y=-2 )
##############
        self.menu = PhotoImage(file = AppConstants.menu_add )
        self.label_menu = Label(self.login ,
                                  image=self.menu,bg="#ffffff",
                                  width = 35
                                , height = 35)
        self.label_menu .pack()
        self.label_menu .place(x=400 , y=20 )
        
##############
        self.password_entry=Entry(self.login,width=15,font = ("b_nazanin" , 20 ))
        self.password_entry.pack()
        self.password_entry.place(x=180 , y=70)
        self.password_entry.config(show='*')
##############
        self.text1 = PhotoImage(file = AppConstants.textlogin_add )
        self.label_text1 = Label(self.login ,
                                  image=self.text1,bg="#ffffff",
                                  width = 100
                                , height = 20)
        self.label_text1 .pack()
        self.label_text1 .place(x=50 , y=70 )
##############
        self.exit = PhotoImage(file = AppConstants.exit_button_add )
        self.label_exit = Label(self.login ,
                                  image=self.exit,bg="#ffffff",
                                  width = 54
                                , height = 64)
        self.label_exit .pack()
        self.label_exit .place(x=70 , y=200 )
##############
        self.login_img = PhotoImage(file = AppConstants.login_button )
        self.label_login = Label(self.login ,
                                  image=self.login_img,bg="#ffffff",
                                  width = 54
                                , height = 64)
        self.label_login .pack()
        self.label_login .place(x=356 , y=200 )
##############
        self.chng_pass = PhotoImage(file = AppConstants.chng_pass_add )
        self.label_chngpass = Label(self.login ,
                                  image=self.chng_pass,bg="#ffffff",
                                  width = 144
                                , height = 50)
        self.label_chngpass .pack()
        self.label_chngpass .place(x=170 , y=207 )
############## 

        self.save_img = PhotoImage(file = AppConstants.save_pass_txt )
        self.save_label = Label(self.login ,
                                  image=self.save_img,bg="#ffffff",
                                  width = 169
                                , height = 20)
        self.save_label .pack()
        self.save_label .place(x=190 , y=150 )
##############
        self.save = BooleanVar()
        self.check1= Checkbutton(self.login , bg="#ffffff" ,activebackground = "#ffffff")
        self.check1.pack()
        self.check1.place(x=380 , y=152)
        self.check1.config(variable = self.save , onvalue = 1 , offvalue = 0 )
        self.save.set(1)
##############
        self.label_menu.bind("<Button-1>",self.menu_func)
        self.label_exit.bind("<Button-1>",self.exit_func)
        self.label_login.bind("<Button-1>",self.login_func)
        self.label_chngpass.bind("<Button-1>",self.chngpass_func)
##############
    def menu_func(self,event = None):
        pass
    def exit_func(self,event  = None):
        os._exit(1)
    def login_func(self,event = None):
        self.login.destroy()
        #self.next_screen = profile()
    def chngpass_func(self,event  = None):
        pass

        
   
        self.login.mainloop()


        
