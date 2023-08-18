from tkinter import *
root=Tk()
root.geometry()
lb1=Label(root,text='form').pack()
e=Entry(root,width=30)
e.pack()
e.insert(2,'enter your name')
def click():
    message='hello '+e.get()
    lb4=Label(root,text=message,font=20).pack()
bt1=Button(root,text='click here',command=click).pack()
root.mainloop()
