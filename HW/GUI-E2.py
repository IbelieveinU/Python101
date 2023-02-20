from tkinter import *
from tkinter import ttk
from tkinter import messagebox


GUI = Tk()
GUI.title('เรียนกับลุงส่งการบ้านหรือยัง ?')
GUI.geometry('500x400')

def Button1():
    text = 'ส่งแล้ว'
    messagebox.showinfo('ยังไม่ได้ส่ง',text)

FB1 = Frame(GUI)
FB1.place(x=80, y=10)
B1 = ttk.Button(FB1,text='เรียนครั้งที่ 1',command=Button1)
B1.pack(ipadx=20, ipady=20)

def Button2():
    text = 'ส่งแล้ว'
    messagebox.showinfo('ยังไม่ได้ส่ง',text)

FB2 = Frame(GUI)
FB2.place(x=80, y=80)
B2 = ttk.Button(FB2,text='เรียนครั้งที่ 2',command=Button2)
B2.pack(ipadx=20, ipady=20)

def Button3():
    text = 'ส่งแล้ว'
    messagebox.showinfo('ยังไม่ได้ส่ง',text)

FB3 = Frame(GUI)
FB3.place(x=80, y=150)
B3 = ttk.Button(FB3,text='เรียนครั้งที่ 3',command=Button3)
B3.pack(ipadx=20, ipady=20)

def Button4():
    text = 'ส่งแล้ว'
    messagebox.showinfo('ยังไม่ได้ส่ง',text)

FB4 = Frame(GUI)
FB4.place(x=80, y=220)
B4 = ttk.Button(FB4,text='เรียนครั้งที่ 4',command=Button3)
B4.pack(ipadx=20, ipady=20)

def Button5():
    text = 'ส่งแล้ว'
    messagebox.showinfo('ยังไม่ได้ส่ง',text)

FB5 = Frame(GUI)
FB5.place(x=80, y=290)
B5 = ttk.Button(FB5,text='เรียนครั้งที่ 5',command=Button3)
B5.pack(ipadx=20, ipady=20)

GUI.mainloop()
