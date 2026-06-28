import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")

        while name == "":
            print("Name cannot be empty!")
            name = input("Enter student name: ")

        age = input("Enter student age: ")

        while not age.isdigit():
            print("Please enter numbers only for age!")
            age = input("Enter student age: ")

        course = input("Enter student course: ")

        while course == "":
            print("Course cannot be empty!")
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

        print("\n===== Student Details =====")
        print("ID | Name | Age | Course")
        print("--------------------------")

        for student in students:
            print(student[0], "|", student[1], "|", student[2], "|", student[3])

    elif choice == "3":
        student_id = input("Enter student ID to update: ")
        name = input("Enter new name: ")
        age = input("Enter new age: ")
        course = input("Enter new course: ")

        cursor.execute(
            "UPDATE students SET name=?, age=?, course=? WHERE id=?",
            (name, age, course, student_id)
        )

        conn.commit()
        print("Student updated successfully!")

    elif choice == "4":
        student_id = input("Enter student ID to delete: ")

        cursor.execute(
            "DELETE FROM students WHERE id=?",
            (student_id,)
        )

        conn.commit()
        print("Student deleted successfully!")

    elif choice == "5":
        search_name = input("Enter student name to search: ")

        cursor.execute(
            "SELECT * FROM students WHERE name LIKE ?",
            ('%' + search_name + '%',)
        )

        students = cursor.fetchall()

        print("\n===== Search Result =====")
        print("ID | Name | Age | Course")
        print("--------------------------")

        for student in students:
            print(student[0], "|", student[1], "|", student[2], "|", student[3])

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice")

conn.close()