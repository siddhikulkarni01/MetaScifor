"""A palindrome is a word, number, phrase, or other sequence of characters that reads the same backward as 
forward, such as madam or racecar. Arunima got a new puppy (pet) and she wants to decide the name for her pet.
 The name of the pet should be a palindrome. Write a program to take the pet name as input and print "true"
   if it is palindrome or print "false" on screen. Help Arunima to decide the name ( should be palindrome ) 
   sof the puppy. Hint: reverse the name and compare it with the original name"""


def palindrome(word):

    word = word.lower()

    reversed_word =  word[::-1]

    return word == reversed_word

pet_name = input()



if palindrome(pet_name):
    print("True")
else:
    print("False")