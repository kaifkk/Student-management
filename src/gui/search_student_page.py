from tkinter import Toplevel, Label, Entry, Button, StringVar, messagebox
from tkinter.ttk import Treeview
from src.models.config import TABLE_HEADINGS


class SearchStudentPage(Toplevel):

    def __init__(self, parent, manager):
        super().__init__(parent)
        self.parent = parent
        self.manager = manager
        self.title("Search Student")
        self.geometry("560x420")
        self.query_var = StringVar()
        self.build_page()

    def build_page(self):
        Label(self, text="Search by ID or Name").pack(pady=10)
        Entry(self, textvariable=self.query_var, width=30).pack()

        Button(self, text="Search by ID", command=self.search_by_id).pack(pady=5)
        Button(self, text="Search by Name", command=self.search_by_name).pack()

        self.table = Treeview(self, columns=TABLE_HEADINGS, show="headings")
        for heading in TABLE_HEADINGS:
            self.table.heading(heading, text=heading)
            self.table.column(heading, width=90)
        self.table.pack(padx=10, pady=10, fill="both", expand=True)

        Button(self, text="Back", command=self.go_back).pack(pady=5)

    def show_results(self, results):
        for row in self.table.get_children():
            self.table.delete(row)

        for student in results:
            self.table.insert("", "end", values=(
                student.id,
                student.name,
                student.total,
                student.percentage,
                student.grade,
                student.status
            ))

    def search_by_id(self):
        student_id = self.query_var.get().strip()

        if student_id == "":
            messagebox.showerror("Error", "Enter a Student ID to search.")
            return

        student = self.manager.find_by_id(student_id)

        if student is None:
            messagebox.showinfo("Not Found", f"No student with ID '{student_id}'.")
            self.show_results([])
            return

        self.show_results([student])

    def search_by_name(self):
        name = self.query_var.get().strip()

        if name == "":
            messagebox.showerror("Error", "Enter a name to search.")
            return

        results = self.manager.find_by_name(name)

        if len(results) == 0:
            messagebox.showinfo("Not Found", f"No student matching '{name}'.")

        self.show_results(results)

    def go_back(self):
        self.parent.deiconify()
        self.destroy()
