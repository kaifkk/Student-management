import json

from src.models.student import Student

DATA_FILE = "data/students.json"

class StudentManager:
    def __init__(self):
        self.data_file = DATA_FILE

        self.students = []
        self.existing_ids = set()
        self.load_from_file()


    def load_from_file(self):
        try:
            with open(self.data_file, "r") as f:
                raw_data = json.load(f)
        except IOError as e:
            print(f"Error: {e}. An I/O error occurred while handling the file '{DATA_FILE}'.")
            return
        except PermissionError as e:
            print(f"Error: {e}. You do not have permission to access the file '{DATA_FILE}'.")
            return
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return

        for record in raw_data:
            student = Student.from_dict(record)
            self.students.append(student)
            self.existing_ids.add(student.id)

    def save_to_file(self):
        try:
            with open(self.data_file, "w") as f:
                data = []
                for student in self.students:
                    data.append(student.to_dict())
                
                json.dump(data, f, indent=4)
            return True
        except IOError as e:
            print(f"Error: {e}. An I/O error occurred while handling the file '{DATA_FILE}'.")
            return
        except PermissionError as e:
            print(f"Error: {e}. You do not have permission to access the file '{DATA_FILE}'.")
            return
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return


    def is_duplicate(self, student_id):
        return student_id in self.existing_ids

    def add_student(self, student_id, name, marks):
        if self.is_duplicate(student_id):
            print("Student ID already exists.")
            return False

        new_student = Student(student_id, name, marks)
        self.students.append(new_student)
        self.existing_ids.add(student_id)
        self.save_to_file()
        return new_student
