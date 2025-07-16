import tkinter as tk

def calc():
    n1 = float(e1.get())
    n2 = float(e2.get())
    op = e3.get()

    if op == "+":
        res.set("Result: " + str(n1 + n2))
    elif op == "-":
        res.set("Result: " + str(n1 - n2))
    elif op == "*":
        res.set("Result: " + str(n1 * n2))
    elif op == "/":
        res.set("Result: " + str(n1 / n2))
    else:
        res.set("Invalid operation")

app = tk.Tk()
app.title("Calculator")
app.geometry("300x250")

tk.Label(app, text="First number").pack()
e1 = tk.Entry(app)
e1.pack()

tk.Label(app, text="Second number").pack()
e2 = tk.Entry(app)
e2.pack()

tk.Label(app, text="Operation (+ - * /)").pack()
e3 = tk.Entry(app)
e3.pack()

res = tk.StringVar()
tk.Label(app, textvariable=res).pack()

tk.Button(app, text="Calculate", command=calc).pack()

app.mainloop()
