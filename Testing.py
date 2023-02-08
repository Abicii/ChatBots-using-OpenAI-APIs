import tkinter as tk

def open_window():
    window = tk.Toplevel(root)
    window.geometry("200x100")
    label = tk.Label(window, text="This is a small text window.")
    label.pack()

root = tk.Tk()

button = tk.Button(root, text="Open Text Window", command=open_window)
button.pack()

root.mainloop()