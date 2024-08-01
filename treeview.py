import tkinter as tk
from tkinter import *
from tkinter import ttk
from dbaccess import connect_db_user_data

def viewer(menu_window):
    menu_window.withdraw()
    window = tk.Toplevel(menu_window)

    window.title("view")
    window.geometry("600x300")

    connect = connect_db_user_data()
    conn = connect.cursor()
    conn.execute("SELECT * FROM users_profile")

    def back():
        window.destroy()
        menu_window.deiconify()

    tree=ttk.Treeview(window)
    tree["show"]="headings"
    s=ttk.Style(window)
    s.theme_use("clam")


    tree["columns"]=("first_name","last_name","title","nationality","age","student_id","phone_number","email_id","home_address","home_district","home_state","home_country","school_name","school_grad_year","college_name","college_enroll_year","college_department","skills","projects","job"
    )

    tree.column("first_name", width=100, minwidth=100, anchor=tk.CENTER)
    tree.column("last_name", width=100, minwidth=100, anchor=tk.CENTER)
    tree.column("title", width=50, minwidth=50, anchor=tk.CENTER)
    tree.column("nationality", width=100, minwidth=100, anchor=tk.CENTER)
    tree.column("age", width=50, minwidth=50, anchor=tk.CENTER)
    tree.column("student_id", width=100, minwidth=100, anchor=tk.CENTER)
    tree.column("phone_number", width=150, minwidth=150, anchor=tk.CENTER)
    tree.column("email_id", width=150, minwidth=150, anchor=tk.CENTER)
    tree.column("home_address", width=200, minwidth=200, anchor=tk.CENTER)
    tree.column("home_district", width=100, minwidth=100, anchor=tk.CENTER)
    tree.column("home_state", width=100, minwidth=100, anchor=tk.CENTER)
    tree.column("home_country", width=100, minwidth=100, anchor=tk.CENTER)
    tree.column("school_name", width=100, minwidth=100, anchor=tk.CENTER)
    tree.column("school_grad_year", width=50, minwidth=50, anchor=tk.CENTER)
    tree.column("college_name", width=100, minwidth=100, anchor=tk.CENTER)
    tree.column("college_enroll_year", width=50, minwidth=50, anchor=tk.CENTER)
    tree.column("college_department", width=100, minwidth=100, anchor=tk.CENTER)
    tree.column("skills", width=200, minwidth=200, anchor=tk.CENTER)
    tree.column("projects", width=200, minwidth=200, anchor=tk.CENTER)
    tree.column("job", width=200, minwidth=200, anchor=tk.CENTER)


    tree.heading("first_name", text="first_name", anchor=tk.CENTER)
    tree.heading("last_name", text="last_name", anchor=tk.CENTER)
    tree.heading("title", text="title", anchor=tk.CENTER)
    tree.heading("nationality", text="nationality", anchor=tk.CENTER)
    tree.heading("age", text="age", anchor=tk.CENTER)
    tree.heading("student_id", text="student_id", anchor=tk.CENTER)
    tree.heading("phone_number", text="phone_number", anchor=tk.CENTER)
    tree.heading("email_id", text="email_id", anchor=tk.CENTER)
    tree.heading("home_address", text="home_address", anchor=tk.CENTER)
    tree.heading("home_district", text="home_district", anchor=tk.CENTER)
    tree.heading("home_state", text="home_state", anchor=tk.CENTER)
    tree.heading("home_country", text="home_country", anchor=tk.CENTER)
    tree.heading("school_name", text="school_name", anchor=tk.CENTER)
    tree.heading("school_grad_year", text="school_grad_year", anchor=tk.CENTER)
    tree.heading("college_name", text="college_name", anchor=tk.CENTER)
    tree.heading("college_enroll_year", text="college_enroll_year", anchor=tk.CENTER)
    tree.heading("college_department", text="college_department", anchor=tk.CENTER)
    tree.heading("skills", text="skills", anchor=tk.CENTER)
    tree.heading("projects", text="projects", anchor=tk.CENTER)
    tree.heading("job", text="job", anchor=tk.CENTER)

    i = 0
    for ro in conn:
        tree.insert("", i, text="", values=(
            ro[0],  # first_name
            ro[1],  # last_name
            ro[2],  # title
            ro[3],  # nationality
            ro[4],  # age
            ro[5],  # student_id
            ro[6],  # phone_number
            ro[7],  # email_id
            ro[8],  # home_address
            ro[9], # home_district
            ro[10], # home_state
            ro[11], # home_country
            ro[12], # school_name
            ro[13], # school_grad_year
            ro[14], # college_name
            ro[15], # college_enroll_year
            ro[16], # college_department
            ro[17], # skills
            ro[18], # projects
            ro[19]  # job
        ))
        i += 1

    hsb= ttk.Scrollbar(window,orient="horizontal")

    hsb.configure(command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X,side = BOTTOM)

    tree.pack()

    back_button = tk.Button(window, text="Back", command=back)
    back_button.pack(pady=10)

    window.mainloop()