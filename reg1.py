import tkinter as tk

def submit_form():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    address = address_entry.get("1.0", "end-1c")
    email = email_entry.get()
    contact = contact_entry.get()
    country = country_entry.get()
    state = state_entry.get()
    diseases = [disease_var[i].get() for i in range(len(disease_var))]
    
    print("name:", name)
    print("age:", age)
    print("gender:", gender)
    print("address:", address)
    print("email:", email)
    print("contact no:", contact)
    print("country:", country)
    print("state:", state)
    print("diseases:", diseases)

root = tk.Tk()
root.title("Covid vaccine Registration Form")

# Name
name_label = tk.Label(root, text="name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

# Age
age_label = tk.Label(root, text="age:")
age_label.grid(row=1, column=0)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1)

# Gender
gender_label = tk.Label(root, text="gender:")
gender_label.grid(row=2, column=0)
gender_var = tk.StringVar()
gender_var.set("male")
male_radio = tk.Radiobutton(root, text="male", variable=gender_var, value="male")
male_radio.grid(row=2, column=1)
female_radio = tk.Radiobutton(root, text="female", variable=gender_var, value="female")
female_radio.grid(row=2, column=2)

# Address
address_label = tk.Label(root, text="address:")
address_label.grid(row=3, column=0)
address_entry = tk.Text(root, height=4, width=30)
address_entry.grid(row=3, column=1)

# Email
email_label = tk.Label(root, text="email:")
email_label.grid(row=4, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=4, column=1)

# Contact No
contact_label = tk.Label(root, text="contact No:")
contact_label.grid(row=5, column=0)
contact_entry = tk.Entry(root)
contact_entry.grid(row=5, column=1)

# Country
country_label = tk.Label(root, text="country:")
country_label.grid(row=6, column=0)
country_entry = tk.Entry(root)
country_entry.grid(row=6, column=1)

# State
state_label = tk.Label(root, text="state:")
state_label.grid(row=7, column=0)
state_entry = tk.Entry(root)
state_entry.grid(row=7, column=1)

# Diseases
diseases_label = tk.Label(root, text="select any diseases you are having:")
diseases_label.grid(row=8, column=0)
disease_var = []
disease_labels = ["cold", "cough", "fever", "headache"]
for i, disease in enumerate(disease_labels):
    var = tk.BooleanVar()
    disease_var.append(var)
    checkbox = tk.Checkbutton(root, text=disease, variable=var)
    checkbox.grid(row=8+i, column=1)

# Submit Button
submit_button = tk.Button(root, text="submit", command=submit_form)
submit_button.grid(row=9+len(disease_labels), column=0, columnspan=2)

root.mainloop()