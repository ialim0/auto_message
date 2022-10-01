import email
from logging import root
from tkinter import *
from tkinter import messagebox,filedialog
import  os
from turtle import title
import pandas as pd



class  Mail:
    def __init__(self,root):
        self.root = root
        
        
        self.root.title("Auto message")
        self.root.geometry("1500x780+250+250")
        self.root.config(bg="teal")
        self.root.focus_force()
        
        
        #Title 
        title=Label(self.root,text="Send Mail",font=("sans-serif",80),bg="white")
        title.pack(side=TOP,fill=X)
        m_frame=LabelFrame(self.root,text="Entrer votre Mail",font=("times new roman",15,"bold"),bg="black",fg="white")
        m_frame.place(x=0,y=120,width=1500,height=90)
        btn_conect=Button(m_frame,text="Your mail",font=("times new roman",20,"bold"),command=self.fen_conect,bg="blue",cursor="hand2",fg="red")
        btn_conect.place(x=700,y=5,width=220,height=50)

        self.var_choice=StringVar()
        simple=Radiobutton(self.root,text="One send",value="one",activebackground="white",variable=self.var_choice,font=("times new roman",25,"bold"),bg="white").place(x=50,y=250)        
        multi=Radiobutton(self.root,text="Multiple send",value="many",activebackground="white",variable=self.var_choice,font=("times new roman",25,"bold"),bg="white").place(x=250,y=250)        


        
        
        #function
    def fen_conect(self):
        self.root2=Toplevel()
        self.root2.title("Connecte to your email")
        self.root2.config(bg="white")
        self.root2.geometry("800x400+600+500")
        self.root2.focus_force()
        
        
        #title
        title1=Label(self.root2,text="Connect to your gmail account",font=("Agerian",30),bg="teal",fg="black")
        title1.pack(side=TOP,fill=X)
        
        
        email=Label(self.root2,text="Email",font=("times new roman",20),bg="white").place(x=320,y=60)
        password=Label(self.root2,text="Password",font=("times new roman",20),bg="white").place(x=320,y=160)

        
        self.email=Entry(self.root2,font=("times new roman",18),bg="gray").place(x=200,y=120,width=350)
        self.password=Entry(self.root2,font=("times new roman",18),bg="gray").place(x=200,y=220,width=350)
        btn_un=Button(self.root2,text='Connect',font=("times new roman",18),bg="green",cursor="hand2").place(x=200,y=300,width=170)
        btn_conecti=Button(self.root2,text="Cancel",font=("times new roman",18),bg="red",cursor="hand2").place(x=490,y=300,width=170)
    
        
        
        
            








if __name__ == '__main__':
    root=Tk()
    obj=Mail(root)
    root.mainloop()
