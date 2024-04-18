"""● Arvind has a huge text file and he wants to put a serial number at the beginning of each line. Doing this 
task manually can take a lot of time. He is not aware of python file handling. Write a python program that can 
put a serial number in front of each line in any specified text file."""
def add_serial_number(filename):

    with open(filename, 'r') as file:
        lines = file.readlines()

    lines_with_serial = [f"{i + 1}. {line}" for i, line in enumerate(lines)]

    with open(filename, 'w') as file:
        file.writelines(lines_with_serial)


add_serial_number("bmi.txt")

