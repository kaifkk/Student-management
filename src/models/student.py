from numpy import sum, mean
from src.models.config import SUBJECTS, GRADE_TABLE


class Student:

    def __init__(self, student_id, name, marks):
        self.id = student_id
        self.name = name
        self.marks = marks

        self.total = self.calculate_total()
        self.percentage = self.calculate_percentage()
        self.grade = self.calculate_grade()
        self.status = self.calculate_status()

    def calculate_total(self):
        return int(sum(self.marks))

    def calculate_percentage(self):
        return round(float(mean(self.marks)), 2)

    def calculate_grade(self):
        for key in sorted(GRADE_TABLE, reverse=True):
            if self.percentage >= key:
                return GRADE_TABLE[key]
        return "F"

    def calculate_status(self):
        if self.percentage < 33:
            return "Fail"

        for mark in self.marks:
            if mark < 33:
                return "Fail"

        return "Pass"

    def to_dict(self):
        marks = {}

        for i in range(len(SUBJECTS)):
            marks[SUBJECTS[i]] = self.marks[i]

        return {
            "id": self.id,
            "name": self.name,
            "marks": marks,
            "total": self.total,
            "percentage": self.percentage,
            "grade": self.grade,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        marks = []

        for subject in SUBJECTS:
            marks.append(data["marks"][subject])

        return cls(
            data["id"],
            data["name"],
            marks
        )

    def __str__(self):
        return (
            f"{self.id} | "
            f"{self.name} | "
            f"{self.total} | "
            f"{self.percentage}% | "
            f"{self.grade} | "
            f"{self.status}"
        )