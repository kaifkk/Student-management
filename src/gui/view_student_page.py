from tkinter import Toplevel, Label, Button
from tkinter.ttk import Treeview
from numpy import mean, max, min
from src.models.config import TABLE_HEADINGS


class ViewStudentsPage(Toplevel):

    def __init__(self, parent, manager):
        super().__init__(parent)
        self.parent = parent
        self.manager = manager
        self.title("View Students")
        self.geometry("560x400")
        self.build_page()

    def build_page(self):
        Label(self, text="All Students", font=("Arial", 14, "bold")).pack(pady=10)

        self.summary_label = Label(self, font=("Arial", 10))
        self.summary_label.pack(pady=5)

        self.table = Treeview(self, columns=TABLE_HEADINGS, show="headings")
        for heading in TABLE_HEADINGS:
            self.table.heading(heading, text=heading)
            self.table.column(heading, width=90)
        self.table.pack(padx=10, pady=10, fill="both", expand=True)

        Button(self, text="Refresh", command=self.refresh_table).pack(pady=5)
        Button(self, text="Back", command=self.go_back).pack()

        self.refresh_table()

    def refresh_table(self):
        for row in self.table.get_children():
            self.table.delete(row)

        for student in self.manager.students:
            self.table.insert("", "end", values=(
                student.id,
                student.name,
                student.total,
                f"{student.percentage:.2f}",
                student.grade,
                student.status
            ))

        total_students = len(self.manager.students)

        if total_students > 0:
            percentages = [student.percentage for student in self.manager.students]

            average_percentage = mean(percentages)
            highest_percentage = max(percentages)
            lowest_percentage = min(percentages)

            self.summary_label.config(
                text=(
                    f"Total Students: {total_students}    |    "
                    f"Average Percentage: {average_percentage:.2f}%    |    "
                    f"Highest Percentage: {highest_percentage:.2f}%    |    "
                    f"Lowest Percentage: {lowest_percentage:.2f}%"
                )
            )
        else:
            self.summary_label.config(
                text=(
                    "Total Students: 0    |    "
                    "Average Percentage: 0.00%    |    "
                    "Highest Percentage: 0.00%    |    "
                    "Lowest Percentage: 0.00%"
                )
            )

    def go_back(self):
        self.parent.deiconify()
        self.destroy()