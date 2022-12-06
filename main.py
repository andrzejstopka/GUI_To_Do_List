from tkinter import *
from tkinter import ttk
from datetime import date, timedelta, datetime
import pickle
from tkcalendar import Calendar

class Task:
    done = False
    def __init__(self, content, date):
        self.content = content
        self.date = date
        all_tasks.append(self)

def show_all_task():
    for widget in display_frame.winfo_children():
        widget.destroy()
    display_label["text"] = "All tasks"
    row_number = 0
    for task in all_tasks:
        ttk.Label(display_frame, text=task.content, font=("-size", 15, "-weight",
                  "bold")).grid(column=0, row=row_number, padx=20, pady=10, sticky=W)
        ttk.Label(display_frame, text=task.date, font=("-size", 15, "-weight",
                  "bold")).grid(column=1, row=row_number, padx=20, pady=10, sticky=W)
        row_number += 1

def show_to_do_tasks():
    for widget in display_frame.winfo_children():
        widget.destroy()
    display_label["text"] = "Tasks To Do"
    row_number = 0
    for task in all_tasks:
        if task.done == False:
            ttk.Label(display_frame, text=task.content, font=("-size", 15, "-weight",
                    "bold")).grid(column=0, row=row_number, padx=20, pady=10, sticky=W)
            ttk.Label(display_frame, text=task.date, font=("-size", 15, "-weight",
                    "bold")).grid(column=1, row=row_number, padx=20, pady=10, sticky=W)
            row_number += 1

def show_done_tasks():
    for widget in display_frame.winfo_children():
        widget.destroy()
    display_label["text"] = "Done Tasks"
    row_number = 0
    for task in all_tasks:
        if task.done == True:
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
    style = ttk.Style()
    style.configure("size.TCheckbutton", font=("arial", 15, "bold"))
    style.configure("size.TButton", font=("arial", 12, "bold"))
    to_delete = []

    def select_task(task, variable):
        if variable.get() == 1:
            to_delete.append(task)
        else:
            to_delete.remove(task)

    def create_checkbox(parent, task, row_number):
        task_var = IntVar()
        task_checkbox = ttk.Checkbutton(parent, text=f"{task.content} ({task.date})", style="size.TCheckbutton",
                                        variable=task_var, onvalue=1, offvalue=0, command=lambda: select_task(task, task_var))
        task_checkbox.grid(column=0, row=row_number, sticky=W, pady=5)

    def tasks_list(task_frame):
        global all_tasks
        row_number = 0
        for task in all_tasks:
            create_checkbox(task_frame, task, row_number)
            row_number += 1

    def load(task_frame):
        task_frame = ttk.Frame(delete_task_window)
        task_frame.grid(column=0, row=0, padx=10, pady=15, ipadx=10, ipady=10)
        tasks_list(task_frame)

    def remove_tasks():
        for x in to_delete:
            all_tasks.remove(x)
        delete_task_window.destroy()
        show_all_task()

    delete_task_window = Toplevel()
    load(delete_task_window)
    buttons_frame = ttk.Frame(delete_task_window)
    remove_button = ttk.Button(
        buttons_frame, text="Delete", command=remove_tasks, style="size.TButton")
    cancel_button = ttk.Button(buttons_frame, text="Cancel",
                               command=delete_task_window.destroy, style="size.TButton")
    buttons_frame.grid(column=0, row=1)
    remove_button.grid(column=0, row=0, padx=10, pady=(0, 15))
    cancel_button.grid(column=1, row=0, padx=10, pady=(0, 15))


def set_date():
    def change_date(task):
        def ok():
            calendar_date = datetime.strptime(
                calendar.get_date(), "%d.%m.%Y").strftime("%Y-%m-%d")
            task.date = calendar_date
            calendar_window.destroy()
            set_date_window.destroy()
            show_all_task()

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

    def create_widgets(parent, task, row_number):
        task_label = ttk.Label(parent, text=task.content,
                               font=("-size", 12, "-weight", "bold"))
        task_date = ttk.Label(parent, text=task.date,
                              font=("-size", 12, "-weight", "bold"))
        change_button = ttk.Button(
            parent, text="Change", command=lambda: change_date(task))

        task_label.grid(column=0, row=row_number, padx=15, pady=10)
        task_date.grid(column=1, row=row_number, padx=15, pady=10)
        change_button.grid(column=2, row=row_number, padx=15, pady=10)

    def tasks_list(set_date_window):
        global all_tasks
        row_number = 0
        for task in all_tasks:
            create_widgets(set_date_window, task, row_number)
            row_number += 1
        cancel_button = ttk.Button(
            set_date_window, text="Cancel", command=set_date_window.destroy)
        cancel_button.grid(column=0, row=row_number, pady=20, columnspan=3)

    def load(set_date_window):
        tasks_list(set_date_window)

    set_date_window = Toplevel()
    load(set_date_window)


