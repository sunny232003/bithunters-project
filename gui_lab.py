from tkinter import *
#print(dir(tkinter))
root=Tk()
root.geometry('900x200')
#pack automatically resizes the widget but in grid you need to resize manually
mylabel=Label(root,text='Not GUI class',font=25,bg='yellow').grid(row=0,column=0)
mylabel=Label(root,text='GUI class',font=35,bg='yellow')
lab1=Label(root,text='click',font=100).grid(row=10,column=20)
def myfun():
    mylabel2=Label(root,text='button clicked').grid(row=35,column=40)

def add():
    a,b=5,6
    s=a+b
    slabel=Label(root,text=s,font=35).grid(row=30,column=50)

bt1=Button(root,text='click here',bg='blue',command=myfun).grid(row=30,column=40)
root.mainloop()

