import json

SEPARATOR = '-'*30
SMALL_SEP = '-'*5

def write_json(data):
    with open('report.json','w',encoding='utf-8') as file:
        json.dump(data,file,indent=2)

def read_json():
    try:
        with open('report.json','r',encoding='utf-8') as file:
            return json.load(file)       
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def print_menu():
    print("\n⚙️  Menu -")
    menu_items = ['Add Subject', 'View Full Report', 'View Summary', 'Update Subject Marks', 'Delete Subject', 'Exit']
    for idx, item in enumerate(menu_items,start=1):
        print(f"\t [{idx}] {item}")
    print(SEPARATOR)

def validate_choices():
    while True:
        try:
            choose_opt = int(input("Choose an Option [1-6]: ").strip())
            if 1 <= choose_opt <= 6:
                return choose_opt
            else:
                print("❌ Please Enter a Valid Number! ")
        except ValueError:
            print("❌ Please Enter a Valid Number! ")

def calculate_grade(marks):
    if 90 <= marks <= 100:
        return "Outstanding", "A+", "Pass"
    if 80 <= marks < 90:
        return "Excellent", "A", "Pass"
    if 70 <= marks < 80:
        return "Good", "B", "Pass"
    if 60 <= marks < 70:
        return "Average", "C", "Pass"
    if 50 <= marks < 60:
        return "Below Average", "D", "Pass"
    if 33 <= marks < 50:
        return "Needs Work", "E", "Pass"
    if 0 <= marks < 33:
        return "Fail", "F", "Fail"
    return "Unknown", "N/A", "Invalid"
    


def add_subject():
    file_data = read_json()
    subject_data = {}
    print(f"\n {SMALL_SEP} ➕  Add Subject {SMALL_SEP} ")
    while True:
        try:
            subject_count = int(input("\n 📍 How many subject you have [default: 3]: ").strip() or '3')
            if subject_count > 0:
                break
            print(f"❌ Please enter a number greater than 0.")
        except ValueError:
            print("❌ Please Enter Valid Subject Count.")

    i = 1
    while i <= subject_count:
        print(f"\n💡 Subject - {i} ")
        try:
            add_subj = input("\n📚 Enter your subject name here: ").strip().title()
            add_marks = int(input(f"📊 Enter percentage for {add_subj} 0-100]: ").strip())
            if 0 <= add_marks <= 100 and add_subj:
                existing_names = [item['subject'] for item in file_data]
                if add_subj not in subject_data and add_subj not in existing_names:
                    subject_data[add_subj] = add_marks
                    print(f"\n -[✅ Added - {add_subj}]-")
                    i += 1
                else:
                    print(f"[SKIPPED] - {add_subj} already exists in data")
            else:
                print("❌ Please Enter a Valid Subject and Marks")
        except ValueError:
            print("❌ Please Enter a Valid Subject and Marks")

    for subj_name, subj_mark in subject_data.items():
        grade_mean, grade, status = calculate_grade(subj_mark)
        subject = {"subject": subj_name, "marks": subj_mark, "grade": f"{grade} ({grade_mean})", "status": status}
        file_data.append(subject)

    print(SEPARATOR)
    write_json(file_data) # Save to JSON
    print("\n -[✅ All Subjects Added Successfully]-")



def view_full_report():

    file_data = read_json()
    total_marks = 0
    total_subj = len(file_data)

    print(f"\n {SMALL_SEP} 📋 Grade Report {SMALL_SEP} ")
    if not file_data:
        print("\n ❌ No Subject Found!")
        return
    

    print(f"{'#':<2}  {'Subject':<9}  {'Marks':<5}  {'Grade (Meaning)':<19}  {'Status'}")
    for idx, item in enumerate(file_data,start=1): # Aligned columns
        print(f"{idx:<2}  {item['subject']:<9}  {item['marks']:<5}  {item['grade']:<19}  {item['status']}")
        total_marks += item['marks']

    print(SEPARATOR)
    total_percentage =  round(total_marks / (total_subj * 100) * 100, 2)
    print(f"🔥 Overall Percentage: {total_percentage}%")
    all_passed = all(item['status'] == 'Pass' for item in file_data)
    print("⚖️ Final Result: " + ('pass' if all_passed else 'fail')) 

