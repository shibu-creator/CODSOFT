import tkinter as tk

tasks = []

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_list()
        entry.delete(0, tk.END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        tasks.pop(selected[0])
        update_list()

def update_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# GUI window
app = tk.Tk()
app.title("To-Do List")
app.geometry("300x350")

# Title
tk.Label(app, text="📝 To-Do List").pack(pady=5)

# Entry for new task
entry = tk.Entry(app)
entry.pack(pady=5)

# Add button
tk.Button(app, text="Add Task", command=add_task).pack()

# Task list display
listbox = tk.Listbox(app, height=10, width=40)
listbox.pack(pady=10)

# Delete button
tk.Button(app, text="Delete Selected", command=delete_task).pack()

# Run app
app.mainloop()
