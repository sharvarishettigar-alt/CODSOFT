import tkinter as tk
from tkinter import messagebox
def calculate():
    try:
        num1=float(entry_num1.get())
        num2=float(entry_num2.get())
    except ValueError:
        messagebox.showerror("Error","Please enter valid number.")
        return
    op=op_var.get()
    if(op=="+"):
        result=num1+num2
    elif(op=="-"):
        result=num1-num2
    elif(op=="*"):
        result=num1*num2
    elif(op=="/"):
        if(num2==0):
            messagebox.showerror("Error",'Division by zero error.')
        else:
            result=num1/num2
    else:
        messagebox.showerror("Error","Please select valid operation.")
        return
    label_result.config(text=f"Result: {num1} {op} {num2} = {result}")

root=tk.Tk()
root.title("Calculator")
root.geometry("350x400")
root.resizable(False,False)

tk.Label(root,text="Basic Calculator",font=("Arial",14,"bold")).pack(pady=10)

tk.Label(root,text="First Number: ").pack()
entry_num1=tk.Entry(root,width=20)
entry_num1.pack()

tk.Label(root,text="Second Number: ").pack()
entry_num2=tk.Entry(root,width=20)
entry_num2.pack()

tk.Label(root,text="Operation").pack()
op_var=tk.StringVar(value="+")
frame_ops=tk.Frame(root)
frame_ops.pack()
for op in ['+','-','*','/']:
    tk.Radiobutton(frame_ops,text=op,variable=op_var,value=op).pack(side=tk.LEFT,padx=5)

tk.Button(root,text="Calculate",command=calculate,bg="blue",fg="white",width=15).pack(pady=20)

label_result=tk.Label(root,text="Result: ",font=("Arial",12))
label_result.pack()
root.mainloop()