def view_summary():
    file_data = read_json()
    total_marks = 0
    total_subj = len(file_data)
    pass_subj = 0

    print(f"\n{SMALL_SEP} 📝 Report Summary {SMALL_SEP}")
    if not file_data:
        print("\n ❌ No Subject Found!")
        return
    
    print(f"\n📊 Total subjects added: {total_subj}")

    for item in file_data:
        total_marks += item['marks']
        if item['status'] == 'Pass':
            pass_subj += 1

    total_percentage =  round(total_marks / (total_subj * 100) * 100, 2)
    print(f"🔥 Overall percentage: {total_percentage}%")

    strong_subj = max(file_data, key=lambda x: x['marks'])
    weak_subj = min(file_data, key=lambda x: x['marks'])
    print(f"📈 Strongest subject: {strong_subj['subject']} ({strong_subj['marks']}%) - {strong_subj['grade']}")
    print(f"📉 Weakest Subject: {weak_subj['subject']} ({weak_subj['marks']}%) - {weak_subj['grade']}")

    print(f"\n⚖️  You Passed: {pass_subj} & Failed: {total_subj - pass_subj}")

def update_subject():
    file_data = read_json()

    print(f"\n{SMALL_SEP} ⚡ Update Subject {SMALL_SEP}")
    if not file_data:
        print("\n ❌ No Subject Found!")
        return

    print("\n📝 Select Subjects:")
    print(f"\t {'#':<4} {'Subject':<10} {'Marks'}")
    for idx, item in enumerate(file_data,start=1):
        print(f"\t {idx:<4} {item['subject']:<10} {item['marks']}")

    while True:
        try:
            pick_subj_idx = int(input(f'\n📌 pick a subject (to update) by index number [1/{len(file_data)}]: ').strip())
            new_marks = int(input("✏️  Enter new marks here [0/100]: ").strip())   # Enter new marks
            if 1 <= pick_subj_idx <= len(file_data) and 0 <= new_marks <= 100:
                break
            else:
                print("❌ Please Enter a Valid Number! ")
        except ValueError:
            print("❌ Please Enter a Valid Number! ")

    target_item = file_data[pick_subj_idx - 1]
    new_mean, new_grade, new_status = calculate_grade(new_marks)

    target_item['marks'] = new_marks
    target_item['grade'] = f"{new_grade} ({new_mean})"
    target_item['status'] = new_status

    write_json(file_data)
    print("\n -[✅ Update Marks Successfully]-")

def delete_subject():
    file_data = read_json()

    
    print(f"\n{SMALL_SEP} 🗑️  Delete Subject {SMALL_SEP}")
    if not file_data:
        print("\n ❌ No Subject Found!")
        return
    
    print("\n📝 Select Subject:")

    print(f"\t {'#':<4} {'Subject':<10} {'Marks'}")
    for idx, item in enumerate(file_data,start=1):
        print(f"\t {idx:<4} {item['subject']:<11} {item['marks']}")

    while True:
        try:
            pick_subj_idx = int(input(f'\n📌 pick a subject (to Delete) by index number [1/{len(file_data)}]: ').strip())
            if 1 <= pick_subj_idx <= len(file_data):
                del_subj_name = file_data[pick_subj_idx - 1]
                break
            else:
                print("❌ Please Enter a Valid Number! ")
        except ValueError:
            print("❌ Please Enter a Valid Number! ")

    del_confirmm = input(f"❓ Confirm deletion of {del_subj_name['subject']} [y/n] [default: yes]: ").strip().lower() or 'y'

    if del_confirmm == 'y':
        try:
            del file_data[pick_subj_idx - 1]
            write_json(file_data)
            print(f"\n ✅ Deleted {del_subj_name['subject']} successfully")
        except Exception as e:
            print(f"\n ❌ Something Went Wrong: {e}")
    else:
        print(f"\n ⚠️  {del_subj_name['subject']}  - Not Deleted.")


def main():
    print(f"\n{SMALL_SEP} 🎓 Student Grade Report {SMALL_SEP}")
    while True:
        print_menu()
        opt_no = validate_choices()
        if opt_no == 1:
            add_subject()
        elif opt_no == 2:
            view_full_report()
        elif opt_no == 3:
            view_summary()
        elif opt_no == 4:
            update_subject()
        elif opt_no == 5:
            delete_subject()
        elif opt_no == 6:
            print("\n👋 Exiting...")
            exit(0)
        print(SEPARATOR)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Exiting...")
        exit(0)