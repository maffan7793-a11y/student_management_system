import csv
import customtkinter as ctk
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from datetime import datetime

# Theme settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Create window
def add_student():

    name = name_entry.get()
    age = age_entry.get()
    course = course_entry.get()

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students(name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )

    conn.commit()
    conn.close()
    view_students()
    name_entry.delete(0, "end")
    age_entry.delete(0, "end")
    course_entry.delete(0, "end")
    id_entry.delete(0, "end")

    messagebox.showinfo("Success", "Student Added Successfully!")

    name_entry.delete(0, "end")
    age_entry.delete(0, "end")
    course_entry.delete(0, "end")
app = ctk.CTk()

app.title("Student Management System")
app.geometry("1400x950")

def view_students():

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    conn.close()

    # Clear old rows
    for row in student_table.get_children():
        student_table.delete(row)

    count = 0

    for student in students:

        if count % 2 == 0:
            student_table.insert(
                "",
                "end",
                values=student,
                tags=("evenrow",)
            )

        else:
            student_table.insert(
                "",
                "end",
                values=student,
                tags=("oddrow",)
            )

        count += 1

    conn.close()
    # WRITE THIS HERE
    student_count_label.configure(
    text=f"Total Students: {len(students)}"
)



def export_students():

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    conn.close()

    with open("students_export.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["ID", "Name", "Age", "Course"])
        writer.writerows(students)

    messagebox.showinfo(
        "Export Successful",
        "Students exported to students_export.csv"
    )


def search_student():

    student_name = name_entry.get()

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE name LIKE ?",
        ('%' + student_name + '%',)
    )

    students = cursor.fetchall()

    conn.close()

    # Clear old data
    for row in student_table.get_children():
        student_table.delete(row)

    # Show search results
    for student in students:
        student_table.insert("", "end", values=student)

def delete_student():

    student_id = id_entry.get()

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Student Deleted Successfully!")

    view_students()

def export_students():

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    with open("students_export.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Age", "Course"])
        writer.writerows(students)

    conn.close()

    messagebox.showinfo(
        "Success",
        "Students exported to students_export.csv"
    )

def update_student():
    messagebox.showinfo("Update", "Update button clicked")
# Title
title = ctk.CTkLabel(
    app,
    text="STUDENT MANAGEMENT SYSTEM",
    font=("Arial", 28, "bold")

)
title.pack(pady=20)

# Main frame
main_frame = ctk.CTkFrame(app)
main_frame.pack(fill="x", padx=20, pady=10)

left_frame = ctk.CTkFrame(main_frame, width=600)
left_frame.pack(side="left", fill="both", expand=False, padx=10, pady=10)

right_frame = ctk.CTkFrame(main_frame, width=700)
right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# Left frame title
left_title = ctk.CTkLabel(
    left_frame,
    text="Quick Student Actions",
    font=("Arial", 22, "bold")
)
left_title.pack(pady=20)

# Entry fields
name_entry = ctk.CTkEntry(
    left_frame,
    placeholder_text="Enter Name",
    width=300
)
name_entry.pack(pady=5)

age_entry = ctk.CTkEntry(
    left_frame,
    placeholder_text="Enter Age",
    width=300
)
age_entry.pack(pady=5)

course_entry = ctk.CTkEntry(
    left_frame,
    placeholder_text="Enter Course",
    width=300
)
course_entry.pack(pady=5)
id_entry = ctk.CTkEntry(
    left_frame,
    placeholder_text="Enter Student ID",
    width=300
)
id_entry.pack(pady=5)
# Buttons
ctk.CTkButton(
    left_frame,
    text="➕  Add Student",
    width=300,
    fg_color="green",
    command=add_student
).pack(pady=10)
ctk.CTkButton(
    left_frame,
    text="👁️  View Students",
    width=300,
    fg_color="blue",
    command=view_students
).pack(pady=10)
ctk.CTkButton(
    left_frame,
    text="🗑️  Delete Student",
    width=300,
    fg_color="red",
    command=delete_student
).pack(pady=10)
ctk.CTkButton(
    left_frame,
    text="📤  Export Students",
    width=300,
    fg_color="brown",
    command=export_students
).pack(pady=10)
ctk.CTkButton(
    left_frame,
    text="🔍  Search Student",
    width=300,
    fg_color="orange",
    command=search_student
).pack(pady=10)
ctk.CTkButton(
    left_frame,
    text="✏️  Update Student",
    width=300,
    fg_color="purple",
    command=update_student
).pack(pady=10)

def clear_fields():
    name_entry.delete(0, "end")
    age_entry.delete(0, "end")
    course_entry.delete(0, "end")
    id_entry.delete(0, "end")


ctk.CTkButton(
    left_frame,
    text="🧹  Clear Fields",
    width=300,
    fg_color="gray",
    command=clear_fields
).pack(pady=10)

# Right frame title
right_title = ctk.CTkLabel(
    right_frame,
    text="Search and Filters",
    font=("Arial", 22, "bold")
)
right_title.pack(pady=10)

search_entry = ctk.CTkEntry(
    right_frame,
    placeholder_text="Search Student Name",
    width=300
)
search_entry.pack(pady=(10, 20))

print("Program Started")


# Scrollbar
scrollbar = ttk.Scrollbar(right_frame, orient="vertical")
scrollbar.pack(side="right", fill="y", padx=5)

# TABLE STYLE
style = ttk.Style()
style.theme_use("default")

style.configure(
    "Treeview",
    background="#2b2b2b",
    foreground="white",
    rowheight=35,
    fieldbackground="#2b2b2b",
    borderwidth=0
)

style.configure(
    "Treeview.Heading",
    background="#02080a",
    foreground="white",
    font=("Arial", 12, "bold"),
    relief="flat",
    borderwidth=0
)

# ADD THESE LINES HERE
style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
style.map("Treeview.Heading", background=[("active", "#274c6b")])


# Selected row color
style.map(
    "Treeview",
    background=[("selected", "#286391")]
)


# Table
student_table = ttk.Treeview(
    right_frame,
    columns=("ID", "Name", "Age", "Course"),
    show="headings",
    height=12,
    yscrollcommand=scrollbar.set
)

# ADD THESE LINES HERE
student_table.tag_configure("oddrow", background="#f5f5f5")
student_table.tag_configure("evenrow", background="#ffffff")

# Connect scrollbar with table
scrollbar.config(command=student_table.yview)

# Headings
student_table.heading("ID", text="ID")
student_table.heading("Name", text="NAME")
student_table.heading("Age", text="AGE")
student_table.heading("Course", text="COURSE")

# Column sizes
student_table.column("ID", width=80, anchor="center")
student_table.column("Name", width=250, anchor="center")
student_table.column("Age", width=100, anchor="center")
student_table.column("Course", width=250, anchor="center")

# Show table
student_table.pack(fill="both", expand=True, pady=(20, 0))
# Show empty rows initially
for i in range(20):

    if i % 2 == 0:
        student_table.insert(
            "",
            "end",
            values=(" ", " ", " ", " "),
            tags=("evenrow",)
        )
    else:
        student_table.insert(
            "",
            "end",
            values=(" ", " ", " ", " "),
            tags=("oddrow",)
        )

student_table.tag_configure("oddrow", background="#2b2b2b")
student_table.tag_configure("evenrow", background="#353535")

student_table["displaycolumns"] = ("ID", "Name", "Age", "Course")


student_count_label = ctk.CTkLabel(
    app,
    text="Total Students: 0",
    font=("Arial", 14, "bold")
)
student_count_label.place(
    relx=0.5,
    rely=0.97,
    anchor="center"
)
app.mainloop()