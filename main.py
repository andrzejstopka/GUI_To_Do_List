from tkinter import *
from tkinter import ttk
from datetime import date, timedelta
import pickle

window = Tk()
# na koniec zmienić ścieżkę
window.tk.call("source", r"To-Do-List\GUI_To-Do-List\azure.tcl")
window.tk.call("set_theme", "dark")
window.title("To Do List")

def create_display():
    for x in range(10):
        ttk.Label(display_frame, text="treść jest taka i owaka").grid(column=0, row=x, pady=10, padx=20)

display_label = ttk.Label(window, text="View content", anchor="s",font=("-size", 25, "-weight", "bold"))
display_frame = ttk.Frame(window, relief="sunken")
buttons_frame = ttk.Frame(window)
add_task_button = ttk.Button(buttons_frame, text="Add Task")
delete_task_button = ttk.Button(buttons_frame, text="Delete Task")
set_date_button = ttk.Button(buttons_frame, text="Set Task Date")
get_done_button = ttk.Button(buttons_frame, text="Get Task Done")
get_not_done_button = ttk.Button(buttons_frame, text="Get Task Not Done")
show_all_tasks_button = ttk.Button(buttons_frame, text="Show All Tasks")
show_to_do_button = ttk.Button(buttons_frame, text="Show Tasks To Do")
show_done_button = ttk.Button(buttons_frame, text="Show Done Tasks")
show_for_button = ttk.Button(buttons_frame, text="Show Task For...")
all_buttons = [add_task_button, delete_task_button, set_date_button, get_done_button, get_not_done_button, show_all_tasks_button, show_to_do_button, show_done_button, show_for_button]


display_label.grid(column=0, row=0, pady=(20, 0), padx=(30))
display_frame.grid(column=0, row=1, pady=(0, 50), padx=(20, 50), ipadx=100)
buttons_frame.grid(column=1, row=1, padx=(50,50), ipady=30)
x = 0
for button in all_buttons:
    button.grid(column=0, row=x, pady=10, sticky=(N,S,E,W))
    x += 1
        
create_display()

window.mainloop()
