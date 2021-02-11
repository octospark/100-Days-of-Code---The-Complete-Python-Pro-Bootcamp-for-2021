import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(500, 300)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)


# Button
def button_clicked():
    my_label["text"] = entry.get()


button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

button2 = tkinter.Button(text="Click Me", command=button_clicked)
button2.grid(row=0, column=2)

# Entry
entry = tkinter.Entry(width=10)
entry.grid(row=2, column=3)










window.mainloop()