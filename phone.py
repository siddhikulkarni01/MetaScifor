import tkinter as tk
from tkinter import messagebox

def get_selected_contact():
    selected_contact = contact_listbox.curselection()
    if selected_contact:
        contact_info = contact_listbox.get(selected_contact[0])
        messagebox.showinfo("Selected Contact", contact_info)
    else:
        messagebox.showwarning("No Contact Selected", "Please select a contact.")

def add_contact():
    name = name_entry.get()
    number = number_entry.get()
    if name and number:
        contact_listbox.insert(tk.END, f"Name: {name}, Number: {number}")
        name_entry.delete(0, tk.END)
        number_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Missing Information", "Please enter both name and number.")

def edit_contact():
    selected_contact = contact_listbox.curselection()
    if selected_contact:
        name = name_entry.get()
        number = number_entry.get()
        if name and number:
            contact_listbox.delete(selected_contact)
            contact_listbox.insert(selected_contact, f"Name: {name}, Number: {number}")
            name_entry.delete(0, tk.END)
            number_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Missing Information", "Please enter both name and number.")
    else:
        messagebox.showwarning("No Contact Selected", "Please select a contact to edit.")

def view_contact():
    selected_contact = contact_listbox.curselection()
    if selected_contact:
        contact_info = contact_listbox.get(selected_contact)
        messagebox.showinfo("Contact Details", contact_info)
    else:
        messagebox.showwarning("No Contact Selected", "Please select a contact to view.")


root = tk.Tk()
root.title("Contact Book")

name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

number_label = tk.Label(root, text="Number:")
number_label.grid(row=1, column=0, padx=5, pady=5)
number_entry = tk.Entry(root)
number_entry.grid(row=1, column=1, padx=5, pady=5)

contact_listbox = tk.Listbox(root, width=50)
contact_listbox.grid(row=2, columnspan=2, padx=5, pady=5)

get_selected_button = tk.Button(root, text="Get Selected Contact", command=get_selected_contact)
get_selected_button.grid(row=3, column=0, padx=5, pady=5)

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=3, column=1, padx=5, pady=5)

edit_button = tk.Button(root, text="Edit Contact", command=edit_contact)
edit_button.grid(row=4, column=0, padx=5, pady=5)

view_button = tk.Button(root, text="View Contact", command=view_contact)
view_button.grid(row=4, column=1, padx=5, pady=5)



exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
