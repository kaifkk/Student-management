from tkinter import Tk, Label, Button, messagebox

from src.managers.student_manager import StudentManager
from src.gui.add_student_page import AddStudentPage
from src.gui.view_student_page import ViewStudentsPage
from src.gui.search_student_page import SearchStudentPage
from src.gui.update_student_page import UpdateStudentPage
from src.gui.delete_student_page import DeleteStudentPage
from src.gui.statistics_page import StatisticsPage


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
        Button(self, text="View Students", command=self.open_view_students).pack(pady=5)
        Button(self, text="Search Student", command=self.open_search_student).pack(pady=5)
        Button(self, text="Update Student", command=self.open_update_student).pack(pady=5)
        Button(self, text="Delete Student", command=self.open_delete_student).pack(pady=5)
        Button(self, text="Statistics", command=self.open_statistics).pack(pady=5)
        Button(self, text="Exit", command=self.destroy).pack(pady=5)

    def update_total_students(self):
        self.total_student_label.config(text=f"Total Students: {len(self.manager.students)}")

    def open_add_student(self):
        self.withdraw()
        AddStudentPage(self, self.manager)

    def open_view_students(self):
        self.withdraw()
        ViewStudentsPage(self, self.manager)

    def open_search_student(self):
        self.withdraw()
        SearchStudentPage(self, self.manager)

    def open_update_student(self):
        self.withdraw()
        UpdateStudentPage(self, self.manager)

    def open_delete_student(self):
        self.withdraw()
        DeleteStudentPage(self, self.manager)

    def open_statistics(self):
        self.withdraw()
        StatisticsPage(self, self.manager)

    def not_implemented(self):
        messagebox.showinfo("Coming soon", "This feature belongs to another module.")

    def refresh_dashboard(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.build_dashboard()
