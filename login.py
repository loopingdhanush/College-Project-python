#login.py

import tkinter as tk
from tkinter import messagebox
from menu import menuop
import mysql.connector

def loginpage(main_window):
    main_window.withdraw()
    login_window = tk.Toplevel(main_window)
    login_window.title("Login Page")
    login_window.geometry("300x300")

    def login():
        username = un1.get()
        password = pw1.get()
        li.grid_remove()
        nli.grid_remove()
        
        # Connect to the MySQL database
        try:
            connect = mysql.connector.connect(
                host='localhost',      
                user='root',   
                password='12345',
                database='user_db'     
            )
            cursor = connect.cursor()

            # Query to check if the username and password exist

            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            

            if result:
                #li.grid(row=5,column=1)
                clear_fields()
                menuop(login_window,username)
            else:
                nli.grid(row=5,column=1)
            
            cursor.close()
            connect.close()
        
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error connecting to MySQL: {err}")

    
    def back_to_main():
        login_window.destroy()  
        main_window.deiconify()  
    
    def clear_fields():
        un1.delete(0, tk.END)  # Clear the username entry field
        pw1.delete(0, tk.END)  # Clear the password entry field
        

    f = tk.Frame(login_window)

    label = tk.Label(f, text="Login",font = ("Arial",20   ))

    un = tk.Label(f, text="student id")
    un1 = tk.Entry(f)

    pw = tk.Label(f, text="Password")
    pw1 = tk.Entry(f)

    lb = tk.Button(f, text="Login",command = login )
    bb = tk.Button(f, text="back",command = back_to_main)

    li = tk.Label(f, text="login sucessfull")
    nli = tk.Label(f, text="login unsucessfull")

    label.grid(row=0,column=1)
    un.grid(row=1,column=0)
    un1.grid(row=1,column=1)
    pw.grid(row=2,column=0)
    pw1.grid(row=2,column=1)
    lb.grid(row=3,column=1)
    bb.grid(row=4,column=1)

    f.pack()


