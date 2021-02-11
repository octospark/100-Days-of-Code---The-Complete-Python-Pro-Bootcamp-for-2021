import tkinter
import tkinter.messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # Easy Level - Order not randomised:
    # e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    password_list = []
    password_list += [random.choice(letters) for i in range(nr_letters)]
    password_list += [random.choice(numbers) for i in range(nr_numbers)]
    password_list += [random.choice(symbols) for i in range(nr_symbols)]
    random.shuffle(password_list)
    password = ''.join(password_list)

    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(password) == 0 or len(website) == 0:
        tkinter.messagebox.showinfo(title="Ooops", message="Please don't leave any of the fields empty.")
    else:

        try:
            with open("data.json", 'r') as file:
                data = json.load(file)

        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open("data.json", 'w') as file:
                json.dump(new_data, file, indent=4)

        else:
            data.update(new_data)
            with open("data.json", 'w') as file:
                json.dump(data, file, indent=4)
            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)


# ---------------------------- SEARCH DATA ------------------------------- #

def search_data():
    try:
        with open("data.json", 'r') as data_file:
            dictionary = json.load(data_file)
            website = dictionary.get(website_entry.get())
        if website:
            email = website["email"]
            password = website["password"]
            tkinter.messagebox.showinfo(title=website_entry.get(),
                                        message=f"The credentials for this website are: \n"
                                                f"E-mail:{email}\nPassword: {password}")
        else:
            tkinter.messagebox.showinfo(title="Not found", message="No credentials for this website found")
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        tkinter.messagebox.showinfo(title="Ooops", message="The item or you looked or the file does not exist")


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.configure(padx=20, pady=20)
bg_img = tkinter.PhotoImage(file="logo.png")
canvas = tkinter.Canvas(width=200, height=200)
canvas.create_image(100, 95, image=bg_img)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = tkinter.Entry(width=34)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = tkinter.Entry(width=53)
email_entry.insert(0, "erling@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = tkinter.Entry(width=34)
password_entry.grid(row=3, column=1)

search_button = tkinter.Button(text="Search", command=search_data, padx=35)
search_button.grid(row=1, column=2)

generate_password_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=45, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
