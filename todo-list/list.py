import tkinter as tk
from tkinter import messagebox
tasks=[]
def list():
    listbox.delete(0,tk.END)
    for i in tasks:
        status="Yes" if i["done"] else "No"
        listbox.insert(tk.END,f"[{status}] {i['task']}")

def add_task():
    task=entry_task.get().strip()
    if task:
        tasks.append({"task": task,"done":False})
        entry_task.delete(0,tk.END)
        list()
    else:
        messagebox.showwarning("Warning","Task cannot be empty.")

def done():
    selected=listbox.curselection()
    if selected:
        tasks[selected[0]]["done"]=True
        list()
    else:
        messagebox.showwarning("Warning","Please select a task.")

def delete_task():
    selected=listbox.curselection()
    if selected:
        removed=tasks.pop(selected[0])
        list()
        messagebox.showinfo("Deleted",f'Task "{removed["task"]}" deleted.')
    else:
        messagebox.showwarning("Warning","Select a task to delete.")

root=tk.Tk()
root.title("To-Do List")
root.geometry("500x500")
root.resizable(False,False)

tk.Label(root,text="To-Do List", font=("Arial",16,"bold")).pack(pady=10)
frame_input=tk.Frame(root)
frame_input.pack(pady=5)
entry_task=tk.Entry(frame_input,width=28)
entry_task.pack(side=tk.LEFT,padx=5)
tk.Button(frame_input,text="Add",command=add_task,bg="blue",fg="white").pack(side=tk.LEFT)

listbox=tk.Listbox(root,width=45,height=12,font=("Arial",12))
listbox.pack(pady=10)

frame_btns=tk.Frame(root)
frame_btns.pack()

tk.Button(frame_btns,text="Mark Done",command=done,bg="green",fg="white",width=12).pack(side=tk.LEFT,padx=5)
tk.Button(frame_btns,text="Delete",command=delete_task,bg="red",fg="white",width=12).pack(side=tk.LEFT,padx=5)

root.mainloop()
