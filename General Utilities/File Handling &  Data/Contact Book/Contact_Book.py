import json

SEPARATOR = '-'*30

def write_json(data):
    with open('contacts.json','w',encoding='utf-8') as file:
        json.dump(data,file,indent=2)

def read_json():
    try:
        with open('contacts.json','r',encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []

def print_menu():
    print(SEPARATOR)
    print('''
📋 Menu -
    [1] Add Contact
    [2] Search Contact
    [3] View All Contacts
    [4] Update Contact
    [5] Delete Contact
    [6] Exit
''')

def choose_operation():
    while True:
        try:
            chosen_option = int(input("🛠️  Choose An Option [1-6]: ").strip())
            if 1<= chosen_option <= 6:
                return chosen_option
            else:
                print("❌ Please Choose A Valid Number.")
        except ValueError:
            print("❌ Please Choose A Valid Number.")

def select_category():
    print("\n 📂 Select Category:")
    category = ['Friend','Family','Work','Other']

    for idx, item in enumerate(category,start=1):
        print(f"{idx}. {item}")

    while True:
        try:
            category_idx = int(input("👉 Choose [1-4]: ").strip())
            if 1 <= category_idx <= 4:
                return category[category_idx - 1]
            else:
                print("❌ Please Choose A Valid Number.")
        except ValueError:
            print("❌ Please Choose A Valid Number.")


def add_contact():
    print(SEPARATOR)
    print("\n➡️  Option Selected: Add Contact")
    while True:
        contact_name = input("👤 Enter Name: ").strip().title() or None
        contact_numb = input("📞 Enter Phone: ").strip() or None
        if not contact_name or not contact_numb:
            print("❌ Please Enter A Valid Number or Name")
        else:
            break
    contact_mail = input("📧 Enter Email (optional): ").strip() or None
    chosen_category = select_category()

    new_data = {
        "name": contact_name,
        "phone": contact_numb,
        "email": contact_mail,
        "category": chosen_category
    }

    file_data = read_json()
    file_data.append(new_data)
    write_json(file_data)
    
    print("\n ✅ Contact Saved Successfully!")
    

def search_contact():
    print(SEPARATOR)
    print("\n➡️  Option Selected: Search Contact")

    search_name = input("🔍 Enter Name to Search: ").strip()
    json_data = read_json()
    search_found = False

    print(f"\n Results for '{search_name}':")
    print(SEPARATOR)
    for item in json_data:
        full_name = item['name']
        if search_name.lower() in full_name.lower():
            search_found = True
            print(f"Name     : {item['name']}")
            print(f"Phone    : {item['phone']}")
            print(f"Email    : {item['email']}")
            print(f"Category : {item['category']}")

    if not search_found:
        print(f"\n 🥺 Not Found '{search_name}' In Our Contact Book")

def view_contact():
    print(SEPARATOR)
    file_content = read_json()
    print("\n➡️  Option Selected: View All Contacts")
    print(f"📋 All Contacts ({len(file_content)} total): ")
    print(SEPARATOR)

    if not file_content:
        print("\n 🥺 No Contacts Yet!")
        return
    
    print(f"{'#':<3}  {'Name':<17}  {'Phone':<17}  {'Category':<10}")

    for idx, item in enumerate(file_content,start=1):
        print(f"{idx:<3}  {item['name']:<17}  {item['phone']:<17}  {item['category']:<10}")

def choose_field():
    field = ['Name', 'Phone', 'Email', 'Category']
    for idx, item in enumerate(field,start=1):
        print(f"[{idx}] {item}")
    while True:
        try:
            field_idx = int(input("👉 Choose field [1-4]: ").strip())
            if 1 <= field_idx <= 4:
                return field[field_idx - 1]
            else:
                print("❌ Please Choose A Valid Number.")
        except ValueError:
            print("❌ Please Choose A Valid Number.")


def update_contact():
    print(SEPARATOR)
    print("\n➡️  Option Selected: Update Contact")

    entered_name = input("🔍 Enter name of contact to update: ").strip()
    json_data = read_json()

    update_check = False
    name_found = False

    for item in json_data:
        full_name = item['name']

        if entered_name.lower() in full_name.lower():
            print(f"Found: {full_name}")
            print("What do you want to update?")
            field = choose_field()
            name_found = True

            if field == 'Name':
                new_name = input("👤 Enter Name: ").strip().title()
                if new_name:
                    item['name'] = new_name
                    update_check = True
                
            elif field == 'Phone':
                new_number = input("📞 Enter new Phone: ").strip()
                if new_number:
                    item['phone'] = new_number
                    update_check = True
                                    
            elif field == 'Email':
                new_mail = input("📧 Enter Email: ").strip()
                if new_mail:
                    item['email'] = new_mail
                    update_check = True
            
            else:
                new_category = select_category()
                item['category'] = new_category
                update_check = True

            break

    if not name_found:
        print(f"\n 🥺 Not Found '{entered_name}' In Our Contact Book")
    elif not update_check:
        print("\n 🥺 No new update you made, try again")
    else:
        write_json(json_data) 
        print("\n ✅ Contact Updated Successfully!")

def delete_contact():
    print(SEPARATOR)
    print("\n➡️  Option Selected: Delete Contact")

    json_data = read_json()
    remove_name = input("🔍 Enter name of contact to delete: ").strip()
    delete_any = False

    for idx,item in enumerate(json_data):
        full_name = item['name']

        if remove_name.lower() in full_name.lower():
            category = item['category']
            contact_number = item['phone']

            print(f"\n Found: {full_name} | {contact_number} | {category}")
            confirmation = input(" Are you sure? [y/n]: ").strip().lower()

            if confirmation == 'y':
                delete_any = True
                json_data.pop(idx)
                write_json(json_data)
                print("\n ✅ Contact Deleted Successfully!")
                return

            else:
                print(f"\n ⬅️  Return To Menu")
                return

    if not delete_any:
        print(f"\n 🥺 Not Found '{remove_name}' In Our Contact Book")

def main():
    print("\n ------ 📒 Contact Book ------")
    while True:
        print_menu()
        choose_opt = choose_operation()
        if choose_opt == 1:
            add_contact()
        elif choose_opt == 2:
            search_contact()
        elif choose_opt == 3:
            view_contact()
        elif choose_opt == 4:
            update_contact()
        elif choose_opt == 5:
            delete_contact()
        else:
            print("\n Exiting....")
            exit(0)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n Exiting....")
        exit(0) 