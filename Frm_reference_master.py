from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import tkinter as tk

def Frm_reference_master(master):
    reference_master = Toplevel(master)
    reference_master.geometry("600x300+450+190")
    reference_master.title('Reference form')
    
    def Save_Data():
        pass
        
    def reset():
        reference_master.geometry("600x300+450+190")
        BtnShow['text'] = 'Show'
        BtnShow['command'] = expand
        
        
    def expand():
        reference_master.geometry("1000x300+300+190")
        BtnShow['text'] = 'Reset'
        BtnShow['command'] = reset
        
    def show_selected_record(event):
        for selection in List.selection():
            item = List.item(selection)


    Frm1 = LabelFrame(reference_master, height=285, width=580)
    Frm1.place(x=10, y=10)

    LblHead = Label(Frm1, text='Reference Form', font=('Arial',25), fg='red')
    LblHead.place(x=190,y=10)
    
    LblNo = Label(Frm1, text='No:', font=('Arial',17))
    LblNo.place(x=60,y=70)
    TxtNo = Entry(Frm1, width=4, font=('Arial',17), justify='center')
    TxtNo.place(x=205,y=70)

    LblName = Label(Frm1, text='Name:', font=('Arial',17))
    LblName.place(x=60,y=110)
    Name = Entry(Frm1, width=25, font=('Arial',17))
    Name.place(x=205,y=110)

    BtnSave = Button(Frm1, text="Save",width=8, font=('Arial',17),fg='white', bg='green',command=Save_Data)
    BtnSave.place(x=30,y=210)
    BtnShow = Button(Frm1, text="Show",width=8, font=('Arial',17),fg='white', bg='brown',command=expand)
    BtnShow.place(x=160,y=210)
    BtnDelete = Button(Frm1, text="Delete",width=8, font=('Arial',17),fg='white',bg='orange')
    BtnDelete.place(x=290,y=210)
    BtnExit = Button(Frm1, text="Exit",width=8, font=('Arial',17),fg='white',bg='red')
    BtnExit.place(x=420,y=210)
    
    columns = ('#1', '#2')
    List = ttk.Treeview(reference_master,show="headings",height="10", columns=columns)
    List.heading('#1', text='No', anchor='center')
    List.column('#1', width=80, anchor='center', stretch=False)
    List.heading('#2', text='Name', anchor='center')
    List.column('#2', width=150, anchor='w', stretch=True)
    List.place(x=610, y=10, height=280, width=370)  

    vsb= ttk.Scrollbar(reference_master,orient=tk.VERTICAL,command=List.yview)  
    vsb.place(x=990, y=10, height=280)
    List.configure(yscroll=vsb.set)

    List.delete(*List.get_children())

    List.bind("<Double-1>", show_selected_record)    
    

    reference_master.mainloop()

#HostelAdd()