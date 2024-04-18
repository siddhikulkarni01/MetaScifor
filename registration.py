import tkinter as tk
from tkinter import messagebox

def submit_form():
    fullname = entry_fullname.get()
    email = entry_email.get()
    gender = gender_var.get()
    country = country_var.get()
    programming_languages = [language for language, value in programming_language_vars.items() if value.get() == 1]

    message = f"Full Name: {fullname}\n\nEmail: {email}\n\nGender: {gender}\n\nCountry: {country}\n\nProgramming Languages: {', '.join(programming_languages)}"
    messagebox.showinfo("Registration Details", message)
    print("Thank you!")

root = tk.Tk()
root.title("Registration Form")

# Full Name
tk.Label(root, text="Full Name:").grid(row=0, column=0)
entry_fullname = tk.Entry(root)
entry_fullname.grid(row=0, column=1)

# Email
tk.Label(root, text="Email:").grid(row=1, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1)

# Gender
tk.Label(root, text="Gender:").grid(row=2, column=0)
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=2, column=1)
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=2, column=2)

# Country
tk.Label(root, text="Country:").grid(row=3, column=0)
countries = ['USA', 'Canada', 'UK', 'Australia', 'India']  # Example list of countries
country_var = tk.StringVar()
country_var.set(countries[0])  # Default country
country_dropdown = tk.OptionMenu(root, country_var, *countries)
country_dropdown.grid(row=3, column=1)

# Programming Languages
tk.Label(root, text="Programming Languages:").grid(row=4, column=0)
programming_languages = ['Python', 'J ava', 'C++', 'JavaScript']  # Example list of programming languages
programming_language_vars = {language: tk.IntVar() for language in programming_languages}
for i, language in enumerate(programming_languages):
    tk.Checkbutton(root, text=language, variable=programming_language_vars[language]).grid(row=4, column=i+1)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=5, columnspan=5)

root.mainloop()
