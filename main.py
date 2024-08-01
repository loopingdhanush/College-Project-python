    #main.py

import tkinter as tk
from login import loginpage
from Signup import signup

def loginbuttonremove(home):
    loginpage(home)

def signupbuttonremove(home):
    signup(home)

home = tk.Tk()
home.title("homepage")
home.geometry("300x300")

frame=tk.Frame(home)
frame.pack()

loginbutton = tk.Button(frame,text="Login page",pady=20,command =lambda: loginbuttonremove(home))
loginbutton.grid(row=0, column=0)

sbutton = tk.Button(frame,text="signup page",pady=20,command =lambda: signupbuttonremove(home))
sbutton.grid(row=0, column=1)

home.mainloop()
