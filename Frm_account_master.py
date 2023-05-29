import csv
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox

def Frm_Account_master(master):
    Take_Att = Toplevel(master)
    Take_Att.geometry("500x500+500+300")

    def show_selected_record(event):
        pass

    def Reset_Form():
        Take_Att.geometry("500x400+500+100")
        BtnList['text'] = 'List'
        BtnList['command'] = Expand_Form

    def Expand_Form():
        Take_Att.geometry("1000x500+400+300")
        BtnList['text'] = 'Reset'
        BtnList['command'] = Reset_Form

    def Save_Data():
        val_code = Txtcode.get()
        val_name = Txtname.get()
        val_phn1 = Txtphn1.get()
        val_phn2 = Txtphn2.get()
        val_phn3 = Txtphn3.get()
        val_city = TxtCity.get()

    Take_Att.title("Account Registeration Form")

    Frm1 = LabelFrame(Take_Att, width=470, height=480,)
    Frm1.place(x=10,y=10)
    
    Frm2 = LabelFrame(Take_Att, width=470, height=480,)
    Frm2.place(x=500,y=10)
    
    LblHead = Label(Frm1, text='Account Registeration Form', font=('Times New Roman',24), fg='red')
    LblHead.place(x=60,y=10)
    
    code= Label(Frm1, text='Acc Code:',font=('Times New Roman',16))
    code.place(x=10,y=70)
    Txtcode= Entry(Frm1, width=20, font=('Times New Roman',16))
    Txtcode.place(x=140,y=70)
    

    Lblname= Label(Frm1, text='Name:',font=('Times New Roman',16))
    Lblname.place(x=10,y=120)
    Txtname= Entry(Frm1, width=20,font=('Times New Roman',16))
    Txtname.place(x=140, y=120)
    
    Lblphn1= Label(Frm1, text='Phone No1:',font=('Times New Roman',16))
    Lblphn1.place(x=10,y=170)
    Txtphn1= Entry(Frm1, width=20,font=('Times New Roman',16))
    Txtphn1.place(x=140, y=170)
    
    Lblphn2= Label(Frm1, text='Phone No2:',font=('Times New Roman',16))
    Lblphn2.place(x=10,y=220)
    Txtphn2= Entry(Frm1, width=20,font=('Times New Roman',16))
    Txtphn2.place(x=140, y=220)
    
    Lblphn3=Label(Frm1, text='Phone No3:',font=('Times New Roman',16))
    Lblphn3.place(x=10,y=270)
    Txtphn3=Entry(Frm1, width=20,font=('Times New Roman',16))
    Txtphn3.place(x=140,y=270)
    
    City=Label(Frm1, text='City:',font=('Times New Roman',16))
    City.place(x=10,y=320)
    TxtCity=Entry(Frm1, width=20,font=('Times New Roman',16))
    TxtCity.place(x=140, y=320)
    
    BtnSave = Button(Frm1, text='Save & Next', bg='green', fg='white', width=12, font=('Times New Roman',14), command=Save_Data)
    BtnSave.place(x=100,y=370)

    BtnList = Button(Frm1, text='List', bg='brown', fg='white', width=12, font=('Times New Roman',14), command=Expand_Form)
    BtnList.place(x=260,y=370)
    
    style = ttk.Style()
    style.configure("mystyle.Treeview", highlightthickness=0,width=20, bd=0, font=('Times New Roman', 12)) # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", highlightthickness=0, bd=0, font=('Times New Roman', 11)) # Modify the font of the body

    columns = ("#1", "#2", "#3", "#4","#5","")
    TreeViewOptions = ttk.Treeview(Frm2, show="headings", height="10", columns=columns, style="mystyle.Treeview")

    TreeViewOptions.heading('#1', text='Name', anchor='center')
    TreeViewOptions.column('#1', width=10, anchor='center', stretch=True)
    TreeViewOptions.heading('#2', text='Phone no1', anchor='center')
    TreeViewOptions.column('#2', width=10, anchor='center', stretch=True) 
    TreeViewOptions.heading('#3', text='Phone no2', anchor='center')
    TreeViewOptions.column('#3', width=10, anchor='center', stretch=True) 
    TreeViewOptions.heading('#4', text='Phone no3', anchor='center')
    TreeViewOptions.column('#4', width=10, anchor='center', stretch=True)
    TreeViewOptions.heading('#5', text='Code', anchor='center')
    TreeViewOptions.column('#5', width=10, anchor='center', stretch=True)
    TreeViewOptions.heading('#6', text='City', anchor='center')
    TreeViewOptions.column('#6', width=10, anchor='center', stretch=True) 

    vsb= ttk.Scrollbar(Frm2, orient=tk.VERTICAL,command=TreeViewOptions.yview)  
    vsb.place(x=480, y=5, height=370)
    TreeViewOptions.configure(yscroll=vsb.set)
    TreeViewOptions.place(x=5,y=5,height=450,width=420)
    TreeViewOptions.bind("<Double-1>", show_selected_record)

    Take_Att.mainloop()
    
#NewDetailsRegister()