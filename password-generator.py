 #import
import random
import string

# Password strength checker
def password_strength(ps):
    score = 0
    
    if len(ps) >= 12:
        score += 2
    elif len(ps) >= 8:
        score += 1

# Character scoring
    if any(char.isupper() for char in ps):
        score += 1
    if any(char.islower() for char in ps):
        score += 1
    if any(char.isdigit() for char in ps):
        score += 1
    if any(char in string.punctuation for char in ps):
        score += 1

# defining scoring
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Decent"
    else:
        return "Strong"

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
                print("Your password will now have uppercased and lowercased letters.")
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
                characters += string.digits
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
                characters += string.punctuation
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
            
                if  6 <= char_length <= 15:
                    break
                else:
                    print("Enter a number between 6-15.")
            except ValueError:
                print("Please enter a number.")

# make sure the special word isn't longer than the password
        if len(password) > char_length:
            print("Your special word was longer than the total password lengtg.")
            continue


# Generate the password
        random_char = ""
        
        for _ in range(char_length - len(password)):
            random_char += random.choice(characters)

        final_password = password + random_char
        print("Your final passowrd is ")
        print(final_password)

        strength = password_strength(final_password)
        print("Password_strength:", strength)
           
                
# Run the program  
yes_no()






    
    
     
