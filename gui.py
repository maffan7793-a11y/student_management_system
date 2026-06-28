import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3
def add_student():
    name = name_entry.get()
    age = age_entry.get()
    course = course_entry.get()
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", (name, age, course))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Student saved successfully!")
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    messagebox.showinfo(
        "Student Added",
        f"Name: {name}\nAge: {age}\nCourse: {course}"
    )
def view_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    conn.close()

    for row in student_table.get_children():
        student_table.delete(row)

    for student in students:
        student_table.insert("", tk.END, values=student)
window = tk.Tk()
window.title("Student Management System")
window.geometry("1000x750")
window.resizable(True, True)
window.configure(bg="lightblue")
def delete_student():
    student_id = id_entry.get()

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Student deleted successfully!")

    id_entry.delete(0, tk.END)
def search_student():
    search_name = search_entry.get()

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE name LIKE ?",
        ('%' + search_name + '%',)
    )

    students = cursor.fetchall()
    conn.close()

    for row in student_table.get_children():
        student_table.delete(row)

    for student in students:
        student_table.insert("", tk.END, values=student)
def update_student():
    student_id = id_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    course = course_entry.get()

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE students SET name=?, age=?, course=? WHERE id=?",
        (name, age, course, student_id)
    )

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Student updated successfully!")

    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)

window.title("Student Management System")
window.geometry("400x300")

title_label = tk.Label(
    window,
    text="Student Management System",
    font=("Arial", 18, "bold"),
    bg="lightblue"
)

title_label.pack(pady=20)
tk.Label(
    window,
    text="Name",
    font=("Arial", 12, "bold"),
    bg="lightblue"
).pack()
name_entry = tk.Entry(
    window,
    width=30,
    font=("Arial", 12)
)
name_entry.pack(pady=5) 

tk.Label(
    window,
    text="Age",
    font=("Arial", 12, "bold"),
    bg="lightblue"
).pack()
age_entry = tk.Entry(
    window,
    width=30,
    font=("Arial", 12)
)
age_entry.pack(pady=5)

tk.Label(
    window,
    text="Course",
    font=("Arial", 12, "bold"),
    bg="lightblue"
).pack()
course_entry = tk.Entry(window, width=30)
course_entry.pack(pady=5)
tk.Label(
    window,
    text="Student ID",
    font=("Arial", 12, "bold"),
    bg="lightblue"
).pack()
id_entry = tk.Entry(window, width=30)
id_entry.pack(pady=5)
tk.Label(
    window,
    text="Search Student Name",
    font=("Arial", 12, "bold"),
    bg="lightblue"
).pack()
search_entry = tk.Entry(window, width=30)
search_entry.pack(pady=5)
tk.Button(
    window,
    text="Add Student",
    command=add_student,
    font=("Arial", 12, "bold"),
    width=20,
    bg="green",
    fg="white"
).pack(pady=10)
tk.Button(
    window,
    text="View Students",
    command=view_students,
    font=("Arial", 12, "bold"),
    width=20,
    bg="blue",
    fg="white"
).pack(pady=10)
tk.Button(
    window,
    text="Delete Student",
    command=delete_student,
    font=("Arial", 12, "bold"),
    width=20,
    bg="red",
    fg="white"
).pack(pady=10)
tk.Button(
    window,
    text="Search Student",
    command=search_student,
    font=("Arial", 12, "bold"),
    width=20,
    bg="orange",
    fg="white"
).pack(pady=10)
tk.Button(
    window,
    text="Update Student",
    command=update_student,
    font=("Arial", 12, "bold"),
    width=20,
    bg="purple",
    fg="white"
).pack(pady=10)
student_table = ttk.Treeview(
    window,
    columns=("ID", "Name", "Age", "Course"),
    show="headings"
)
style = ttk.Style()

style.configure(
    "Treeview",
    font=("Arial", 11),
    rowheight=30
)

style.configure(
    "Treeview.Heading",
    font=("Arial", 12, "bold")
)

student_table.heading("ID", text="ID")
student_table.heading("Name", text="Name")
student_table.heading("Age", text="Age")
student_table.heading("Course", text="Course")
student_table.column("ID", width=50)
student_table.column("Name", width=150)
student_table.column("Age", width=100)
student_table.column("Course", width=250)
scrollbar = tk.Scrollbar(window, orient="vertical",
                         command=student_table.yview)

student_table.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
student_table.pack(pady=20, fill="both", expand=True)
window.mainloop()