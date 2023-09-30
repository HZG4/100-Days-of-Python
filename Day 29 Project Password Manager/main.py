from tkinter import *
from tkinter import messagebox
import pandas
from password_generator import generate_password
import pyperclip

data = pandas.DataFrame(columns=['Website', 'Email', 'Password'])

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

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(title="Error", message="Do not leave any fields empty.")

    else:
        is_confirm = messagebox.askokcancel(title="Confirm Details", message=f"These are the following details: \n\n\n Website: {website} \n\n Email: {email} \n\n Password: {password}")

        if is_confirm:
            new_data = pandas.DataFrame({'Website': [website], 'Email': [email], 'Password': [password]})
            data = pandas.concat([data, new_data], ignore_index=True)

            string_data = data.to_string()
            with open("passwords.txt", "w") as file:
                file.write(string_data)

            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=60)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=1, columnspan=2)

label_1 = Label(text="Website:")
label_1.grid(column=1, row=2)

label_2 = Label(text="Email/Username:")
label_2.grid(column=1, row=3)

label_3 = Label(text="Password:")
label_3.grid(column=1, row=4)

# Entry
website_entry = Entry(width=40)
website_entry.grid(column=2, row=2, columnspan=2)

email_entry = Entry(width=40)
email_entry.grid(column=2, row=3, columnspan=2)

password_entry = Entry(width=40)
password_entry.grid(column=2, row=4, columnspan=1)

#Button
generate_password_button = Button(width=34, justify="left", text="Generate", command=create_password)
generate_password_button.grid(column=2, row=5, columnspan=1)

add_password = Button(width= 34, text="Add Password", command=add_data)
add_password.grid(column=2, row=6, columnspan=2)

window.mainloop()
