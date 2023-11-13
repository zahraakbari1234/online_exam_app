from tkinter import*
from const import*
import os
import time

 

class questions_screen:

    number_of_q = 10
    result = 0
    Q=1
    result_list=[0 for i in range (number_of_q+1) ]
    
    def __init__( self ):
        
        self.root = Tk()
        self.root.config(bg= "#ffffff")
        self.root.geometry("1000x670+%d+%d" %(self.root.winfo_screenwidth()/2-500
                                             ,self.root.winfo_screenheight()/2-335))
        self.root.resizable(False,False)
        self.root.overrideredirect(True)
        self.root.title("Q")

        self.canvas = Canvas(self.root,width=1000,height=670)
        self.canvas.pack()

        
##############
        self.frame = PhotoImage(file = AppConstants.questions_backgnd_add )
        self.canvas.create_image(-2 , -2 ,
                                  image=self.frame,
                                  anchor = NW )
##############
        self.time_date = Label(self.canvas ,
                          text = time.asctime()[11:19]+"\n"+time.asctime()[4:9]+" "+time.asctime()[20:24] , bg = "#ffffff" ,
                          fg = "#000000", font = ("Bnazanin" , 15 , "bold") )
        self.time_date.pack()
        self.time_date.place( x = 35 , y = 590 )
##############
        try:
            self.question_add = ("assets/Q_%02d.png"%self.Q)
            self.question_img = PhotoImage(file = self.question_add )
            self.canvas.create_image(900 , 80 ,
                                  image=self.question_img,
                                  anchor = NE )
        except:
            print("no  q here")

##############
        try:
            self.photo_add = ("assets/QP_%02d.png"%self.Q)
            self.photo_img = PhotoImage(file = self.photo_add )
            self.canvas.create_image(250 , 350 ,
                                          image=self.photo_img,
                                          anchor = NW )
        except:
  
            self.photo_img = PhotoImage(file = AppConstants.no_image_add)
            self.canvas.create_image(250 , 350 ,
                                          image=self.photo_img,
                                          anchor = NW )
        

##############
        self.result = IntVar()
        self.alef = Radiobutton(self.canvas ,variable=self.result,value=1,
                                bg="#ffffff" ,activebackground = "#ffffff")
        self.alef.place(x=910 , y = 188)

        self.be = Radiobutton(self.canvas ,variable=self.result,value=2,
                              bg="#ffffff" ,activebackground = "#ffffff")
        self.be.place(x=910 , y = 220)

        self.jim = Radiobutton(self.canvas ,variable=self.result,value=3,
                               bg="#ffffff" ,activebackground = "#ffffff")
        self.jim.place(x=910 , y = 260)

        self.dol = Radiobutton(self.canvas ,variable=self.result,value=4,
                               bg="#ffffff" ,activebackground = "#ffffff")
        self.dol.place(x=910 , y = 300)

  ##############
        self.next_q_button_img = PhotoImage(file = AppConstants.next_q_button_add )
        self.next_q_button = self.canvas.create_image(23 , 210 ,
                                  image=self.next_q_button_img,
                                  anchor = NW )

        self.canvas.tag_bind(self.next_q_button, '<Button-1>', self.next_q_func )
        
################
        self.prev_q_button_img = PhotoImage(file = AppConstants.prev_q_button_add )
        self.prev_q_button = self.canvas.create_image(23 , 315 ,
                                  image=self.prev_q_button_img,
                                  anchor = NW )

        self.canvas.tag_bind(self.prev_q_button, '<Button-1>', self.prev_q_func )
        
################
  
        self.exit_img = PhotoImage(file = AppConstants.exit_large_button_add )
        self.exit= self.canvas.create_image(23 , 420 ,
                                  image=self.exit_img,
                                  anchor = NW )

        self.canvas.tag_bind(self.exit, '<Button-1>',  lambda void : os._exit(1) )
        
################
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        self.time_date.config(
        text = time.asctime()[11:19]+"\n"+time.asctime()[4:9]+" "+time.asctime()[20:24] , bg = "#ffffff" ,)
        self.root.update()
        self.root.after(10,self.update_clock)

    def next_q_func(self,event=None):
        
        if(self.Q < self.number_of_q ):
            print( self.result.get() )
            self.result_list[self.Q]= self.result.get() 
            print(self.result_list)
            self.Q +=1
            try:
                self.question_add = ("assets/Q_%02d.png"%self.Q)
                self.question_img = PhotoImage(file = self.question_add )
                self.canvas.create_image(900 , 80 ,
                                  image=self.question_img,
                                  anchor = NE )
            except:
                print("no q ")

            try:
                self.photo_add = ("assets/QP_%02d.png"%self.Q)
                self.photo_img = PhotoImage(file = self.photo_add )
                self.canvas.create_image(250 , 350 ,
                                          image=self.photo_img,
                                          anchor = NW )
            except:
  
                self.photo_img = PhotoImage(file = AppConstants.no_image_add)
                self.canvas.create_image(250 , 350 ,
                                          image=self.photo_img,
                                          anchor = NW )
                
            if( self.Q  == self.number_of_q ):
                self.finish_button_img = PhotoImage(file = AppConstants.finish_button_add )
                self.finish_button = self.canvas.create_image(23 , 210 ,
                                  image=self.finish_button_img,
                                  anchor = NW )
                self.canvas.tag_bind(self.finish_button, '<Button-1>', self.finish_func )
                
            
            
    def finish_func(self,event=None):
        print( self.result.get() )
        self.result_list[self.Q]= self.result.get() 
        print(self.result_list)
            

        
 
        
    def prev_q_func(self,event=None):
        
        if( self.Q == self.number_of_q ):
            self.next_q_button_img = PhotoImage(file = AppConstants.next_q_button_add )
            self.next_q_button = self.canvas.create_image(23 , 210 ,
                                  image=self.next_q_button_img,
                                  anchor = NW )

            self.canvas.tag_bind(self.next_q_button, '<Button-1>', self.next_q_func )

        
        if(self.Q > 1):
            print( self.result.get() )
            self.result_list[self.Q]= self.result.get() 
            print(self.result_list)
            self.Q -=1
            try:
                self.question_add = ("assets/Q_%02d.png"%self.Q)
                self.question_img = PhotoImage(file = self.question_add )
                self.canvas.create_image(900 , 80 ,
                                  image=self.question_img,
                                  anchor = NE )
            except:
                print("no q ")

            try:
                self.photo_add = ("assets/QP_%02d.png"%self.Q)
                self.photo_img = PhotoImage(file = self.photo_add )
                self.canvas.create_image(250 , 350 ,
                                          image=self.photo_img,
                                          anchor = NW )
            except:
  
                self.photo_img = PhotoImage(file = AppConstants.no_image_add)
                self.canvas.create_image(250 , 350 ,
                                          image=self.photo_img,
                                          anchor = NW )

                

         
       
            
   



    

        
