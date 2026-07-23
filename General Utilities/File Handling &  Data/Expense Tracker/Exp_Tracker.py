import csv
from datetime import date
import os

SEPARATOR = '-'*30

def print_menu():
    print('[1] Add Expense')
    print('[2] View All Expense')
    print('[3] View Summary')
    print('[4] Delete Expense')
    print('[5] Exit')
    print(SEPARATOR)

def op_num():
    while True:
        try:
            operation_num = int(input("\n 🛠️  Choose An Option [1-5]: "))
            if 1 <= operation_num <= 5:
                return operation_num
            else:
                print("\n ❌ Please Choose A Valid Number!")
        except ValueError:
            print("\n ❌ Please Choose A Valid Number!")

def expense_category():
    print("\n📂 Select Category:")
    category = ['Food', 'Transport', 'Shopping', 'Bills', 'Health', 'Other']
    for i, item in enumerate(category,start=1):
        print(f"{i}. {item}")
    while True:    
        try:
            choose_option = int(input("👉 Choose category [1-6]: ").strip())
            if 1 <= choose_option <= 6:
                return category[choose_option - 1]
            else:
                print("\n ❌ Please Choose A Valid Number Between 1-6")
        except ValueError:
            print("\n ❌ Please Choose A Valid Number Between 1-6")

def add_expense_variable():
    while True:
        try:
            product_amt = float(input("\n💸 Enter Amount(₹): ").strip())
            if product_amt > 0:
                round_amt = round(product_amt,2)
                break
            else:
                print("\n ❌ Please Enter Valid Amount!")
        except ValueError:
            print("\n ❌ Please Enter Valid Amount!")
    product_desc = input("📝 Enter Description: ").strip()
    todays_date = date.today()
    return round_amt, product_desc, todays_date


def add_expense(todays_date, chosen_category, round_amt, product_desc):
    file_is_empty = not os.path.exists('expense.csv') or os.path.getsize('expense.csv') == 0

    with open('expense.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Date', 'Category', 'Amount(₹)', 'Description'])
        if file_is_empty:
            writer.writeheader()
        writer.writerow({'Date': todays_date, 'Category': chosen_category, 'Amount(₹)': round_amt, 'Description': product_desc})
    print("\n ✅ Expense Saved Successfully!")

def view_exp():
    print("\n📋 All Expenses:")
    print(SEPARATOR)

    total_exp_amt = 0.0
    try:
        with open('expense.csv', newline='', encoding='utf-8', mode='r') as file:
            reader = csv.DictReader(file)
            header = reader.fieldnames
            rows = list(reader)
    except FileNotFoundError:
        print("\n 🥺 No Records Found!")
        return
    
    if len(rows) == 0:
        print("\n 🥺 No Records Found, Please Add At Least One Expense!")
    else:
        all_rows_data = [header] + [list(row.values()) for row in rows] # header + row data
        col_width = [max(len(cell) for cell in col) for col in zip(*all_rows_data)] # one column in (header + column), one cell in one column, maximum length of a cell in numbers. 
        formatted_header = [f'{cell:<{col_width[idx]}}' for idx, cell in enumerate(header)] # aligning header cell object on left by adding empty spaces to the right until its maximum width.
        print(" | ".join(formatted_header))

        for row in rows:
            formatted_row = [f"{cell:<{col_width[idx]}}" for idx, cell in enumerate(row.values())]
            print(' | '.join(formatted_row))
            total_exp_amt += float(row['Amount(₹)'])

    print(SEPARATOR)
    print(f"\n 💵 Total Expenses: ₹{total_exp_amt}")

def view_summary():
    print(f"\n 📊 Expense Summary: ")
    print(SEPARATOR)

    grand_total = 0.0
    category_totals = {}

    try:
        with open('expense.csv', newline='', encoding='utf-8', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                category = row.get('Category')
                try:
                    amount = float(row.get('Amount(₹)',0.0))
                except ValueError:
                    amount = 0.0

                category_totals[category] = category_totals.get(category, 0.0) + amount # It handles two things simultaneously: 1) add new entry in dictionary && 2) calculate existing entry
                grand_total += amount
    except FileNotFoundError:
        print("\n 🥺 No Records Found!")
        return
    
    if grand_total == 0:
        print("\n 🥺 No Records Found, Please Add At Least One Expense!")
    else:
        for category, total in category_totals.items():
            percentage = (total/grand_total) * 100
            print(f"{category:<14}    ₹{total:<10.2f}    ({percentage:>5.1f}%)")
        
    print(SEPARATOR)
    print(f"Total:     ₹{grand_total}")

def delete_exp():
    print("\n 📋 Current Expenses:")
    print(SEPARATOR)

    try:
        with open('expense.csv', newline='', encoding='utf-8', mode='r') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
    except FileNotFoundError:
        print("\n 🥺 No Records Found!")
        return
    
    if len(rows) == 0:
        print("\n 🥺 No Records Found, Please Add At Least One Expense!")
    else:
        for idx, row in enumerate(rows, start=1):
            print(f"[{idx}]  {row['Date']:<10} | {row['Category']:<10}  | {row['Description']:<30} ")

    while True:
        try:
            remove_idx = int(input(f"\n 🗑️  Enter expense number to delete [1-{len(rows)}]: "))
            if 1 <= remove_idx <= len(rows):
                del rows[remove_idx - 1]
                break
            else:
                print("\n ❌ Please Enter A Valid Number!")
        except ValueError:
            print("\n ❌ Please Enter A Valid Number!")

    with open('expense.csv','w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Date', 'Category', 'Amount(₹)', 'Description'])

        writer.writeheader()
        writer.writerows(rows)
    
    print("\n ✅ Expense Deleted Successfully!")

def main():
    while True:
        print("\n ------ 💰 Expense Tracker ------ \n")
        print_menu()         
        operation_num = op_num()
        if operation_num == 1:
            category_num = expense_category()
            amount, description, today_date = add_expense_variable()
            add_expense(today_date,category_num,amount,description)

        elif operation_num == 2:
            view_exp()

        elif operation_num == 3:
            view_summary()

        elif operation_num == 4:
            delete_exp()
            
        elif operation_num == 5:
            print("\n👋 Goodbye!")
            exit(0)

        rerun_program = input("\n🤔 Do you want to do other operations [y/n]: ").strip().lower()
        if rerun_program != 'y':
            print("\n👋 Goodbye!")
            exit(0)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
        exit(0)
