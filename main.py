from tkinter import *
from tkinter import ttk
from datetime import date, timedelta, datetime
import pickle
from tkcalendar import Calendar

all_tasks = []
to_do_tasks = []


class Task:
    done = False

    def __init__(self, content, date):
        self.content = content
        self.date = date
        all_tasks.append(self)


Task("Wynieść śmieci", "2022-12-07")
Task("Wyjść z psem", "2022-12-08")
Task("Pozmywać naczynia", "2022-12-09")
Task("Iść do psychologa", "2022-12-10")
Task("Umyć podłogę", "2022-12-17")
Task("Odebrać Tymusia", "2023-01-08")


def show_all_task():
    display_label["text"] = "All tasks"
    row_number = 0
    for task in all_tasks:
        ttk.Label(display_frame, text=task.content, font=("-size", 15, "-weight",
                  "bold")).grid(column=0, row=row_number, padx=20, pady=10, sticky=W)
        ttk.Label(display_frame, text=task.date, font=("-size", 15, "-weight",
                  "bold")).grid(column=1, row=row_number, padx=20, pady=10, sticky=W)
        row_number += 1


def add_task():

    def open_calendar():
        def ok():
            calendar_date = datetime.strptime(
                calendar.get_date(), "%d.%m.%Y").strftime("%Y-%m-%d")
            task_date.set(calendar_date)
            calendar_window.destroy()

        def cancel():
            calendar_window.destroy()

        calendar_window = Toplevel()
        calendar = Calendar(calendar_window)
        buttons_frame = Frame(calendar_window)
        ok_button = ttk.Button(buttons_frame, text="OK", command=ok)
        cancel_button = ttk.Button(
            buttons_frame, text="Cancel", command=cancel)

        calendar.grid(column=0, row=0, columnspan=2)
        buttons_frame.grid(column=1, row=1)
        ok_button.grid(column=0, row=0, padx=15, pady=5)
        cancel_button.grid(column=1, row=0, padx=15, pady=5)

    def add_content():
        content = enter_entry.get()
        Task(content, task_date.get())
        add_task_window.destroy()
        show_all_task()

    def cancel_add_content():
        add_task_window.destroy()
        show_all_task()

    add_task_window = Toplevel()
    enter_frame = ttk.Frame(add_task_window)
    enter_label = ttk.Label(enter_frame, text="Enter the task:", font=(
        "-size", 15, "-weight", "bold"))
    enter_entry = ttk.Entry(enter_frame, width=50)
    select_day_frame = ttk.Frame(add_task_window)
    select_day_label = ttk.Label(
        select_day_frame, text="Choose the day:", font=("-size", 10, "-weight", "bold"))
    task_date = StringVar()
    today_button = ttk.Radiobutton(
        select_day_frame, text="Today", variable=task_date, value=date.today())
    tommorrow_button = ttk.Radiobutton(
        select_day_frame, text="Tomorrow", variable=task_date, value=(date.today() + timedelta(days=1)))
    other_button = ttk.Button(
        select_day_frame, text="Other", command=open_calendar)
    all_buttons = [today_button, tommorrow_button, other_button]
    display_date_label = ttk.Label(
        add_task_window, textvariable=task_date, font=("-size", 15, "-weight", "bold"))
    ok_cancel_frame = ttk.Frame(add_task_window)
    ok_button = ttk.Button(ok_cancel_frame, text="OK", command=add_content)
    cancel_button = ttk.Button(
        ok_cancel_frame, text="Cancel", command=cancel_add_content)

    enter_frame.grid(column=0, row=0)
    enter_label.grid(column=0, row=1, pady=(15, 5))
    enter_entry.grid(column=0, row=2, pady=10, padx=10)
    select_day_frame.grid(column=0, row=1)
    select_day_label.grid(column=0, row=0, columnspan=3, pady=10)
    x = 0
    for button in all_buttons:
        button.grid(column=x, row=1, padx=10, pady=10)
        x += 1
    display_date_label.grid(column=0, row=2, pady=20)
    ok_cancel_frame.grid(column=0, row=3)
    ok_button.grid(column=0, row=0, padx=15, pady=(10, 20))
    cancel_button.grid(column=1, row=0, padx=15, pady=(10, 20))

def delete_task():
    delete_task_window = Toplevel()
    
window = Tk()
# na koniec zmienić ścieżkę
style = ttk.Style()
window.tk.call("source", r"To-Do-List\GUI_To-Do-List\azure.tcl")
window.tk.call("set_theme", "dark")
window.title("To Do List")
display_label = ttk.Label(window, text="View content",
                          anchor="s", font=("-size", 25, "-weight", "bold"))
display_frame = ttk.Frame(window)
buttons_frame = ttk.Frame(window)
add_task_button = ttk.Button(buttons_frame, text="Add Task", command=add_task)
delete_task_button = ttk.Button(buttons_frame, text="Delete Task")
set_date_button = ttk.Button(buttons_frame, text="Set Task Date")
get_done_button = ttk.Button(buttons_frame, text="Get Task Done")
get_not_done_button = ttk.Button(buttons_frame, text="Get Task Not Done")
show_all_tasks_button = ttk.Button(
    buttons_frame, text="Show All Tasks", command=show_all_task)
show_to_do_button = ttk.Button(buttons_frame, text="Show Tasks To Do")
show_done_button = ttk.Button(buttons_frame, text="Show Done Tasks")
show_for_button = ttk.Button(buttons_frame, text="Show Task For...")
all_buttons = [add_task_button, delete_task_button, set_date_button, get_done_button,
               get_not_done_button, show_all_tasks_button, show_to_do_button, show_done_button, show_for_button]

display_label.grid(column=0, row=0, pady=(20, 0), padx=(30))
display_frame.grid(column=0, row=1, pady=(0, 50), padx=(20, 50), ipadx=50)
buttons_frame.grid(column=1, row=1, padx=(50, 50), ipady=30)
x = 0
for button in all_buttons:
    button.grid(column=0, row=x, pady=10, sticky=(N, S, E, W))
    x += 1

window.eval('tk::PlaceWindow . center')
show_all_task()
window.mainloop()
