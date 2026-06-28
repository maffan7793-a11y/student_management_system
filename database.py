import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

print("===== Student Management System =====")
print("1. Add Student")
print("2. View Student")
print("3. Delete Student")
print("4. Exit")

choice = input("Enter your choice: ")

if choice == "1":
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    course = input("Enter student course: ")

    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )

    conn.commit()
    print("Student added successfully!")

elif choice == "2":
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    print("\nStudent Details:")
    for student in students:
        print(student)

elif choice == "3":
    student_id = input("Enter student ID to delete: ")

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )

    conn.commit()
    print("Student deleted successfully!")

elif choice == "4":
    print("Thank you!")

else:
    print("Invalid choice")

conn.close()