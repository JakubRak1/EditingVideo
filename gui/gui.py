import tkinter as tk

def run_gui():
    # Your GUI code here
    root = tk.Tk()
    label = tk.Label(root, text="Hello, GUI!")
    label.pack()
    root.mainloop()