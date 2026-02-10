import random
import string

# -----------------------------
# Password Strength Checker
# -----------------------------
def password_strength(ps):
    score = 0

    # Length scoring
    if len(ps) >= 12:
        score += 2
    elif len(ps) >= 8:
        score += 1

    # Character scoring
    if any(c.isupper() for c in ps):
        score += 1
    if any(c.islower() for c in ps):
        score += 1
    if any(c.isdigit() for c in ps):
        score += 1
    if any(c in string.punctuation for c in ps):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Decent"
    else:
        return "Strong"


# -----------------------------
# Ask Yes/No
# -----------------------------
def ask_yes_no(prompt):
    while True:
        ans = input(prompt).lower().strip()
        if ans in ("yes", "no"):
            return ans
        print("Please type yes or no.")


# Defining password generator function
def generate_password():
        # Ask if user wants a special word
        password = ""
        if ask_yes_no("Do you want a special word in your password? (yes/no)") == "yes":
            password = input("Enter your special word: ").strip()
            print("Okay we will add your special word to the password.")
        else:
            print("Alright we will not add a special word to your password.")
                

# Asking the secound question
    characters = string.ascii_lowercase
    if ask_yes_no("Do you want uppercase letters in your password? (yes/no)") == "yes":
        characters += string.ascii_uppercase
        print("Okay we will add uppercase letters to your password.")
    else:
        print("Alright, there will not be uppercase letters in your password.")

                
        
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
# Return colors (set terminal in command prompt to see)
        if strength == "Strong":
            color = "\033[92m"
        elif strength == "Decent":
            color = "\033[93m"
        else:
            color = "\033[91m"
        reset = "\033[0m"

        print("Password strength:", color + strength + reset)
        break      
                      
yes_no()










    
    
     
