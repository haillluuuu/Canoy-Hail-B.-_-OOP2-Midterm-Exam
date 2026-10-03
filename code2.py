import tkinter as tk


def display_fullname():
    fullname = entry1.get()
    entry2.delete(0, tk.END)
    entry2.insert(0, fullname)


window = tk.Tk()
window.title("Midterm in OOP")
window.geometry("900x500")

label = tk.Label(
    window,
    text="Enter your fullname:",
    fg="red"
)
label.place(x=100, y=150)

entry1 = tk.Entry(window, width=35, font=("Arial", 18))
entry1.place(x=500, y=140)

button = tk.Button(
    window,
    text="Click to display your Fullname",
    fg="red",
    command=display_fullname
)
button.place(x=100, y=220)

entry2 = tk.Entry(window, width=35, font=("Arial", 18))
entry2.place(x=500, y=220)

window.mainloop()
