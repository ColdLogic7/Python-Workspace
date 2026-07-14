# 1. Ask user for desired password length
# 2. Ask which character types to include (lowercase, uppercase, digits, symbols)
# 3. Build the character pool from chosen types
# 4. Generate the password from that pool
# 5. Display the password
# 6. Ask to generate another or exit

import string
import random

PASS_MENU = {
                  'L': 'Lowercase',
                  'U': 'Uppercase',
                  'D': 'Digits',
                  'S': 'Symbols',
                  'M':  'Mixed'
}
def pass_length():
    while True:
        try: 
            len_pass = int(input("\n 🤔 Choose PASSWORD LENGTH here [greater than 16]: ").strip())
            if len_pass < 16:
                print("\n ❌ Choose length greater than 16!") 
            else:
                return len_pass
        except ValueError:
            print("\n ❌ Please Enter a Number here")
    
def char_type():
    while True:
        choosen_char_type = input(f"\n 🧐 Choose CHARACTERS TYPE in MENU [default: mixed]: ").strip().upper() or 'M'
        if choosen_char_type not in PASS_MENU.keys():
            print("\n ❌ Error: Please choose letter in provided Menu")     
        else:
            return choosen_char_type
    
def char_pool(character_type):
    if character_type == 'L':
        return string.ascii_lowercase
    elif character_type == 'U':
        return string.ascii_uppercase
    elif character_type == 'D':
        return string.digits
    elif character_type == 'S':
        return string.punctuation
    elif character_type == 'M':
        return (string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)

def gen_pass(character_pool,length):
    create_pass = random.choices(character_pool,k=length)
    refined_pass = ''.join(create_pass)
    return refined_pass

def show_pass_menu():
    for key, val in PASS_MENU.items():
        print(f" \t {key} — {val} \n")

def main():
    print("\n----- 🔑 Password Generator Program -----\n")
    while True:
        print("🍔 PASSWORD MENU :")
        show_pass_menu()
        pass_char_type = char_type()
        password_length = pass_length()
        pass_char_pool = char_pool(pass_char_type)
        created_pass = gen_pass(pass_char_pool,password_length)
        print(f"\n \t 🍜 Your Password Generated: {created_pass} \n")

        play_again = input("\n 🙃 Do you want to CREATE ANOTHER PASSWORD [y/n]: ").strip().lower()
        if play_again != 'y':
            print("\n 🫡 Goodbye!")
            break

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n 🫡 Goodbye!")
