import json
import os
import shutil
from tkinter import messagebox

class DataManager:
    def __init__(self, filename="data/students.json"):
        self.filename = filename

  
    def save_records(self, records):
        try:
            with open(self.filename, "w") as f:
                json.dump(records, f, indent=4)
            messagebox.showinfo("Success", "Records saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save records: {e}")

    def load_records(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, "r") as f:
                    return json.load(f)
            else:
                return []
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load records: {e}")
            return []

   
    def create_sample_data(self):
        sample = [
            {"id": "101", "name": "Rahim", "marks": [80, 75, 90]},
            {"id": "102", "name": "Karim", "marks": [60, 65, 70]},
        ]
        self.save_records(sample)
        messagebox.showinfo("Info", "Sample data created!")

   
    def reset_data(self):
        self.save_records([])
        messagebox.showinfo("Info", "All records reset!")


    def backup_data(self, backup_file="data/backup.json"):
        try:
            shutil.copy(self.filename, backup_file)
            messagebox.showinfo("Success", "Backup created!")
        except Exception as e:
            messagebox.showerror("Error", f"Backup failed: {e}")


    def restore_data(self, backup_file="data/backup.json"):
        try:
            shutil.copy(backup_file, self.filename)
            messagebox.showinfo("Success", "Data restored!")
        except Exception as e:
            messagebox.showerror("Error", f"Restore failed: {e}")
