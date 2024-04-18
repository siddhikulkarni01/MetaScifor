import tkinter as tk
from tkinter import colorchooser

current_tool = "pen"
pen_color = "black"
brush_size = 2

def use_pen():
    global current_tool
    current_tool = "pen"

def use_brush():
    global current_tool
    current_tool = "eraser"

def choose_pen():
    global pen_color
    color = colorchooser.askcolor()
    if color:
        pen_color = color[1]

def change_size(val):
    global brush_size
    brush_size = int(val)

def paint(event):
    x1, y1 = (event.x - brush_size),(event.y - brush_size)
    x2, y2 = (event.x - brush_size),(event.y - brush_size)
    
