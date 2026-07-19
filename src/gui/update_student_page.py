from tkinter import Toplevel, Label, Entry, Button, StringVar, messagebox
from src.models.config import SUBJECTS


class UpdateStudentPage(Toplevel):

    def __init__(self, parent, manager):
        super().__init__(parent)
        self.parent = parent
        self.manager = manager
        self.title("Update Student")
        self.geometry("320x460")
        self.id_var = StringVar()
        self.name_var = StringVar()
        self.mark_var = []
        for subject in SUBJECTS:
            self.mark_var.append(StringVar())
        self.build_load_form()

    def build_load_form(self):

        Label(self, text="Student ID to update").pack(pady=10)
        Entry(self, textvariable=self.id_var).pack()

        Button(self, text="Load", command=self.load_student).pack(pady=10)
        Button(self, text="Back", command=self.go_back).pack()

    def load_student(self):
        student_id = self.id_var.get().strip()

        if student_id == "":
            messagebox.showerror("Error", "Student ID cannot be empty.")
            return

        student = self.manager.find_by_id(student_id)

        if student is None:
            messagebox.showerror("Error", f"No student with ID '{student_id}'.")
            return

        self.name_var.set(student.name)
        for i in range(len(SUBJECTS)):
            self.mark_var[i].set(student.marks[i])

        self.build_edit_form()

    def build_edit_form(self):
        for widget in self.winfo_children():
            widget.destroy()

        Label(self, text=f"Editing ID {self.id_var.get()}", font=("Arial", 12, "bold")).pack(pady=10)

        Label(self, text="Name").pack()
        Entry(self, textvariable=self.name_var).pack()

        for i in range(len(SUBJECTS)):
            Label(self, text=SUBJECTS[i]).pack()
            Entry(self, textvariable=self.mark_var[i]).pack()

        Button(self, text="Save Changes", command=self.save_student).pack(pady=15)
        Button(self, text="Back", command=self.go_back).pack()

    def save_student(self):
        student_id = self.id_var.get().strip()
        name = self.name_var.get().strip()

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

        updated_student = self.manager.update_student(student_id, name, marks)

        if updated_student == False:
            messagebox.showerror("Error", "Student record no longer exists.")
            return

        messagebox.showinfo(
            "Success",
            f"{updated_student.name} updated.\n"
            f"Total: {updated_student.total}  "
            f"Percentage: {updated_student.percentage}%  "
            f"Grade: {updated_student.grade}  "
            f"Status: {updated_student.status}"
        )


    def go_back(self):
        self.parent.update_total_students()
        self.parent.deiconify()
        self.destroy()
