from tkinter import messagebox

class ErrorHandler:
    @staticmethod
    def show_error(msg):
        messagebox.showerror("Error", msg)

    @staticmethod
    def show_warning(msg):
        messagebox.showwarning("Warning", msg)

    @staticmethod
    def show_info(msg):
        messagebox.showinfo("Info", msg)
