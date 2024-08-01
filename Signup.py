#signup

import tkinter as tk
from tkinter import messagebox
import mysql.connector
import time
from dbaccess import connect_db_user_db

def signup(main_window):
    main_window.withdraw()
    signup_window = tk.Toplevel(main_window)
    signup_window.title("Signup Page")
    signup_window.geometry("300x300")

    def add_user():
        username = un1.get()
        password = pw1.get()

        # Debug prints to check the types and values
        print(f"username: {username} (type: {type(username)})")
        print(f"password: {password} (type: {type(password)})")

        li.grid_remove()
        nli.grid_remove()
        
        # Connect to the MySQL database
        try:
            dbconnection = connect_db_user_db()
            cursor = dbconnection.cursor()

            # Query to check if the username already exists
            check_query = "SELECT * FROM users WHERE username = %s"
            cursor.execute(check_query, (username,))
            result = cursor.fetchone()

            if result:
                nli.grid(row=5, column=1)
            else:
                # Query to add the new user
                add_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
                cursor.execute(add_query, (username, password))
                dbconnection.commit()
                li.grid(row=5, column=1)
                signup_window.after(5000, back_to_main)  # Return to main window after 5 seconds
                clear_fields()
            
            cursor.close()
            dbconnection.close()
        
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error connecting to MySQL: {err}")

    def back_to_main():
        signup_window.destroy()
        main_window.deiconify()

    def clear_fields():
        un1.delete(0, tk.END)  # Clear the username entry field
        pw1.delete(0, tk.END)  # Clear the password entry field

    f = tk.Frame(signup_window)

    label = tk.Label(f, text="Signup", font=("Arial", 20))

    un = tk.Label(f, text="student id")
    un1 = tk.Entry(f)

    pw = tk.Label(f, text="Password")
    pw1 = tk.Entry(f)

    lb = tk.Button(f, text="Signup", command=add_user)
    bb = tk.Button(f, text="Back", command=back_to_main)

    li = tk.Label(f, text="Signup Successful")
    nli = tk.Label(f, text="User already exists")

    label.grid(row=0, column=1)
    un.grid(row=1, column=0)
    un1.grid(row=1, column=1)
    pw.grid(row=2, column=0)
    pw1.grid(row=2, column=1)
    lb.grid(row=3, column=1)
    bb.grid(row=4, column=1)

    f.pack()

# For testing purpose: Initialize the main Tkinter window
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    signup(root)
    root.mainloop()
