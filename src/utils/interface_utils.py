import json
import os
from tkinter import messagebox, filedialog
from utils.data_manager import DataManager

class InterfaceUtils:
    def __init__(self):
        self.dm = DataManager()

    def export_data(self):
        try:
            export_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
            if export_path:
                data = self.dm.load_records()
                with open(export_path, "w") as f:
                    json.dump(data, f, indent=4)
                messagebox.showinfo("Export", f"Data exported to {os.path.basename(export_path)}")
        except Exception as e:
            messagebox.showerror("Error", f"Export failed: {e}")

   
    def show_about(self):
        about_text = (
            "🎓 Student Management System\n"
            "Version: 1.0\n"
            "Developed by Team Castaway on the Moon\n"
            "Member 4: Pranto — Data & Utilities\n"
            "Features: Save/Load, Export, Backup, Restore, Reset\n"
        )
        messagebox.showinfo("About", about_text)
