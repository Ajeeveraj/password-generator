import secrets #More safe than import random
import string

# Color coding
colors = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "cyan": "\033[96m",
    "reset": "\033[0m"
}



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

    # scoring results
    return "Weak" if score <= 2 else ("Decent" if score <= 4 else "Strong")


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
            print(colors["red"] + "Please type yes or no."+ colors["reset"])

# Defining password generator function
def generate_password(password_history):

    # Ask if user wants a special word
    special_word = ""
    if ask_yes_no("Do you want a special word in your password? (yes/no)") == "yes":
        special_word = input("Enter your special word: ").strip()
        print(colors["green"] + "Okay we will add that to the password." + colors["reset"])
    else:
        print(colors["green"] + "Alright we will not add a special word to your password." + colors["reset"])
                
    # Mandatory characters
    mandatory_chars = []

    # Asking the secound question
    characters = string.ascii_lowercase
    if ask_yes_no("Do you want uppercase letters in your password? (yes/no)") == "yes":
        mandatory_chars.append(secrets.choice(string.ascii_uppercase))
        characters += string.ascii_uppercase
        print(colors["green"] + "Okay we will add uppercase letters to your password." + colors["reset"])
    else:
        print(colors["green"] + "Alright, there will not be uppercase letters in your password." + colors["reset"])

                        
    # Third question
    add_symbols = ask_yes_no("Do you want symbols in your password? (yes/no)")

    if add_symbols == "yes":
        symbols = string.punctuation
        print(colors["green"] + "Okay, we will add symbols to your password." + colors["reset"])
    # Remove weird symbols
        remove_uncommon = ask_yes_no("Do you want to remove uncommon symbols? (yes/no)")

        if remove_uncommon == "yes":
            allowed = "!@#$%&*?-_=+"
            symbols = "".join(c for c in symbols if c in allowed)
            print(colors["green"] + "Uncommon symbols removed" + colors["reset"])

        characters += symbols
        mandatory_chars.append(secrets.choice(symbols))
    else:
        print(colors["green"] + "Alright there will not be symbols in your password." + colors["reset"])

    # Fourth question
    add_numbers = ask_yes_no("Do you want numbers in your password? (yes/no) ")

    if add_numbers == "yes":
        characters += string.digits
        mandatory_chars.append(secrets.choice(string.digits))
        print(colors["green"] + "Great! Your password will include numbers." + colors["reset"])
    else:
        print(colors["green"] + "Okay your password will not include numbers!" + colors["reset"])
    
    

    # Ask how many characters
    while True:
        password_length = input("How long do you want your passwowrd to be? (6-15) ")
        try:
            password_length = int(password_length)
            if 6 <= password_length <= 15:
                break
            else:
                print(colors["red"] + "Enter a number between 6-15." + colors["reset"])
        except ValueError:
            print(colors["red"] + "Please enter a number." + colors["reset"])

    # Checking special word and added characters isn't longer than password length
    if len(special_word) + len(mandatory_chars) > password_length:
        print(colors["red"] + "Password length is too short for special word and mandatory characters.")
        return
    
    # Generate password
    remaining_length = password_length - len(special_word) - len(mandatory_chars)
    random_chars = "".join(secrets.choice(characters) for _ in range(remaining_length))
    other_chars = list("".join(mandatory_chars) + random_chars)
    secrets.SystemRandom().shuffle(other_chars)

    final_password = special_word + "".join(other_chars)
    print("Your final password is...")
    print(colors["cyan"] + final_password + colors["reset"])

    strength = password_strength(final_password)

    # Check memorability
    memorability = password_memorability(final_password, special_word)

    #password statistics
    password_stats = {
        "uppercase": sum(c.isupper() for c in final_password),
        "lowercase": sum(c.islower() for c in final_password),
        "digits": sum(c.isdigit() for c in final_password),
        "symbols": sum(c in string.punctuation for c in final_password)
    }
    
    # Add password to history
    password_history.append({
        "password": final_password,
        "strength": strength,
        "memorability": memorability,
        "length": len(final_password),
        "stats": password_stats
    })
    
    
    # show strength and return colors
    strength_colors = {
        "Strong": colors["green"],
        "Decent": colors["yellow"],
        "Weak": colors["red"]
    }

    color = strength_colors[strength]
        

    print("Password strength:", color + strength + colors["reset"])

    # Show memorability
    memorability_colors = {
        "Easy": colors["green"],
        "Moderate": colors["yellow"],
        "Hard": colors["red"]
    }

    mem_color = memorability_colors[memorability]

    print("Difficulty to remember:", mem_color + memorability + colors["reset"])

# view password history
def view_history(password_history):
    if not password_history:
        print(colors["red"] + "You have no passwords!" + colors["reset"])
        return
    print("\nPassword history:")
    for index, entry in enumerate(password_history, start=1):
        print(f"{index}. {entry['password']}")
        print(f" Strength: {entry['strength']}")
        print(f" Memorability: {entry['memorability']}")
        print(f" Length: {entry['length']}")

        stats = entry["stats"]
        print(f" Stats: UPPER={stats['uppercase']}, "
              f"lower={stats['lowercase']}, "
              f"digits={stats['digits']}, "
              f"symbols={stats['symbols']}")

   
# Main menu
def main_menu():
    password_history = []

    menu_options = (
    ("1", "Generate a new password", generate_password),
    ("2", "View password history", view_history),
    ("3", "Exit", None)
    )

    while True:
        print(colors["green"] +"\n Password Generator Menu" + colors["reset"])

        # display menu
        for num, description, _ in menu_options:
            print(f"{num}. {description}")

        choice = input("Enter your choice (1,2, or 3): ").strip()

        for number, _, funct in menu_options:
            if choice == number:
                if funct:
                    funct(password_history)
                else:
                    print(colors["green"] + "Thank you for using the password generator!" + colors["reset"])
                    return
                break
        else:
            print(colors["red"] + "Please enter one of the options" + colors["reset"])
main_menu()










    
    
     
