import random
import string

def yes_no():
    print("Do you want a specific word to be in your passowrd?")
    
    user_input = input("(yes/no)")
    
    if user_input == "yes":
        word = input("Please enter your word. ")
     
