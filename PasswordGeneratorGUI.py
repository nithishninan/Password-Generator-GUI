from tkinter import *
import random
window = Tk()
window.title("Password suggestion generator")
window.geometry('600x200')
label1 = Label(window, text = "Enter the number of charecters for password", font=("Arial Bold",10),fg="blue")
label1.grid(row=2, column=0)
label = Label(window, font=("Arial Bold",10),fg="red")
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '0123456789'
symbol = '!@#$%^&*()_+<>/'
txt = Entry(window,width=5)
txt.grid(row=2,column=2)
def clicked():
    length = int(txt.get())
    string = lower + upper + number + symbol
    password = "".join(random.sample(string, length))
    res="Suggested password:==>       " +password
    label.configure(text=res)
    label.grid(row=15, column=0)
bt1= Button(window,text="Entry",fg="green",font=("Arial Bold",10),bg="yellow",command=clicked)
bt1.grid(row=5,column=2)
window.mainloop()

#Command for converting python file to exe
# pyinstaller --onefile -w PasswordGeneratorGUI.py