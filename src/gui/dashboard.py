from tkinter import Tk, Label, Button, messagebox

from src.managers.student_manager import StudentManager
from src.gui.add_student_page import AddStudentPage


class DashboardApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Result Management & Analyzer")
        self.geometry("420x430")
        self.manager = StudentManager()
        self.build_dashboard()

    def build_dashboard(self):
        Label(self, text="Student Result Management & Analyzer", font=("Arial", 14, "bold")).pack(pady=20)
        self.total_student_label = Label(self, text=f"Total Students: {len(self.manager.students)}")
        self.total_student_label.pack(pady=5)
        Button(self, text="Add Student", command=self.open_add_student).pack(pady=5)
        Button(self, text="View Students", command=self.not_implemented).pack(pady=5)
        Button(self, text="Search Student", command=self.not_implemented).pack(pady=5)
        Button(self, text="Update Student", command=self.not_implemented).pack(pady=5)
        Button(self, text="Delete Student", command=self.not_implemented).pack(pady=5)
        Button(self, text="Statistics", command=self.not_implemented).pack(pady=5)
        Button(self, text="Exit", command=self.destroy).pack(pady=5)

    def update_total_students(self):
        self.total_student_label.config(text=f"Total Students: {len(self.manager.students)}")

    def open_add_student(self):
        self.withdraw()
        AddStudentPage(self, self.manager)
    
    def not_implemented(self):
        messagebox.showinfo("Coming soon", "This feature belongs to another module.")

    def refresh_dashboard(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.build_dashboard()
