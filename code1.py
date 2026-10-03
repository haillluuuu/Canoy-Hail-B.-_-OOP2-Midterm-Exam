import tkinter as tk


def change_color():
    button.config(bg="yellow")


window = tk.Tk()
window.title("Special Midterm Exam in OOP")
window.geometry("600x500")

button = tk.Button(
    window,
    text="Click to Change Color",
    command=change_color
)

button.place(relx=0.5, rely=0.5, anchor="center")

window.mainloop()
