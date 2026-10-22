#1]
import tkinter as tk
root = tk.Tk()
root.title("Form")
tk.Label(root, text="Name").pack()
tk.Entry(root).pack()
tk.Label(root, text="Subject").pack()
tk.Checkbutton(root, text="Python").pack()
tk.Checkbutton(root, text="Java").pack()
tk.Checkbutton(root, text="C++").pack()
tk.Button(root, text="Submit").pack()
root.mainloop()

#2]
from tkinter import *
root = Tk()
root.title("Hello World")
root.geometry("300x200")
Label(root, text="Hello World!").pack()
root.mainloop()

#3]
from tkinter import *
def click():
    label.config(text="Button Clicked!")
root = Tk()
root.title("Button Example")
root.geometry("300x200")
label = Label(root, text="Click the button")
label.pack()
Button(root, text="Click Me", command=click).pack()
root.mainloop()

#4]
from tkinter import *
def add():
    a = int(e1.get())
    b = int(e2.get())
    result.config(text="Sum = " + str(a + b))
root = Tk()
root.title("Addition")
root.geometry("300x250")
Label(root, text="First Number").pack()
e1 = Entry(root)
e1.pack()
Label(root, text="Second Number").pack()
e2 = Entry(root)
e2.pack()
Button(root, text="Add", command=add).pack()
result = Label(root, text="Sum = ")
result.pack()
root.mainloop()

#5]
from tkinter import *
def login():
    if user.get() == "admin" and pwd.get() == "1234":
        result.config(text="Login Successful")
    else:
        result.config(text="Invalid Login")
root = Tk()
root.title("Login Form")
root.geometry("300x250")
Label(root, text="Username").pack()
user = Entry(root)
user.pack()
Label(root, text="Password").pack()
pwd = Entry(root, show="*")
pwd.pack()
Button(root, text="Login", command=login).pack()
result = Label(root, text="")
result.pack()
root.mainloop()

#6]
from tkinter import *
def calculate():
    a = float(e1.get())
    b = float(e2.get())
    op = operator.get()

    if op == "+":
        ans = a + b
    elif op == "-":
        ans = a - b
    elif op == "*":
        ans = a * b
    elif op == "/" and b != 0:
        ans = a / b
    else:
        result.config(text="Invalid Operation")
        return

    result.config(text="Answer = " + str(ans))
root = Tk()
root.title("Calculator")
root.geometry("300x300")
Label(root, text="First Number").pack()
e1 = Entry(root)
e1.pack()
Label(root, text="Second Number").pack()
e2 = Entry(root)
e2.pack()
Label(root, text="Operator (+, -, *, /)").pack()
operator = Entry(root)
operator.pack()
Button(root, text="Calculate", command=calculate).pack()
result = Label(root, text="Answer = ")
result.pack()
root.mainloop()