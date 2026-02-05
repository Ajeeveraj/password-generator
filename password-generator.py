 #import
import random
import string
# Yes or no responses
def yes_no():
    while True:
        
        while True:
            
            user_input = input("Would you like to have a specific word in your password.(yes/no) ").lower().strip()
            password = ""
            
            if user_input == "yes":
                
                print("Okay, we'll add that word to your password.")
                password = input("Please enter your word. ")
                break
            elif user_input == "no":
                print("Okay, your password will be entirely random.")
                break
            else:
                print("Thats not a valid answer.")
            
# Asking the second question
        while True:
            upper_case = input("Would you like uppercase letters in your password? (yes/no)").lower().strip()
            
            if upper_case == "yes":
                characters = string.ascii_letters
                print("Your password will now have uppercased and lowercassed letters.")
                break
            elif upper_case == "no":
                characters = string.ascii_lowercase
                print("Okay, your password will be made up of only lowercase letters.")
                break
            else:
                print("Type yes or no.")
                

# Asking the third question
        while True:
            add_number = input("Do you want numbers in yoyur password (yes/no) ").lower().strip()

            if add_number == "yes":
                print("Okay, we will add numbers to your password.")
                break
            elif add_number == "no":
                print("Alright, your password will not have any numbers.")
                break
            else:
                print("Thats not a vaild answer!")
                
        
# Fourth question
        while True:
            add_symbols = input("Do you want symbols in your password? (yes/no)").lower().strip()

            if add_symbols == "yes":
                print("Okay, we will add symbols to your password.")
                break
            elif add_symbols == "no":
                print("Alright, there will not be symbols in your password.")
                break
            else:
                print("Thats not a valid answer!")
                
# Ask how many characters
        while True:
            char_length = input("How long do you want your passwowrd to be? (6-15)")

            try:
                char_length = int(char_length)
            
            except ValueError:
                print("Please enter a number.")
            
            if  6 <= char_length <= 15:
                break
             
                
# Run the program  
yes_no()






    
    
     
