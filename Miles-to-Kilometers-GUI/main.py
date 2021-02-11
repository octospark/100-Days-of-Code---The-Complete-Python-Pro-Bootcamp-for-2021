import tkinter

window = tkinter.Tk()
window.title("Miles to kilometers")
window.minsize(width=300, height=200)
window.config(padx=70, pady=70)


label1 = tkinter.Label(text="Miles")
label1.grid(row=0, column=2)

label2 = tkinter.Label(text="is equal to")
label2.grid(row=1, column=0)

label3 = tkinter.Label(text="Km")
label3.grid(row=1, column=2)

label4 = tkinter.Label(text="0")
label4.grid(row=1, column=1)

entry = tkinter.Entry(width=7)
entry.grid(row=0, column=1)


def calculate_km():
    miles = float(entry.get())
    km = round(miles * 1.609, 2)
    label4["text"] = km


button = tkinter.Button(text="Calculate", command=calculate_km)
button.grid(row=2, column=1)

window.mainloop()