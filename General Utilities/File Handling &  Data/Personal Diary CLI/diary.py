# 1. Show a menu: Add entry, Read entries, Delete entry, Exit
# 2. Add entry: get text from user, save with today's date to diary.txt
# 3. Read entries: open diary.txt and display all saved entries
# 4. Delete entry: show entries, ask which date to delete, rewrite file without it
# 5. Loop menu until user chooses Exit

import os
from datetime import date

DIARY_FILE = 'diary.txt'
SEPARATOR = '\n===\n'

def show_menu():
    print("[1] Write A New Entry")
    print("[2] View Past Entries")
    print("[3] Delete An Entry")
    print("[4] Exit")
    print("\n" + '-'*30)


def get_menu_choice():

    while True:
        try:  
            user_choice = int(input("\n 🛠️  Choose An Option [1,2,3,4]: ").strip())
            if 1 <= user_choice <= 4:
                return user_choice 
        except ValueError:
            print("\n ❌ Error: Please Enter A Valid Number Here!\n")
    
    

def add_entry():

    todays_date = date.today()

    user_entry = input("\n 💭 Write Your Thoughts: ").strip()

    if not user_entry:
        print("\n ⚠️ Cannot Save An Empty Entry!\n")
        return

    formatted_entry = f"\n --- {todays_date} ---\n{user_entry}{SEPARATOR}"

    with open(DIARY_FILE, 'a', encoding='UTF-8') as file:
        file.write(formatted_entry)
    print("\n ✅ Entry Saved Successfully!\n")

def read_entries():

    if not os.path.exists(DIARY_FILE):
        print("\n 🥺 No Entries Yet!\n")
        return

    with open(DIARY_FILE, 'r',encoding='UTF-8') as file: 
        content = file.read()
    
    entries = content.split(SEPARATOR)
    if not entries:
        print("\n 🥺 No Entries Yet!\n")
        return
    
    entries = [e.strip() for e in entries if e.strip()]

    for entry in entries:
        print(entry)
        print()

def delete_entry():

    if not os.path.exists(DIARY_FILE):
        print("\n 🥺 No Entries Yet!\n")
        return
    
    with open(DIARY_FILE, 'r',encoding='UTF-8') as file:
        content = file.read()

    entries = content.split(SEPARATOR)
    if not entries:
        print("\n 🥺 No Entries Yet!\n")
        return
    
    entries = [e.strip() for e in entries if e.strip()]

    # ----- Current Diary Entries ----
    for entry in entries:
        print(entry)
        print()

    delete_date = input("\n 🤔 Which Date's Entry Should I Delete, [YYYY-MM-DD]: ").strip()
    target_header = f"--- {delete_date} ---"
    remaining_entries = []
    entry_found = False
    for entry in entries: 
        if target_header in entry:
            entry_found = True
            continue #skipping this entry

        remaining_entries.append(entry + SEPARATOR)

    if entry_found:
        with open(DIARY_FILE, 'w', encoding='UTF-8') as file:
            file.writelines(remaining_entries) 
        print(f"\n ✅ Successfully Deleted The Entry For {delete_date} \n")
    else:
        print(f"\n ❌ Date Not Found: Could Not Find An Entry For {delete_date} \n")

def main():
    print("\n ------ 📔 Personal Diary ------")
    while True:
        show_menu()
        choice = get_menu_choice()
        if choice == 1:
            add_entry()
        elif choice == 2:
            read_entries()
        elif choice == 3:
            delete_entry()
        elif choice == 4:
            print("\n 👋 Goodbye!")
            break

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n 👋 Goodbye!")

        