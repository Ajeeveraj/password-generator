import secrets #More safe than import random
import string

# Color coding
red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
cyan = "\033[96m"
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
    
    # difficulty to remember based on length
def password_memorability(final_password, special_word):
    score = 0

    if len(final_password) >= 14:
        score += 2
    elif len(final_password) >= 10:
        score += 1

    # difficulty to remmember baased on ammount of character types
    symbol_count = sum(1 for c in final_password if c in string.punctuation)
    if symbol_count >= 3:
        score += 2
    elif symbol_count >= 1:
        score += 1

    number_count = sum(1 for c in final_password if c.isdigit())
    if number_count >= 3:
        score += 2
    elif number_count >= 1:
        score += 1

    # harder to remember if no special word
    if not special_word:
        score += 2

    if score <= 2:
        return "Easy"
    elif score <= 5:
        return "Moderate"
    else:
        return "Hard"
    
    # Ask yes or no questions
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
    special_word = ""
    if ask_yes_no("Do you want a special word in your password? (yes/no)") == "yes":
        special_word = input("Enter your special word: ").strip()
        print(green + "Okay we will add that to the password." + reset)
    else:
        print(green + "Alright we will not add a special word to your password." + reset)
                
    # Mandatory characters
    mandatory_chars = []

    # Asking the secound question
    characters = string.ascii_lowercase
    if ask_yes_no("Do you want uppercase letters in your password? (yes/no)") == "yes":
        mandatory_chars.append(secrets.choice(string.ascii_uppercase))
        characters += string.ascii_uppercase
        print(green + "Okay we will add uppercase letters to your password." + reset)
    else:
        print(green + "Alright, there will not be uppercase letters in your password." + reset)

                        
    # Third question
    add_symbols = ask_yes_no("Do you want symbols in your password? (yes/no)")

    if add_symbols == "yes":
        symbols = string.punctuation
        print(green + "Okay, we will add symbols to your password." + reset)
    # Remove weird symbols
        remove_uncommon = ask_yes_no("Do you want to remove uncommon symbols? (yes/no)")

        if remove_uncommon == "yes":
            allowed = "!@#$%&*?-_=+"
            symbols = "".join(c for c in symbols if c in allowed)
            print(green + "Uncommon symbols removed" + reset)

        characters += symbols
        mandatory_chars.append(secrets.choice(symbols))
    else:
        print(green + "Alright there will not be symbols in your password." + reset)

    # Fourth question
    add_numbers = ask_yes_no("Do you want numbers in your password? (yes/no) ")

    if add_numbers == "yes":
        characters += string.digits
        mandatory_chars.append(secrets.choice(string.digits))
        print(green + "Great! Your password will include numbers." + reset)
    else:
        print(green + "Okay your password will not include numbers!" + reset)
    
    

    # Ask how many characters
    while True:
        password_length = input("How long do you want your passwowrd to be? (6-15) ")
        try:
            password_length = int(password_length)
            if 6 <= password_length <= 15:
                break
            else:
                print(red + "Enter a number between 6-15." + reset)
        except ValueError:
            print(red + "Please enter a number." + reset)


    # make sure the special word isn't longer than the password
    if len(special_word) > password_length:
        print(red + "Your special word was longer than the total password length." + reset)
        return


    # Generate the password

    remaining_length = password_length - len(special_word) - len(mandatory_chars)

    if remaining_length < 0:
        print(red + "Password length is too short for the special word and mandatory characters." + reset)
        return
    
    random_chars = "".join(secrets.choice(characters) for _ in range(remaining_length))

    other_chars = list("".join(mandatory_chars) + random_chars)
    secrets.SystemRandom().shuffle(other_chars)

    final_password = special_word + "".join(other_chars)
    print("Your final password is...")
    print(cyan + final_password + reset)

    strength = password_strength(final_password)

    # Check memorability
    memorability = password_memorability(final_password, special_word)
    
    # Add password to history
    password_history.append(final_password)
    
    
    # show strength and return colors
    if strength == "Strong":
        color = "\033[92m"
    elif strength == "Decent":
        color = "\033[93m"
    else:
        color = "\033[91m"
        

    print("Password strength:", color + strength + reset)

    # Show memorability
    if memorability == "Easy":
        mem_color = green
    elif memorability == "Moderate":
        mem_color = yellow
    else:
        mem_color = red

    print("Difficulty to remember:", mem_color + memorability + reset)

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
        print(green +"\n Password Generator Menu" + reset)
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
            break
        else:
            print(red + "Please enter 1,2, or 3" + reset)

main_menu()










    
    
     
