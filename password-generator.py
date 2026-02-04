import random
import string
    #Yes or no responses
def yes_no():
    print("Do you want a specific word to be in your password?")
    
    user_input = input("(yes/no)")
    
    if user_input == "yes":
        print("Okay, we'll add that word to your password.")
        word = input("Please enter your word. ")
    elif user_input == "no":
        print("Okay, your password will be entirely random.")
    else:
        print("Thats not a valid answer.")
        return
    # Asking the second question
    upper_case = input("Would you like uppercase letters in your password? (yes/no)")
    
    if upper_case == "yes":
        print("Your password will now have uppercased and lowercassed letters.")
    elif upper_case == "no":
        print("Okay, your password will be made up of only lowercase letters.")
    else:
        print("Type yes or no.")
        return
    
    
     
