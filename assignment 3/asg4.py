"""Jack has been experimenting a lot with mirrors in his Physics class. He was very distracted throughout 
his entire school day as he spent all day thinking about mirrors and mirror images. When Jack went to his 
computer class, he finally found a solution, he wanted to create a computer program that can take a three 
letter string input from the user and display the mirror image of it. Write a program for the same."""


def mirror_image(word):
   
    if len(word) == 3:
      
        mirror = word[::-1]
        return mirror
    else:
        return "invalid input! Please enter a three-letter string."


input_word = input("enter a three-letter string: ")


print("mirror image:", mirror_image(input_word))
