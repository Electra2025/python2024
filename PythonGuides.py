from tkinter import *
from tkinter.ttk import Combobox
import sqlite3
import tkinter as tk

a=tk.Tk()
a.geometry('500x500')
a.title('Registeration')

rd_btn = tk.StringVar(value='0')

def set_db():
    con = sqlite3.connect('reg.db')
    cursor_obj = con.cursor()

    t1 = """CREATE TABLE Reg_Info(
        Name VARCHAR(255) NOT NULL,
        Email VARCHAR(255) NOT NULL,
        Contact VARCHAR(255) NOT NULL,
        Gender VARCHAR(255) NOT NUll,
        Country VARCHAR(255) NOT NULL,
        Passsword VARCHAR(255) NOT NULL,
        Re_Password VARCHAR(255)
    );"""
    cursor_obj.execute(t1)
    con.commit()
    con.close()

def insert():
    name = en1.get()
    email = em1.get()
    contact_number = cn1.get()
    male = m.get()
    female = fm.get()
    others = o.get()
    country = c_cmb.get()
    password = p1.get()
    re_password = rp1.get()
    print(name)
    print(email)
    print(contact_number)
    print(male)
    print(female)
    print(others)
    print(country)
    print(password)
    print(re_password)

def reg_message():
    reg_msg = Toplevel()
    reg_msg.geometry('200x200')
    reg_lb = Label(reg_msg,text='Register is successful')
    reg_lb.pack()

    reg_b = Button(reg_msg,text='Close',command=a.destroy)
    reg_b.pack()

lf1 = LabelFrame(a)
lf1.grid(row=3,column=1)

en = Label(a,text='Enter Name ')
en.grid(row=0,column=0,padx=10,pady=20)
en1 = Entry(a)
en1.grid(row=0,column=1,padx=10,pady=20)

em = Label(a,text='Enter Email ')
em.grid(row=1,column=0,padx=5,pady=5)
em1 = Entry(a)
em1.grid(row=1,column=1,padx=5,pady=5)

cn = Label(a,text='Contact Number ')
cn.grid(row=2,column=0,padx=5,pady=5)
cn1 = Entry(a)
cn1.grid(row=2,column=1,padx=5,pady=5)

g = Label(a,text='Select Gender ')
g.grid(row=3,column=0,padx=5,pady=5)

m = tk.Radiobutton(lf1,text='Male',value='0',variable=rd_btn).grid(row=3,columnspan=2,padx=5,pady=5)
fm = tk.Radiobutton(lf1,text='Female',value='1',variable=rd_btn).grid(row=3,column=2,padx=5,pady=5)
o = tk.Radiobutton(lf1,text='Others',value='2',variable=rd_btn).grid(row=3,column=3,padx=5,pady=5)

c = Label(a,text='Select Country ')
c.grid(row=4,column=0,padx=5,pady=5)

c_cmb = Combobox(a,values=['United States', 'United Kingdown','Canada','Austrila','New Zealand','Japan','China'])
c_cmb.set('Select Country')
c_cmb.grid(row=4,column=1,padx=5,pady=5)

p = Label(a,text='Enter Password ')
p.grid(row=5,column=0,padx=5,pady=5)
p1 = Entry()
p1.grid(row=5,column=1,padx=5,pady=5)

rp = Label(a,text='Re-Enter Password ')
rp.grid(row=6,column=0,padx=5,pady=5)
rp1 = Entry()
rp1.grid(row=6,column=1,padx=5,pady=5)

b1 = Button(a,text='Register',highlightbackground='yellow',fg='red',command=insert).grid(row=7,column=0,padx=5,pady=5)
b2 = Button(a, text='Cancel',highlightbackground='grey',fg='blue',command=a.destroy).grid(row=7,column=1,padx=5,pady=5)

a.mainloop()