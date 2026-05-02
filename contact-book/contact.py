import tkinter as tk
from tkinter import messagebox

contacts=[]

def book():
    listbox.delete(0,tk.END)
    for i in contacts:
        listbox.insert(tk.END,f"{i['name']} - {i['phone']}")

def add():
    name=entry_name.get().strip()
    phone=entry_phone.get().strip()
    email=entry_email.get().strip()
    address=entry_address.get().strip()
    if not name or not phone:
        messagebox.showwarning("Warning","Name and Phone are required!!!")
        return
    contacts.append({"name":name,"phone":phone,"email":email,"address":address})
    entry_name.delete(0,tk.END)
    entry_phone.delete(0,tk.END)
    entry_email.delete(0,tk.END)
    entry_address.delete(0,tk.END)
    book()

def view():
    selected=listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning","Select a contact to view!!!")
        return
    i=contacts[selected[0]]
    messagebox.showinfo("Contact Details",f"Name: {i['name']}\n" f"Phone: {i['phone']}\n" f"Email: {i['email']}\n" f"Address: {i['address']}\n")

def delete():
    selected=listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning","Select a contact to delete!!!")
        return
    name=contacts[selected[0]]["name"]
    if messagebox.askyesno("Confirm",f'Delete "{name}"?'):
        contacts.pop(selected[0])
        book()

def search():
    query=entry_search.get().strip().lower()
    listbox.delete(0,tk.END)
    for i in contacts:
        if query in i["name"].lower() or query in i["phone"]:
            listbox.insert(tk.END,f"{i['name']} - {i['phone']}")

def show():
    entry_search.delete(0,tk.END)
    book()

root=tk.Tk()
root.title("Contact Book")
root.geometry("450x550")
root.resizable(False,False)

tk.Label(root,text="Contact Book",font=("Arial",16,"bold")).pack(pady=10)

frame_input=tk.Frame(root)
frame_input.pack(pady=5)

labels=["Name:", "Phone:", "Email:", "Address:"]
entries=[]
for i,label in enumerate(labels):
    tk.Label(frame_input,text=label,width=10,anchor="e").grid(row=i,column=0,padx=5,pady=3)
    e=tk.Entry(frame_input,width=30)
    e.grid(row=i,column=1)
    entries.append(e)

entry_name,entry_phone,entry_email,entry_address=entries

tk.Button(root,text="Add Contact",command=add,bg="green",fg="white",width=25).pack(pady=5)

frame_search=tk.Frame(root)
frame_search.pack(pady=5)

entry_search=tk.Entry(frame_search,width=22)
entry_search.pack(side=tk.LEFT,padx=5)

tk.Button(frame_search,text="Search",command=search,width=10).pack(side=tk.LEFT,padx=5)
tk.Button(frame_search,text="Show Info",command=show,width=10).pack(side=tk.LEFT,padx=5)

listbox=tk.Listbox(root,width=45,height=10,font=("Arial",12))
listbox.pack(pady=10)

frame_btns=tk.Frame(root)
frame_btns.pack(pady=10)
tk.Button(root,text="View Details",command=view,bg="blue",fg="white",width=15).pack(side=tk.LEFT,padx=5)
tk.Button(root,text="Delete the selected",command=delete,bg="red",fg="white",width=20).pack(side=tk.LEFT,padx=5)

root.mainloop()
