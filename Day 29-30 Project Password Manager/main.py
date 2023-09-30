from tkinter import *
from tkinter import messagebox
import json
from password_generator import generate_password
import pyperclip


# ------------------------ PASSWORD GENERATOR --------------------------#
def search_password():
    website_name = (website_entry.get())
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            if website_name in data:
                messagebox.showinfo(title=f"{website_name} Info ", message=f" Email: {data[website_name]['email']} \n\n Password: {data[website_name]['password']}")
            else:
                messagebox.showinfo(title="Search Error", message="Website Not Found")

    except FileNotFoundError:
        with open("data.json", "w") as file:
            json.dump({}, file)
            messagebox.showinfo(title="Search Error", message="Website Not Found")

# ------------------------ PASSWORD GENERATOR --------------------------#
def create_password():
    password = generate_password()
    password_entry.insert(END, f"{password}")
    pyperclip.copy(password)

# -------------------------- SAVE PASSWORD ---------------------------- #
def add_data():
    global data
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_dict = {website : {"email" : email,
                           "password" : password}}

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(title="Error", message="Do not leave any fields empty.")

    else:
        is_confirm = messagebox.askokcancel(title="Confirm Details", message=f"These are the following details: \n\n\n Website: {website} \n\n Email: {email} \n\n Password: {password}")
        if is_confirm:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_dict, file, indent=4)
            else:
                data.update(new_dict)
                with open("data.json", "w")as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=60, pady=60)

canvas = Canvas(width=200, height=200)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

label_email_uname = Label(text="Email/Username:")
label_email_uname.grid(column=0, row=2)

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")

email_entry = Entry()
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")

search_btn = Button(text="Search Password", command=search_password)
search_btn.grid(column=2, row=1, sticky="EW")

generate_btn = Button(text="Generate Password", command=create_password)
generate_btn.grid(column=2, row=3, sticky="EW")

add_btn = Button(text="Add Password", width=35, command=add_data)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()