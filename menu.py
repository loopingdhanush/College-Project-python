#menu.py

import tkinter as tk
from entry import data_entry
from treeview import viewer


def editor(ewindow,studentid):
    data_entry(ewindow,studentid)


def menuop(lwindow,studentid):
    print(studentid)
    lwindow.withdraw()
    menuwindow = tk.Toplevel(lwindow)

    def back():
        menuwindow.destroy()
        lwindow.deiconify()
    

    menuwindow.title("menu")
    menuwindow.geometry("340x310")

    button = tk.Button(menuwindow,text="User Profile Entry",command=lambda:editor(menuwindow,studentid))
    button.grid(row=0, column=0)

    buttonback = tk.Button(menuwindow,text = "Log Out",command=back)
    buttonback.grid(row=1,column=0)

    buttonall = tk.Button(menuwindow,text = "view all profiles",command=lambda:viewer(menuwindow))
    buttonall.grid(row=2,column=0)
