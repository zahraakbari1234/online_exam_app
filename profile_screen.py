from tkinter import*
from const import*
from questions_screen import*
import os
import time


class profile_screen:
   
    def __init__(self ):
        self.root = Tk()
        self.root.config(bg= "#ffffff")
        self.root.geometry("480x300+%d+%d" %(self.root.winfo_screenwidth()/2-240
                                             ,self.root.winfo_screenheight()/2-150))
        self.root.resizable(False,False)
        self.root.overrideredirect(True)
        self.root.title("Profile")

        self.canvas = Canvas(self.root,width=480,height=300)
        self.canvas.pack()
#############
        self.time_date = Label(self.canvas ,
                          text = time.asctime()[11:19]+"\n"+time.asctime()[4:9]+" "+time.asctime()[20:24] , bg = "#ffffff" ,
                          fg = "#000000", font = ("Bnazanin" , 10 , "bold") )
        self.time_date.pack()
        self.time_date.place( x = 8 , y = 250 )
 
        
##############
        self.frame = PhotoImage(file = AppConstants.profile_backgnd_add )
        self.canvas.create_image(-2 , -2 ,
                                  image=self.frame,
                                  anchor = NW )
      
##############
        self.name_entry=Entry(self.canvas,width=15,font = ("b_nazanin" , 18 ),
                                  bg = AppConstants.cream)
        self.name_entry.pack()
        self.name_entry.place(x=210 , y=50)
        
##############
        ##############
        self.sirname_entry=Entry(self.canvas,width=15,font = ("b_nazanin" , 18 ),
                                  bg = AppConstants.cream)
        self.sirname_entry.pack()
        self.sirname_entry.place(x=210 , y=120)
##############
        ##############
        self.id_entry=Entry(self.canvas,width=15,font = ("b_nazanin" , 18 ),
                                  bg = AppConstants.cream)
        self.id_entry.pack()
        self.id_entry.place(x=210 , y=190)
##############
        self.ok = BooleanVar()
        self.check1= Checkbutton(self.canvas , bg="#ffffff" ,activebackground = "#ffffff")
        self.check1.pack()
        self.check1.place(x=420 , y=235)
        self.check1.config(variable = self.ok , onvalue = 1 , offvalue = 0 )
        self.ok.set(1)
  ##############
        self.start_button_img = PhotoImage(file = AppConstants.start_button_add )
        self.start_button = self.canvas.create_image(8 , 105 ,
                                  image=self.start_button_img,
                                  anchor = NW )

        self.canvas.tag_bind(self.start_button, '<Button-1>', self.start_func )
        
################
  
        self.exit_img = PhotoImage(file = AppConstants.exit_small_button_add )
        self.exit= self.canvas.create_image(8 , 160 ,
                                  image=self.exit_img,
                                  anchor = NW )

        self.canvas.tag_bind(self.exit, '<Button-1>', lambda void : os._exit(1) )
        
################

        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        self.time_date.config(
        text = time.asctime()[11:19]+"\n"+time.asctime()[4:9]+" "+time.asctime()[20:24] , bg = "#ffffff" ,)
        self.root.update()
        self.root.after(10,self.update_clock)
        
    def start_func(self,event=None):
        self.root.destroy()
        questions_screen()
 


        
