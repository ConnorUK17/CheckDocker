import tkinter as tk

root = tk.Tk()

root.geometry("800x500")

root.title("Resource Value")

label = tk.Label(root, text="Recource Monitor", font=("Times New Roman", 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, font="Arial, 10")

myentry = tk.Entry(root)
myentry.pack()

Button = tk.Button(root, text="Login", font=("Times New Roman", 10))
Button.pack(padx=10, pady=10)

root.mainloop()