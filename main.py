from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
from Frm_account_master import Frm_Account_master
from Frm_reference_master import Frm_reference_master


def Open_Forms(x):
    if x == 1:
        Frm_Account_master(root)
        
    if x==2:
        Frm_reference_master(root)

root=Tk()
root.geometry("1530x790+0+0")

#bg image
img1=Image.open(r"F:\project\Tkinter\assets\bg.jpg")
img1=img1.resize((1530,790),Image.ANTIALIAS)
photoimg1=ImageTk.PhotoImage(img1)

bg_img=Label(root,image=photoimg1)
bg_img.place(x=0,y=0,width=1530,height=790)

title_lbl=Label(bg_img,text="M & H Group",font=("times new roman",30,"bold"))
title_lbl.place(x=470,y=0,width=550,height=45)

Btn_acc_master = Button(bg_img, text='List',command=lambda x=1:Open_Forms(x), bg='brown', fg='white', width=12, font=('Arial',14))
Btn_acc_master.place(x=260,y=280)

Btn_acc_master = Button(bg_img, text='item',command=lambda x=2:Open_Forms(x), bg='brown', fg='white', width=12, font=('Arial',14))
Btn_acc_master.place(x=500,y=280)


root.mainloop()