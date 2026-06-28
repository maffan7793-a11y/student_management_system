import os
import sys
from tkinter import messagebox
import tkinter as tk

username = "affan"
password = "2006"

print("===== Admin Login =====")

user = input("Enter username: ")
pwd = input("Enter password: ")

if user == username and pwd == password:
    print("Welcome, Admin!")
    root = tk.Tk()
    root.withdraw()

    messagebox.showinfo(
        "Welcome",
        "Welcome, Admin!\nLogin Successful!"
    )

    root.destroy()
    import subprocess
    import os

    gui_path = os.path.join(
        os.path.dirname(sys.executable),
        "modern_gui.exe"
)

    subprocess.Popen([gui_path])
else:
    print("Invalid username or password")