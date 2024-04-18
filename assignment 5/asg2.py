"""Himanshi has a text file and she wants to check whether that file contains any numerical value. So to help
Himanshi write a python program that can check whether the text file includes any numerical value or not. As 
text files contain so many lines, so print the line number that has numerical values"""
import re

def check_numerical_value(filename):
    with open(filename, 'r') as file:
        line_number = 0
        for line in file:
            line_number += 1
            if re.search(r'\d', line):
                print(f"Line {line_number}: {line.strip()}")

check_numerical_value("python1.txt")
