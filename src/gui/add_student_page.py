from tkinter import Toplevel, Label, Entry, Button, StringVar, messagebox
from src.models.config import SUBJECTS
from src.utils.validator import is_valid_student_id


class AddStudentPage(Toplevel):

    def __init__(self, parent, manager):
        super().__init__(parent)
        self.parent = parent
        self.manager = manager
        self.title("Add Student")
        self.geometry("320x430")
        self.id_var = StringVar()
        self.name_var = StringVar()
        self.mark_var = []
        for subject in SUBJECTS:
            self.mark_var.append(StringVar())
        self.build_form()

    def build_form(self):
        Label(self, text="Student ID").pack()
        Entry(self, textvariable=self.id_var).pack()

        Label(self, text="Name").pack()
        Entry(self, textvariable=self.name_var).pack()

        for i in range(len(SUBJECTS)):
            Label(self, text=SUBJECTS[i]).pack()
            Entry(self, textvariable=self.mark_var[i]).pack()

        Button(self, text="Save Student", command=self.save_student).pack(pady=15)
        Button(self, text="Back", command=self.go_back).pack()

    def save_student(self):
        student_id = self.id_var.get().strip()
        name = self.name_var.get().strip()

        if student_id == "":
            messagebox.showerror("Error", "Student ID cannot be empty.")
            return
        
        if not is_valid_student_id(student_id):
            messagebox.showerror("Error", "Student id must be number and -")
            return

        if name == "":
            messagebox.showerror("Error", "Student Name cannot be empty.")
            return

        marks = []
        for i in range(len(SUBJECTS)):
            value = self.mark_var[i].get().strip()

            if value == "":
                    messagebox.showerror("Error", f"{SUBJECTS[i]} mark must not be empty.")
                    return

            try:
                mark = float(value)
            except ValueError:
                messagebox.showerror("Error", f"{SUBJECTS[i]} mark must be a number.")
                return
            
            if mark < 0 or mark > 100:
                messagebox.showerror("Error", f"{SUBJECTS[i]} mark must be between 0 and 100")
                return
            marks.append(mark)
        
        new_student = self.manager.add_student(student_id, name, marks)
        
        if new_student == False:
            messagebox.showerror("Error", "Student ID already exists")
            return
        
        messagebox.showinfo(
            "Success",
            f"{new_student.name} added.\n"
            f"Total: {new_student.total}  "
            f"Percentage: {new_student.percentage}%  "
            f"Grade: {new_student.grade}  "
            f"Status: {new_student.status}"
        )

        self.id_var.set("")
        self.name_var.set("")

        for mark in self.mark_var:
            mark.set("")

    def go_back(self):
        self.parent.update_total_students()
        self.parent.deiconify()
        self.destroy()