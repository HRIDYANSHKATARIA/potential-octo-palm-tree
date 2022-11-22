from tkinter import *

root = Tk()

root.title("Identifier")
root.geometry("400x400")

name_l = Label(root,text="Name")
name_l.place(relx=0.2,rely=0.2,anchor=CENTER)

name_entry = Entry(root)
name_entry.place(relx=0.6,rely=0.2,anchor=CENTER)

pass_l = Label(root,text="Password")
pass_l.place(relx=0.2,rely=0.3,anchor=CENTER)

pass_entry = Entry(root)
pass_entry.place(relx=0.6,rely=0.3,anchor=CENTER)

cap_l = Label(root,text="Captcha")
cap_l.place(relx=0.2,rely=0.4,anchor=CENTER)

cap_entry = Entry(root)
cap_entry.place(relx=0.6,rely=0.4,anchor=CENTER)

label_name = Label(root,text="")
label_name.place(relx=0.5,rely=0.6,anchor=CENTER)

label_pass = Label(root,text="")
label_pass.place(relx=0.5,rely=0.7,anchor=CENTER)

label_cap = Label(root,text="")
label_cap.place(relx=0.5,rely=0.8,anchor=CENTER)

def show():
    name = name_entry.get()
    password = pass_entry.get()
    cap = cap_entry.get()
    label_name["text"]=str("Name = "+name)
    label_pass["text"]=str("Password = "+password)
    label_cap["text"]=str("Captcha = "+cap)
    
btn = Button(root,text="Check",command=show)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
