import mysql.connector as mql
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage, filedialog, messagebox, END

# strat: make one button "add new show", which will create a new entry which allows you to put a name and episode number
# then, add another function "enter episode" which prompts for the show name and new episode number, and uses alter function to change data in the table
def new_show():
    show_name = e1.get()
    episode_number = e2.get()
    mydb = mql.connect(
            host = "localhost",
            database = "episode_tracker",
            user = "root",
            password = "4JVkrk75Jamd"
            )
    cursor = mydb.cursor()
    sql = "insert into main (show, episode) values(%s, %s)" 
    val = (show_name, episode_number,)
    cursor.execute(sql, val)
    messagebox.showinfo("Info", "Added Show!")

root = tk.Tk()
root.geometry("800x500")
root.title("Episode Tracker")

l1 = tk.Label(root, text = "REGISTRATION FORM", font = ("Times", 14, "bold", "underline")).place(x = 300, y = 5)

l2 = tk.Label(root, text = "Show Name").place(x = 10, y = 50)

e1 = tk.Entry(root)
e1.place(x = 140, y = 50)

l3 = tk.Label(root, text = "Episode #").place(x = 10, y = 90)

e2 = tk.Entry(root)
e2.place(x = 140, y = 90)

b1 = tk.Button(root, text = "New Show", command = new_show, height=1, width=12).place(x = 30, y = 210)


root.mainloop()

