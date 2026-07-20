from tkinter import Toplevel, Label, Button, messagebox, filedialog
from tkinter.ttk import Treeview
import numpy as np

from src.models.config import SUBJECTS



class ResultAnalyzer:
    """
    StudentManager theke shob student er object/list niye puro class er
    statistics calculate kora hoy. Ekhane prottek student er 
    id, name, marks (subject onujayi), total, percentage, grade, ar status use kore 
    bibhinno statistical analysis kora hoise. 
    Ekhane overall class average, highest/lowest total, median, std deviation,
    """
    
    def __init__(self, students):
        self.students = students

    def _totals(self):
        if not self.students:
            raise ValueError("Kono student er tothyo pawa jaini.")
        return np.array([s.total for s in self.students], dtype=float)

    def class_average(self):
        return float(np.mean(self._totals()))

    def highest_total(self):
        return float(np.max(self._totals()))

    def lowest_total(self):
        return float(np.min(self._totals()))

    def median_total(self):
        return float(np.median(self._totals()))

    def std_dev(self):
        return float(np.std(self._totals()))

    def pass_fail_count(self):
        pass_koreche = sum(1 for s in self.students if s.status == "Pass")
        fail_koreche = len(self.students) - pass_koreche
        return {"Pass": pass_koreche, "Fail": fail_koreche}

    def subject_wise_average(self):
        result = {}                          # Dictionary use kora hoyeche
        for i in range(len(SUBJECTS)):
            marks = np.array([s.marks[i] for s in self.students], dtype=float)
            result[SUBJECTS[i]] = float(np.mean(marks)) if len(marks) else 0.0
        return result

    #                    grade distribution
    
    def unique_grades(self):
        return {s.grade for s in self.students}  # Set use kora hoyeche

    def grade_distribution(self):
        grades = {}                   # Dictionary use kora hoyeche
        for g in self.unique_grades():
            grades[g] = sum(1 for s in self.students if s.grade == g)
        return grades

    def topper(self):
        return max(self.students, key=lambda s: s.percentage)

    def lowest_performer(self):
        return min(self.students, key=lambda s: s.percentage)

    #             Overall summary
    
    def full_summary(self):
        return {
            "total_students": len(self.students),
            "class_average": round(self.class_average(), 2),
            "highest_total": self.highest_total(),
            "lowest_total": self.lowest_total(),
            "median_total": self.median_total(),
            "std_dev": round(self.std_dev(), 2),
            "pass_fail": self.pass_fail_count(),
            "subject_avg": self.subject_wise_average(),
            "grade_dist": self.grade_distribution(),
            "topper": self.topper(),
            "lowest_performer": self.lowest_performer(),
        }

class StatisticsPage(Toplevel):
    
    """ViewStudentsPage o SearchStudentPage er moto same niyom mene banano."""

    def __init__(self, parent, manager):
        super().__init__(parent)
        self.parent = parent
        self.manager = manager
        self.title("Class Statistics")
        self.geometry("560x640")
        self.summary = None
        self.build_page()
        
    def build_page(self):
        Label(self, text="Class Statistics", font=("Arial", 14, "bold")).pack(pady=10)

        if len(self.manager.students) == 0:   # Kono student na thakle empty message dekhabe
            Label(self, text="Ekhono kono student er record nei.").pack(pady=20)
            Button(self, text="Back", command=self.go_back).pack(pady=10)
            return

        try:
            analyzer = ResultAnalyzer(self.manager.students)
            self.summary = analyzer.full_summary()
        except ValueError as e:
            # Exception handling: khali list hole error dekhabe, crash korbe na
            Label(self, text=str(e)).pack(pady=20)
            Button(self, text="Back", command=self.go_back).pack(pady=10)
            return
          
        summary = self.summary
        stats_text = (
            f"Total Students: {summary['total_students']}\n"
            f"Class Average (Total marks): {summary['class_average']}\n"
            f"Highest Total: {summary['highest_total']}\n"
            f"Lowest Total: {summary['lowest_total']}\n"
            f"Median Total: {summary['median_total']}\n"
            f"Std Deviation: {summary['std_dev']}\n"
            f"Pass: {summary['pass_fail']['Pass']}   |   Fail: {summary['pass_fail']['Fail']}\n"
            f"Topper: {summary['topper'].name} ({summary['topper'].percentage}%)\n"
            f"Lowest: {summary['lowest_performer'].name} ({summary['lowest_performer'].percentage}%)"
        )
        Label(self, text=stats_text, justify="left", font=("Arial", 11)).pack(pady=10)

        # subject er table
        
        Label(self, text="Subject-wise Average", font=("Arial", 12, "bold")).pack(pady=(10, 5))
        subj_table = Treeview(self, columns=("Subject", "Average"), show="headings", height=6)
        subj_table.heading("Subject", text="Subject")
        subj_table.heading("Average", text="Average")
        for subject, avg in summary["subject_avg"].items():
            subj_table.insert("", "end", values=(subject, round(avg, 2)))
        subj_table.pack(pady=5)
         
       # ei table e grade distribution dekhabe
       
        Label(self, text="Grade Distribution", font=("Arial", 12, "bold")).pack(pady=(10, 5))
        grade_table = Treeview(self, columns=("Grade", "Count"), show="headings", height=6)
        grade_table.heading("Grade", text="Grade")
        grade_table.heading("Count", text="Count")
        for grade, count in summary["grade_dist"].items():
            grade_table.insert("", "end", values=(grade, count))
        grade_table.pack(pady=5)

        Button(self, text="Export Report (.txt)", command=self.export_report).pack(pady=5)
        Button(self, text="Back", command=self.go_back).pack(pady=10)        