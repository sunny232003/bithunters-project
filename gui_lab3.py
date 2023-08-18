from tkinter import *
root=Tk()
root.geometry('500x500')
var1=IntVar()
mycheck1=Checkbutton(root,text='male',variable=var1).grid(row=0,column=0)
var2=IntVar()
mycheck2=Checkbutton(root,text='female',variable=var2).grid(row=1,column=0)
root.mainloop()