def get_done():
    to_done = []
    style = ttk.Style()
    style.configure("size.TCheckbutton", font=("arial", 15, "bold"))

    def make_done():
        for task in to_done:
            task.done = True
            get_done_window.destroy()

    def done_for_task(task, task_var):
        if task_var.get() == 1:
            to_done.append(task)
        else:
            to_done.remove(task)

    def create_widgets(parent, task, row_number):
        task_var = IntVar()
        task_checkbox = ttk.Checkbutton(parent, text=f"{task.content} ({task.date})", style="size.TCheckbutton",
                                        variable=task_var, onvalue=1, offvalue=0, command=lambda: done_for_task(task, task_var))
        task_checkbox.grid(column=0, row=row_number, sticky=W, pady=5)

    def tasks_list(get_done_window):
        global all_tasks
        for widget in get_done_window.winfo_children():
            widget.destroy()
        row_number = 0
        for task in all_tasks:
            if task.done == False:
                create_widgets(get_done_window, task, row_number)
                row_number += 1
        buttons_frame = ttk.Frame(get_done_window)
        get_done_button = ttk.Button(
            buttons_frame, text="Get Done", command=make_done, style="size.TButton")
        cancel_button = ttk.Button(
            buttons_frame, text="Cancel", command=get_done_window.destroy)
        buttons_frame.grid(column=0, row=row_number)
        get_done_button.grid(column=0, row=0, pady=20, padx=20)
        cancel_button.grid(column=1, row=0, pady=20, padx=20)

    def load(get_done_window):
        tasks_list(get_done_window)

    get_done_window = Toplevel()
    load(get_done_window)


def get_not_done():
    to_not_done = []
    style = ttk.Style()
    style.configure("size.TCheckbutton", font=("arial", 15, "bold"))

    def make_done():
        for task in to_not_done:
            task.done = False
            get_not_done_window.destroy()

    def not_done_for_task(task, task_var):
        if task_var.get() == 1:
            to_not_done.append(task)
        else:
            to_not_done.remove(task)

    def create_widgets(parent, task, row_number):
        task_var = IntVar()
        task_checkbox = ttk.Checkbutton(parent, text=f"{task.content} ({task.date})", style="size.TCheckbutton",
                                        variable=task_var, onvalue=1, offvalue=0, command=lambda: not_done_for_task(task, task_var))
        task_checkbox.grid(column=0, row=row_number, sticky=W, pady=5)

    def tasks_list(get_not_done_window):
        global all_tasks
        for widget in get_not_done_window.winfo_children():
            widget.destroy()
        row_number = 0
        for task in all_tasks:
            if task.done == True:
                create_widgets(get_not_done_window, task, row_number)
                row_number += 1
        buttons_frame = ttk.Frame(get_not_done_window)
        get_done_button = ttk.Button(
            buttons_frame, text="Get Done", command=make_done, style="size.TButton")
        cancel_button = ttk.Button(
            buttons_frame, text="Cancel", command=get_not_done_window.destroy)
        buttons_frame.grid(column=0, row=row_number)
        get_done_button.grid(column=0, row=0, pady=20, padx=20)
        cancel_button.grid(column=1, row=0, pady=20, padx=20)

    def load(get_not_done_window):
        tasks_list(get_not_done_window)

    get_not_done_window = Toplevel()
    load(get_not_done_window)

try:
    with open("data.py", "rb") as load_data:
        all_tasks = pickle.load(load_data)
except FileNotFoundError:
    all_tasks = []

all_tasks.sort(key = lambda x: x.date)
window = Tk()
window.tk.call("source", "azure.tcl")
window.tk.call("set_theme", "dark")
window.title("To Do List")
display_label = ttk.Label(window, text="View content",
                          anchor="s", font=("-size", 25, "-weight", "bold"))
display_frame = ttk.Frame(window)
buttons_frame = ttk.Frame(window)
add_task_button = ttk.Button(buttons_frame, text="Add Task", command=add_task)
delete_task_button = ttk.Button(
    buttons_frame, text="Delete Task", command=delete_task)
set_date_button = ttk.Button(
    buttons_frame, text="Set Task Date", command=set_date)
get_done_button = ttk.Button(
    buttons_frame, text="Get Task Done", command=get_done)
get_not_done_button = ttk.Button(buttons_frame, text="Get Task Not Done", command=get_not_done)
show_all_tasks_button = ttk.Button(
    buttons_frame, text="Show All Tasks", command=show_all_task)
show_to_do_button = ttk.Button(buttons_frame, text="Show Tasks To Do", command=show_to_do_tasks)
show_done_button = ttk.Button(buttons_frame, text="Show Done Tasks", command=show_done_tasks)
all_buttons = [add_task_button, delete_task_button, set_date_button, get_done_button,
               get_not_done_button, show_all_tasks_button, show_to_do_button, show_done_button]

display_label.grid(column=0, row=0, pady=(20, 0), padx=(30))
display_frame.grid(column=0, row=1, pady=(0, 50), padx=(20, 30), ipadx=50)
buttons_frame.grid(column=1, row=1, padx=(0, 50), ipady=30)
x = 0
for button in all_buttons:
    button.grid(column=0, row=x, pady=10, sticky=(N, S, E, W))
    x += 1
    

window.eval('tk::PlaceWindow . center')
show_all_task()

def on_destroy(event):
    if event.widget.winfo_parent() == "":
        with open("data.py", "wb") as save_data:
            pickle.dump(all_tasks, save_data)
window.bind("<Destroy>", on_destroy)
window.mainloop()
