"""● Ayman wants to modify one of his text files. In his text file, he wants to start a new line whenever he 
encounters a number followed by a period(.). So he decides to do the same with the help of the python program. 
Write a program for Ayman."""
def modify_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        modified_content = ""
  
        for i in range(len(content)):
       
            if content[i].isdigit() and content[i+1:i+2] == '.':
                modified_content += content[i] + '.\n'
            else:
                modified_content += content[i]

        with open(file_path, 'w') as file:
            file.write(modified_content)
        
        print("File modified successfully!")
    
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", str(e))

file_path = "asg6.txt"

modify_file(file_path)
