from tkinter import *
from tkcalendar import *
from datetime import datetime as dt
import requests
import webbrowser
from tkinter import messagebox
from dotenv import load_dotenv
import os

load_dotenv(".env")

USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("TOKEN")
GRAPH_ID = os.getenv("GRAPH_ID")

headers = {
    "X-USER-TOKEN": TOKEN
}

root = Tk()
root.config(bg="Powder Blue")
root.title("Python Journey")

root.resizable(width=False, height=False)
root.config(pady=20, padx=20)
URL = F"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}.html"
TODAY = dt.now()

def open_browser():
    webbrowser.open(URL, new=1)


def format_date():
    cal.config(date_pattern="yyyyMMdd")
    date = cal.get_date()
    cal.config(date_pattern="dd/MM/yyyy")
    return date


def add_pixel():
    global GRAPH_ID, USERNAME
    endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/"
    pixel_add = {
        "date": format_date(),
        "quantity": user_in.get(),
    }
    requests.post(url=endpoint, json=pixel_add, headers=headers)
    user_in.delete(0, END)
    messagebox.showinfo(message="Progress added.")

def del_pixel():
    global GRAPH_ID, USERNAME
    endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{format_date()}"
    requests.delete(url=endpoint, headers=headers)
    messagebox.showinfo(message="Progress deleted.")

def change_pixel():
    global GRAPH_ID, USERNAME
    endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{format_date()}"
    pixel_update = {
        "quantity": user_in.get(),
    }
    requests.put(url=endpoint, json=pixel_update, headers=headers)
    user_in.delete(0, END)
    messagebox.showinfo(message="Pixel updated.")


cal = Calendar(root, selectmode="day", year=TODAY.year, month=TODAY.month, day=TODAY.day)
cal.grid(row=0, column=0, columnspan=4)
units = Label(text="Hours/Day:")
units.grid(row=1, column=0, columnspan=2, pady=10, sticky="e")
user_in = Entry(width=10)
user_in.grid(row=1, column=2, sticky="w")

add = Button(text="Add", command=add_pixel)
add.grid(row=2, column=0, pady=10)
update = Button(text="Update", command=change_pixel)
update.grid(row=2, column=1, pady=10, sticky="w")
delete = Button(text="Delete", command=del_pixel)
delete.grid(row=2, column=2, pady=10, sticky="w")
link = Button(text="Show\nJourney", command=open_browser)
link.grid(row=2, column=3)

root.mainloop()