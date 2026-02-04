 #import
import random
import string
#Yes or no responses
def yes_no():
    print("Do you want a specific word to be in your password?")
    
    user_input = input("(yes/no)")
    password = ""
    
    if user_input == "yes":
        print("Okay, we'll add that word to your password.")
        password = input("Please enter your word. ")
    elif user_input == "no":
        print("Okay, your password will be entirely random.")
    else:
        print("Thats not a valid answer.")
        return
# Asking the second question
    upper_case = input("Would you like uppercase letters in your password? (yes/no)")
    
    if upper_case == "yes":
        characters = string.ascii_letters
        print("Your password will now have uppercased and lowercassed letters.")
    elif upper_case == "no":
        characters = string.ascii_lowercase
        print("Okay, your password will be made up of only lowercase letters.")
    else:
        print("Type yes or no.")
        return

# Asking the third question
    add_number = input("Do you want numbers in yoyur password (yes/no) ")

    if add_number == "yes":
        print("Okay, we will add numbers to your password.")
    elif add_number == "no":
        print("Alright, your password will not have any numbers.")
    else:
        print("Thats not a vaild answer!")
        return
    
#Fourth question
    add_symbols = input("Do you want symbols in your password? (yes/no)")

    if add_symbols == "yes":
        print("Okay, we will add symbols to your password.")
    elif add_symbols == "no":
        print("Alright, there will not be symbols in your password.")
    else:
        print("Thats not a valid answer!")
        return




    
    
     
