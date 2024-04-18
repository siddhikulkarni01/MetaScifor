import tkinter as tk
from tkinter import ttk

def calculate_interest():
    p = float(p_entry.get())
    r = float(r_entry.get()) / 100
    t = float(t_entry.get())

    if i_type.get() == 1:  
        s_interest = (p * r * t) / 100
        s_interest_var.set(s_interest)
        c_interest_var.set(0)
    else:  
        c_interest = p * (1 + r) ** t - p
        c_interest_var.set(c_interest)
        s_interest_var.set(0)

root = tk.Tk()
root.title("Interest Calculator")

s_interest_var = tk.DoubleVar()
c_interest_var = tk.DoubleVar()

p_label = ttk.Label(root, text="Principal:")
p_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
p_entry = ttk.Entry(root)
p_entry.grid(row=0, column=1, padx=5, pady=5)

r_label = ttk.Label(root, text="Rate (%):")
r_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
r_entry = ttk.Entry(root)
r_entry.grid(row=1, column=1, padx=5, pady=5)

t_label = ttk.Label(root, text="Time (years):")
t_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
t_entry = ttk.Entry(root)
t_entry.grid(row=2, column=1, padx=5, pady=5)

i_type = tk.IntVar()
simple_radio = ttk.Radiobutton(root, text="Simple Interest", variable=i_type, value=1)
simple_radio.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="w")
compound_radio = ttk.Radiobutton(root, text="Compound Interest", variable=i_type, value=2)
compound_radio.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="w")

s_interest_label = ttk.Label(root, text="Simple Interest:")
s_interest_label.grid(row=5, column=0, padx=5, pady=5, sticky="e")
s_interest_output = ttk.Label(root, textvariable=s_interest_var)
s_interest_output.grid(row=5, column=1, padx=5, pady=5, sticky="w")

c_interest_label = ttk.Label(root, text="Compound Interest:")
c_interest_label.grid(row=6, column=0, padx=5, pady=5, sticky="e")
c_interest_output = ttk.Label(root, textvariable=c_interest_var)
c_interest_output.grid(row=6, column=1, padx=5, pady=5, sticky="w")

calculate_button = ttk.Button(root, text="Calculate", command=calculate_interest)
calculate_button.grid(row=7, column=0, columnspan=2, padx=5, pady=10)

root.mainloop()