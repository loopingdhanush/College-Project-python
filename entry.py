import tkinter as tk
from tkinter import ttk, messagebox
from dbaccess import connect_db_user_data
from dbaccess import fetch_data

def data_entry(menu_window, studentid):

    def save_data():
        db = connect_db_user_data()
        cursor = db.cursor()

        query = """
        INSERT INTO users_profile (first_name, last_name, title, nationality, age, student_id, phone_number, email_id,
        home_address, home_district, home_state, home_country, school_name, school_grad_year, college_name,
        college_enroll_year, college_department, skills, projects, job)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE first_name = VALUES(first_name), last_name = VALUES(last_name), title = VALUES(title),
        nationality = VALUES(nationality), age = VALUES(age), phone_number = VALUES(phone_number), email_id = VALUES(email_id),
        home_address = VALUES(home_address), home_district = VALUES(home_district), home_state = VALUES(home_state),
        home_country = VALUES(home_country), school_name = VALUES(school_name), school_grad_year = VALUES(school_grad_year),
        college_name = VALUES(college_name), college_enroll_year = VALUES(college_enroll_year),
        college_department = VALUES(college_department), skills = VALUES(skills), projects = VALUES(projects), job = VALUES(job)
        """

        values = (
            firstnamee.get(), lastnamee.get(), title_combobox.get(), nationale.get(), age_spinbox.get(), studentide.get(),
            phe.get(), ee.get(), ade.get(), de.get(), se.get(), ce.get(), school_entry.get(), school_year_entry.get(),
            college_entry.get(), college_year_entry.get(), department_entry.get(), skills_entry.get(), projects_entry.get(),
            job_entry.get()
        )

        cursor.execute(query, values)
        db.commit()
        db.close()
        messagebox.showinfo("Info", "Data saved successfully")
    
    menu_window.withdraw()
    window = tk.Toplevel(menu_window)
    window.title("Data Entry Form")

    frame = tk.Frame(window)
    frame.pack(padx=10, pady=10)

    
    
    # going back
    def back():
        window.destroy()
        menu_window.deiconify()
   


    # User info
    userinfo = tk.LabelFrame(frame, text="User Information")
    userinfo.grid(row=0, column=0, padx=20, pady=20)

    firstname = tk.Label(userinfo, text="First Name")
    firstname.grid(row=0, column=0)
    firstnamee = tk.Entry(userinfo)
    firstnamee.grid(row=1, column=0)

    lastname = tk.Label(userinfo, text="Last Name")
    lastname.grid(row=0, column=1)
    lastnamee = tk.Entry(userinfo)
    lastnamee.grid(row=1, column=1)

    title = tk.Label(userinfo, text="Title")
    title.grid(row=0, column=2)
    title_combobox = ttk.Combobox(userinfo, values=["", "Mr.", "Ms.", "Dr."])
    title_combobox.grid(row=1, column=2)

    age_label = tk.Label(userinfo, text="Age")
    age_label.grid(row=2, column=0)
    age_spinbox = tk.Spinbox(userinfo, from_=16, to=110)
    age_spinbox.grid(row=3, column=0)

    national = tk.Label(userinfo, text="Nationality")
    national.grid(row=2, column=1)
    nationale = tk.Entry(userinfo)
    nationale.grid(row=3, column=1)

    studentid_label = tk.Label(userinfo, text="Student Id")
    studentid_label.grid(row=2, column=2)
    studentide = tk.Entry(userinfo)
    studentide.insert(0,studentid)
    studentide.grid(row=3, column=2)

    for widget in userinfo.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    # Contact info
    cinfo = tk.LabelFrame(frame, text="Contact Information")
    cinfo.grid(row=1, column=0, sticky="news", padx=20, pady=20)

    ph = tk.Label(cinfo, text="Phone Number")
    ph.grid(row=0, column=0)
    phe = tk.Entry(cinfo)
    phe.grid(row=1, column=0)

    e = tk.Label(cinfo, text="Email")
    e.grid(row=0, column=1)
    ee = tk.Entry(cinfo)
    ee.grid(row=1, column=1)

    ad = tk.Label(cinfo, text="Address")
    ad.grid(row=0, column=2)
    ade = tk.Entry(cinfo)
    ade.grid(row=1, column=2)

    d = tk.Label(cinfo, text="District")
    d.grid(row=2, column=2)
    de = tk.Entry(cinfo)
    de.grid(row=3, column=2)

    s = tk.Label(cinfo, text="State")
    s.grid(row=2, column=1)
    se = tk.Entry(cinfo)
    se.grid(row=3, column=1)

    c = tk.Label(cinfo, text="Country")
    c.grid(row=2, column=0)
    ce = tk.Entry(cinfo)
    ce.grid(row=3, column=0)

    for widget in cinfo.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    # Education and Work Experience
    edu_work = tk.LabelFrame(frame, text="Education and Work Experience")
    edu_work.grid(row=2, column=0, sticky="news", padx=20, pady=20)

    school_label = tk.Label(edu_work, text="School Name")
    school_label.grid(row=0, column=0)
    school_entry = tk.Entry(edu_work)
    school_entry.grid(row=1, column=0)

    school_year_label = tk.Label(edu_work, text="Year of Graduation (school)")
    school_year_label.grid(row=0, column=1)
    school_year_entry = tk.Entry(edu_work)
    school_year_entry.grid(row=1, column=1)

    college_label = tk.Label(edu_work, text="College Name")
    college_label.grid(row=0, column=2)
    college_entry = tk.Entry(edu_work)
    college_entry.grid(row=1, column=2)

    college_year_label = tk.Label(edu_work, text="Year of Enrollment (college)")
    college_year_label.grid(row=2, column=0)
    college_year_entry = tk.Entry(edu_work)
    college_year_entry.grid(row=3, column=0)

    department_label = tk.Label(edu_work, text="Department")
    department_label.grid(row=2, column=1)
    department_entry = tk.Entry(edu_work)
    department_entry.grid(row=3, column=1)

    skills_label = tk.Label(edu_work, text="Skills")
    skills_label.grid(row=2, column=2)
    skills_entry = tk.Entry(edu_work)
    skills_entry.grid(row=3, column=2)

    projects_label = tk.Label(edu_work, text="Projects")
    projects_label.grid(row=4, column=0)
    projects_entry = tk.Entry(edu_work)
    projects_entry.grid(row=5, column=0)

    job_label = tk.Label(edu_work, text="Job")
    job_label.grid(row=4, column=1)
    job_entry = tk.Entry(edu_work)
    job_entry.grid(row=5, column=1)

    for widget in edu_work.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    button = tk.Button(frame, text="Save Data", command=save_data)
    button.grid(row=3, column=0, pady=10)
    

    buttonback = tk.Button(frame, text="Back", command=back)
    buttonback.grid(row=4, column=0, pady=10)

    def prefill_data(student_id):
            print("opening print data")
            data = fetch_data(student_id)
            print("data fetched")
            print(data)
            if data:
                firstnamee.insert(0, data[0])
                lastnamee.insert(0, data[1])
                title_combobox.set(data[2])
                nationale.insert(0, data[3])
                age_spinbox.delete(0, "end")
                age_spinbox.insert(0, data[4])
                phe.insert(0, data[6])
                ee.insert(0, data[7])
                ade.insert(0, data[8])
                de.insert(0, data[9])
                se.insert(0, data[10])
                ce.insert(0, data[11])
                school_entry.insert(0, data[12])
                school_year_entry.insert(0, data[13])
                college_entry.insert(0, data[14])
                college_year_entry.insert(0, data[15])
                department_entry.insert(0, data[16])
                skills_entry.insert(0, data[17])
                projects_entry.insert(0, data[18])
                job_entry.insert(0, data[19])

    # Call prefill_data with the provided studentid
    prefill_data(studentid)
    

    
    window.mainloop()