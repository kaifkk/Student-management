from tkinter import Toplevel, Label, Entry, Button, StringVar, messagebox
from src.utils.validator import is_valid_student_id


class DeleteStudentPage(Toplevel):

    def __init__(self, parent, manager):
        super().__init__(parent)
        self.parent = parent
        self.manager = manager
        self.title("Delete Student")
        self.geometry("320x260")
        self.id_var = StringVar()
        self.info_var = StringVar()
        self.build_form()

    def build_form(self):
        Label(self, text="Student ID to delete").pack(pady=10)
        Entry(self, textvariable=self.id_var).pack()

        Button(self, text="Find", command=self.find_student).pack(pady=10)
        Label(self, textvariable=self.info_var, wraplength=280, justify="left").pack(pady=5)

        Button(self, text="Delete", command=self.delete_student).pack(pady=10)
        Button(self, text="Back", command=self.go_back).pack()

    def find_student(self):
        student_id = self.id_var.get().strip()

        if student_id == "":
            messagebox.showerror("Error", "Student ID cannot be empty.")
            return
        
        if not is_valid_student_id(student_id):
            messagebox.showerror("Error", "Student id must be number and -")
            return

        student = self.manager.find_by_id(student_id)

        if student is None:
            self.info_var.set(f"No student with ID '{student_id}'.")
            return

        self.info_var.set(str(student))

    def delete_student(self):
        student_id = self.id_var.get().strip()

        if student_id == "":
            messagebox.showerror("Error", "Student ID cannot be empty.")
            return

        confirmed = messagebox.askyesno("Confirm Delete", f"Delete student with ID '{student_id}'? This cannot be undone.")
        if not confirmed:
            return

        deleted = self.manager.delete_student(student_id)

        if deleted == False:
            messagebox.showerror("Error", f"No student with ID '{student_id}'.")
            return

        messagebox.showinfo("Deleted", f"Student '{student_id}' was deleted.")
        self.id_var.set("")
        self.info_var.set("")
        self.parent.update_total_students()

    def go_back(self):
        self.parent.deiconify()
        self.destroy()
