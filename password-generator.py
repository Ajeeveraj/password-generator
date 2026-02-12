import random
import string

# Color coding
red = "\033[91m"
green = "\033[92m"
orange = "\033[93m"
reset = "\033[0m"

# password history
password_history = []

# Password strength check
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

def ask_yes_no(prompt):
    while True:
        ans = input(prompt).lower().strip()
        if ans in ("yes", "no"):
            return ans
        else:
            print(red + "Please type yes or no."+ reset)


# Defining password generator function
def generate_password():
    # Ask if user wants a special word
    password = ""
    if ask_yes_no("Do you want a special word in your password? (yes/no)") == "yes":
        password = input("Enter your special word: ").strip()
        print(green + "Okay we will add that to the password." + reset)
    else:
        print(green + "Alright we will not add a special word to your password." + reset)
                

    # Asking the secound question
    characters = string.ascii_lowercase
    if ask_yes_no("Do you want uppercase letters in your password? (yes/no)") == "yes":
        characters += string.ascii_uppercase
        print(green + "Okay we will add uppercase letters to your password." + reset)
    else:
        print(green + "Alright, there will not be uppercase letters in your password." + reset)

                        
    # Third question
    add_symbols = ask_yes_no("Do you want symbols in your password? (yes/no)")
    if add_symbols == "yes":
        characters += string.punctuation
        print(green + "Okay, we will add symbols to your password." + reset)
    else:
        print(green + "Alright there will not be symbols in your password." + reset)

    # Fourth question
    if ask_yes_no("Do you want numbers in your password? (yes/no)") == "yes":
        characters += string.digits
    else:
        print(green + "Okay your password will not include numbers!" + reset)

    # Ask how many characters
    while True:
        char_length = input("How long do you want your passwowrd to be? (6-15)")
        try:
            char_length = int(char_length)
            if 6 <= char_length <= 15:
                break
            else:
                print(red + "Enter a number between 6-15." + reset)
        except ValueError:
            print(red + "Please enter a number." + reset)


    # make sure the special word isn't longer than the password
    if len(password) > char_length:
        print(red + "Your special word was longer than the total password length." + reset)
        return


    # Generate the password
    
    random_char = ""
    for _ in range(char_length - len(password)):
        random_char += random.choice(characters)

    final_password = password + random_char
    print("Your final passowrd is ")
    print(final_password)

    strength = password_strength(final_password)
    
    # Add password to history
    password_history.append(final_password)
    
    
    # show strength and return colors (need terminal in command prompt to see)
    if strength == "Strong":
        color = "\033[92m"
    elif strength == "Decent":
        color = "\033[93m"
    else:
        color = "\033[91m"
        

    print("Password strength:", color + strength + reset)

# view password history
def view_history():
    if not password_history:
        print(red + "You have no passwords!" + reset)
        return
    print("\nPassword history:")
    for index, pw in enumerate(password_history, start=1):
        print(f"{index}. {pw}")
# Main menu
def main_menu():
    while True:
        print("\n Password Generator Menu")
        print("1. Generate a new password")
        print("2. View password history")
        print("3. exit")
        choice = input("Enter your choice (1,2, or 3): ").strip()

        if choice == "1":
            generate_password()
        elif choice == "2":
            view_history()
        elif choice == "3":
            print(green + "Thank you for using the password generator!" + reset)
        else:
            print(red + "Please enter 1,2, or 3" + reset)

main_menu()










    
    
     
