"""Himanshi is confused with different shapes. Write a program in python to print
 different shapes using these symbols: “|”, “-”, “/”, “\”.
"""
# rectangle
def print_rectangle(width, height):
    for i in range(height):
        print("|" + "-" * (width) + "|")

# triangle
def print_triangle(height):
    for i in range(height):
        print(" " * (height - i - 1) + "/" + "-" * (2 * i) + "\\")


# square
def print_square(side_length):
    for i in range(side_length):
        print("|" + "--" * (side_length) + "|")


print("Rectangle:")
print_rectangle(4, 8)
print("\nTriangle:")
print_triangle(5)
print("\nSquare:")
print_square(4)
