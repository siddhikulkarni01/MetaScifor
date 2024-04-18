"""Arunima created a text file on programming where she wrote the word language incorrectly many times. Now she 
wants to replace the incorrect word with the correct word. Doing it manually can take a lot of time plus she can 
miss out few words at the end. To help Arunima to replace the words write a python program. Use the concept of file
handling and make changes in the text file."""
def replace_word(input_file,wrong,right):
    try:
        with open(input_file, 'r') as file:
            content = file.read()

            correct_content =  content.replace(wrong,right)

        with open(input_file,'w') as file:
            file.write(correct_content)
        
        print("Changes made successfully")


    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", str(e))

input_string = "programs.txt"

incorect_word =  'langauge'

correct_word = 'language'

replace_word(input_string,incorect_word,correct_word)

