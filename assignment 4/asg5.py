# List of colors
colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown"]

# Function to print colors
def print_colors():
    for color in colors:
        print(color)

# Main function
def main():
    print("Please enter color names. Enter 'done' when finished.")
    while True:
        color = input("Enter a color: ").lower()
        if color == "done":
            break
        # Call function to print colors
        print_colors()

if __name__ == "__main__":
    main()
