# 1. Show the user a menu of operations (+, -, *, /)
# 2. Ask them to pick an operation
# 3. Ask for two numbers
# 4. Calculate the result using the chosen operation
# 5. Handle divide-by-zero gracefully
# 6. Show result, then ask to calculate again

OPERATIONS = ['+', '-', '*', '/']

def show_menu():
     print(f"\n Operations Menu : {OPERATIONS}")

def get_operation():
    while True:
            operation = input("\n \t Choose an operation: ")
            if operation in OPERATIONS:
                return str(operation)
            else:
                print("\n Error: Please Enter a Valid Operation From Menu")

def get_number(prompt):
    while True:
        try:
            user_num = float(input(f"\n \t Enter {prompt} number here: ").strip())
            return user_num
        except ValueError:
            print("\n Error: Please Enter a Valid Number")
    

def calculate(num1, num2, operation):
    if operation == '+':
         return num1 + num2
    elif operation == '-':
         return num1 - num2
    elif operation == '*':
         return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return None
        else:
            return num1 / num2
    
def main():
    print("\n - Welcome to our simple calculator program - ")
    while True:
        show_menu()
        n1 = get_number("first")
        operator = get_operation()
        n2 = get_number("second")
        result = calculate(n1,n2,operator)
        if result is None:
            print("\n \t -----------------------")
            print("\n \t Error: Division by Zero is not allowed!")
        else:
            print("\t -----------------------")
            roundOff_result = round(result,2)
            print(f"\n \t Result: {roundOff_result}")
        play_again = input("\n Do you want to play it again [y/n]: ").lower().strip()
        if play_again != 'y':
            print("\n Goodbye!")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n Goodbye!")