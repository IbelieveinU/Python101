from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import massagebox

GUI = Tk() # นี่คือหน้าจอหลักของโปรแกรม





GUI.title('โปรแกรมบันทึกข้อมูล') #นี่คือชื่อโปรแกรม
GUI.geometry('500x400') #นี่คือขนาดโปรแกรม

L1 = Lable(GUI,text='โปรแกรมบันทึกความรู้', font=('Angsana New',3), fg='green')
ฺB1 = ttk.Button(GUI, text='เงินมีอยู่กี่บาท')
B1.pack(ipadx=20, ipady=20)

#########
def Button2():
    text = 'ตอนนี้มีเงินในบัญชีอยู่ 300 บาท'
    messangebox.showinfor('เงินในบัญชี',text)

FB1 = LabelFrame(GUI)# คล้ายกระดาน
FB1.place(x=10, y=10)
ฺB2 = ttk.Button(GUI, text='เงินมีอยู่กี่บาท')
B2.pack(ipadx=20, ipady=20)
########


GUI.maninloop()
