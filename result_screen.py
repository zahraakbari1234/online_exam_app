from tkinter import*
from const import*
import os


class result_screen:
    
    def __init__(self):

        self.root = Tk()
        self.root.config(bg= "#ffffff")
        self.root.geometry("480x300+%d+%d" %(self.root.winfo_screenwidth()/2-240
                                             ,self.root.winfo_screenheight()/2-150))
        self.root.resizable(False,False)
        self.root.overrideredirect(True)
        self.root.title("Login")

        self.canvas = Canvas(self.root,width=480,height=300)
        self.canvas.pack()

        
##############
        self.frame = PhotoImage(file = AppConstants.reult_backgnd_add )
        self.canvas.create_image(-2 , -2 ,
                                  image=self.frame,
                                  anchor = NW )
 
##############
        self.exit_img = PhotoImage(file = AppConstants.exit_small_button_add )
        self.exit= self.canvas.create_image(200 , 210 ,
                                  image=self.exit_img,
                                  anchor = NW )

        self.canvas.tag_bind(self.exit, '<Button-1>',  lambda void : os._exit(1) )
        
################

 
        self.root.mainloop()




        
