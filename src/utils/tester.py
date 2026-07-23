from tkinter import messagebox
from utils.data_manager import DataManager

class Tester:
    def __init__(self):
        self.dm = DataManager()

    def test_system(self):
        try:
            records = self.dm.load_records()
            if isinstance(records, list):
                messagebox.showinfo("Test Result", f"System OK. {len(records)} records loaded.")
            else:
                messagebox.showwarning("Test Result", "System check failed!")
        except Exception as e:
            messagebox.showerror("Error", f"Testing failed: {e}")
