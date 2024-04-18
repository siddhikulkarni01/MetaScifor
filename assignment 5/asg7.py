"""Nidhi has a bad habit of repeating the same word while typing. She wants a program that can remove duplicate 
phrases from paragraphs written by her. To help Nidhi write a python program that can connect with a text file 
and remove repeating words. """
def remove_duplicate_phrases(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.readlines()
            print(content,type(content))
        
        modified_content = []
        for line in content:
            words = line.split()
            print(words)
            unique_words = []
            for word in words:
                if word not in unique_words:
                    unique_words.append(word)
            modified_line = ' '.join(unique_words)
            modified_content.append(modified_line)

        with open(file_path, 'w') as file:
            file.write('\n'.join(modified_content))
        
        print("Duplicate phrases removed successfully!")
    
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", str(e))


file_path = "repeat.txt"

remove_duplicate_phrases(file_path)
