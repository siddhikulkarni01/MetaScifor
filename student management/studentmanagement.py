import tkinter as tk
from tkinter import messagebox

class Student:
    def __init__(self, name, age, roll_no, grade):
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.grade = grade

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, age, roll_no, grade):
        student = Student(name, age, roll_no, grade)
        self.students.append(student)
        messagebox.showinfo("Success", "Student added successfully.")

    def display_students(self):
        if not self.students:
            messagebox.showinfo("No Students", "No students data to display.")
        else:
            student_details = ""
            for student in self.students:
                student_details += f"Name: {student.name}, Age: {student.age}, Roll No: {student.roll_no}, Grade: {student.grade}\n"
            messagebox.showinfo("Student Details", student_details)

    def search_student(self, roll_no):
        found = False
        for student in self.students:
            if student.roll_no == roll_no:
                messagebox.showinfo("Student Found", f"Name: {student.name}\nAge: {student.age}\nRoll No: {student.roll_no}\nGrade: {student.grade}")
                found = True
                break
        if not found:
            messagebox.showinfo("Not Found", "Student not found.")

    def delete_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                messagebox.showinfo("Success", "Student deleted successfully.")
                return
        messagebox.showinfo("Not Found", "Student data not found.")

    def update_student(self, roll_no, name=None, age=None, grade=None):
        for student in self.students:
            if student.roll_no == roll_no:
                if name:
                    student.name = name
                if age:
                    student.age = age
                if grade:
                    student.grade = grade
                messagebox.showinfo("Success", "Student details updated successfully.")
                return
        messagebox.showinfo("Not Found", "No data found for update.")

    def run(self):
        root = tk.Tk()
        root.title("Student Management System")

        def add_student():
            name = name_entry.get()
            age = age_entry.get()
            roll_no = roll_no_entry.get()
            grade = grade_entry.get()
            self.add_student(name, age, roll_no, grade)

        def display_students():
            self.display_students()

        def search_student():
            roll_no = search_entry.get()
            self.search_student(roll_no)

        def delete_student():
            roll_no = delete_entry.get()
            self.delete_student(roll_no)

        def update_student():
            roll_no = update_entry.get()
            name = new_name_entry.get()
            age = new_age_entry.get()
            grade = new_grade_entry.get()
            self.update_student(roll_no, name, age, grade)

        # GUI Layout
        tk.Label(root, text="Name:").grid(row=0, column=0)
        tk.Label(root, text="Age:").grid(row=1, column=0)
        tk.Label(root, text="Roll No.:").grid(row=2, column=0)
        tk.Label(root, text="Grade:").grid(row=3, column=0)

        name_entry = tk.Entry(root)
        age_entry = tk.Entry(root)
        roll_no_entry = tk.Entry(root)
        grade_entry = tk.Entry(root)

        name_entry.grid(row=0, column=1)
        age_entry.grid(row=1, column=1)
        roll_no_entry.grid(row=2, column=1)
        grade_entry.grid(row=3, column=1)

        add_button = tk.Button(root, text="Add Student", command=add_student)
        add_button.grid(row=4, column=0, columnspan=2, pady=5)

        display_button = tk.Button(root, text="Display Students", command=display_students)
        display_button.grid(row=5, column=0, columnspan=2, pady=5)

        search_label = tk.Label(root, text="Enter roll no. to search:")
        search_label.grid(row=6, column=0, columnspan=2, pady=5)

        search_entry = tk.Entry(root)
        search_entry.grid(row=7, column=0, columnspan=2, pady=5)

        search_button = tk.Button(root, text="Search Student", command=search_student)
        search_button.grid(row=8, column=0, columnspan=2, pady=5)

        delete_label = tk.Label(root, text="Enter roll no. to delete:")
        delete_label.grid(row=9, column=0, columnspan=2, pady=5)

        delete_entry = tk.Entry(root)
        delete_entry.grid(row=10, column=0, columnspan=2, pady=5)

        delete_button = tk.Button(root, text="Delete Student", command=delete_student)
        delete_button.grid(row=11, column=0, columnspan=2, pady=5)

        update_label = tk.Label(root, text="Enter roll no. to update:")
        update_label.grid(row=12, column=0, columnspan=2, pady=5)

        update_entry = tk.Entry(root)
        update_entry.grid(row=13, column=0, columnspan=2, pady=5)

        new_name_label = tk.Label(root, text="Enter new name (leave empty to skip):")
        new_name_label.grid(row=14, column=0, columnspan=2, pady=5)

        new_name_entry = tk.Entry(root)
        new_name_entry.grid(row=15, column=0, columnspan=2, pady=5)

        new_age_label = tk.Label(root, text="Enter age (leave empty to skip):")
        new_age_label.grid(row=16, column=0, columnspan=2, pady=5)

        new_age_entry = tk.Entry(root)
        new_age_entry.grid(row=17, column=0, columnspan=2, pady=5)

        new_grade_label = tk.Label(root, text="Enter grade (leave empty to skip):")
        new_grade_label.grid(row=18, column=0, columnspan=2, pady=5)

        new_grade_entry = tk.Entry(root)
        new_grade_entry.grid(row=19, column=0, columnspan=2, pady=5)

        update_button = tk.Button(root, text="Update Student", command=update_student)
        update_button.grid(row=20, column=0, columnspan=2, pady=5)

        root.mainloop()

if __name__ == "__main__":
    system = StudentManagementSystem()
    system.run()
