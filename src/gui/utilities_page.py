import tkinter as tk
from tkinter import messagebox, filedialog
from utils.data_manager import DataManager
import json
import os

class UtilitiesPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Data & System Utilities")
        self.dm = DataManager()

        tk.Label(root, text="📁 Data & System Utilities", font=("Arial", 16, "bold")).pack(pady=10)

        # Buttons
        tk.Button(root, text="Save Records", width=20, command=lambda: self.dm.save_records([])).pack(pady=5)
        tk.Button(root, text="Load Records", width=20, command=self.load_records).pack(pady=5)
        tk.Button(root, text="Export Data (JSON)", width=20, command=self.export_data).pack(pady=5)
        tk.Button(root, text="Settings / About", width=20, command=self.show_about).pack(pady=5)
        tk.Button(root, text="Reset Data", width=20, command=self.dm.reset_data).pack(pady=5)
        tk.Button(root, text="Backup Data", width=20, command=self.dm.backup_data).pack(pady=5)
        tk.Button(root, text="Restore Data", width=20, command=self.dm.restore_data).pack(pady=5)

    def load_records(self):
        records = self.dm.load_records()
        messagebox.showinfo("Loaded", f"{len(records)} records loaded successfully!")

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

if __name__ == "__main__":
    root = tk.Tk()
    app = UtilitiesPage(root)
    root.mainloop()
