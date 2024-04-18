from tkinter import Tk, Label, Button
import tkinter as tk
import requests

window =  tk.Tk()
window.title("QUOTE GENERATOR")

label = Label(window, text="", wraplength=400)
label.pack()

def fetch_quote():
    url  = 'http://api.quotable.io/random'
    response = requests.get(url)
    Json = response.json()
    Quote = Json['content']
    Author = Json['author']
    label.config(text=f"{Quote} \n\n - {Author}")

button = Button(window, text="Click", bg="yellow", command=fetch_quote)
button.pack()

window.mainloop()
