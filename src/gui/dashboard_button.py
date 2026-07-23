from gui.utilities_page import UtilitiesPage

tk.Button(root, text="Open Utilities", command=lambda: UtilitiesPage(tk.Toplevel(root))).pack(pady=5)
