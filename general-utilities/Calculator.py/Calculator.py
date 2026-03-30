'''This is my first project as beginner in python and I know it's very basic project but It's crucial for my future '''
# Functions Room where we create functions for our work

def add(n1,n2):
    result = n1 + n2
    return result

def subtract(n1,n2):
    result = n1 - n2
    return result

def multiply(n1,n2):
    result = n1 * n2
    return result

def divide(n1,n2):
    if n2 == 0:
        print("Error: Cannot divide by 0 .")
        return None
    result = n1 / n2
    return result

def square(n1):
    result = n1 * n1
    return result

def Radical_value(number,i=2):
    if number == 0:
        print("Please enter positive number , not zero 😌")
        return None
    return number**(1/i)

def Multiple_addition(n1, n2):
    sum_total = n1 + n2
    print(f"\nIt's your previous summation: {sum_total}")
    print("\nINSTRUCTION: If you want to stop this process, Enter 4 times zero below (0000)")
    while True:
        next_input = input("\nEnter your next number here, which you want to add: ")
        if next_input == "0000":
            print("\nYou are aborting further process......")
            print(f"\nYour grand total is: {sum_total}")
            break
        try:
            next_number = int(next_input)
            sum_total += next_number
            print(f"\nIt's your previous summation: {sum_total}")

        except ValueError:
            print("Please enter a valid number.")
           
def Multiple_subtraction(n1, n2):
    subtract_total = n1 - n2
    print(f"\nIt's your previous subract: {subtract_total}")
    print("\nINSTRUCTION: If you want to stop this process, Enter 4 times zero below (0000)")
    while True:
        next_input = input("\nEnter your next number here, which you want to subtract: ")
        if next_input == "0000":
            print("\nYou are aborting further process......")
            print(f"\nYour grand total of subtraction is: {subtract_total}")
            break
        try:
            next_number = int(next_input)
            subtract_total -= next_number
            print(f"\nIt's your previous Subtraction: {subtract_total}")

        except ValueError:
            print("Please enter a valid number.")

def Multiple_multiplication(n1, n2):
    multiplication_total = n1 * n2
    print(f"\nIt's your previous multilication: {multiplication_total}")
    print("\nINSTRUCTION: If you want to stop this process, Enter 4 times zero below (0000)")
    while True:
        next_input = input("\nEnter your next number here, which you want to : ")
        if next_input == "0000":
            print("\nYou are aborting further process......")
            print(f"\nYour grand total of multiplication is: {multiplication_total}")
            break
        try:
            next_number = int(next_input)
            multiplication_total *= next_number
            print(f"\nIt's your previous multiplication: {multiplication_total}")

        except ValueError:
            print("Please enter a valid number.")


def Multiple_division(n1, n2):
    # Initial division needs a ZeroDivisionError check for n2
    if n2 == 0:
        print("Error: Cannot start with division by zero.")
        return None # Or handle the error as you prefer

    division_total = n1 / n2
    print(f"\nIt's your previous Division : {division_total}")
    print("\nINSTRUCTION: If you want to stop this process, Enter 4 times zero below (0000)")
    while True:
        next_input = input("\nEnter your next number here, which you want to divide by: ") # Better prompt
        if next_input == "0000":
            print("\nYou are aborting further process......")
            print(f"\nYour grand total of Division is: {division_total}")
            break
        try:
            next_number = int(next_input)
            
            # CHECK FOR ZERO DIVISION INSIDE THE LOOP
            if next_number == 0:
                print("Error: Cannot divide by zero. Please enter a non-zero number.")
                continue # Skip the rest of the loop and ask for input again
            
            division_total /= next_number
            print(f"\nIt's your previous Division: {division_total}")

        except ValueError :
            print("Please enter a valid number.")
# Main Room where we interact with user

def main():
    user_greeting = '''Hello👋 ,Welcome in My Basic Calculator program 
                    So , what we do today , Here is options:
                        1 - ADDition
                        2 - Subtraction
                        3 - Multiplication
                        4 - Division
                        5 - Multiple Addition
                        6 - Multiple Subtraction
                        7 - Multiple Multiplication
                        8 - Multiple Division
                        9 - Calculate Square like (12 = 144) 
                        10 - Calculate Radical value (√) like (√144 = 12)'''
    print(user_greeting)

    try:
        choose_option = int(input(" \nEnter your operation through it's correcponding number: "))
        if choose_option == 1:
                num1 = int(input("\n Enter your First number for Addition: "))
                num2 = int(input("\n Enter your Second number for Addition: "))
                result_of_add = add(num1,num2)
                print(f"\n It's your Addition answer: {result_of_add}")
        elif choose_option == 2:
                num1 = int(input("\n Enter your First number for Subtraction: "))
                num2 = int(input("\n Enter your Second number for Subtraction: "))
                result_of_subtract = subtract(num1,num2)
                print(f"\n It's your Subtraction answer: {result_of_subtract}")
        elif choose_option == 3:
                num1 = int(input("\n Enter your First number for Multiplication: "))
                num2 = int(input("\n Enter your Second number for Multiplication: "))
                result_of_multiply = multiply(num1,num2)
                print(f"\n It's your Multiplication answer: {result_of_multiply}")
        elif choose_option == 4:
                num1 = int(input("\n Enter your First number for Division: "))
                num2 = int(input("\n Enter your Second number for Division: "))
                result_of_divide = divide(num1,num2)
                print(f"\n It's your Division answer: {result_of_divide}")
        elif choose_option == 5:
                num1 = int(input("\n Enter your number for Adding: "))
                num2 = int(input("\n Enter your next number for Adding: "))
                further_multiple_addition = Multiple_addition(num1,num2)
        elif choose_option == 6:
                num1 = int(input("\n Enter your number for Subtraction: "))
                num2 = int(input("\n Enter your next number for Subtraction: "))
                further_multiple_subtraction = Multiple_subtraction(num1,num2)
        elif choose_option == 7:
                num1 = int(input("\n Enter your number for Multiplication: "))
                num2 = int(input("\n Enter your next number for Multiplicaion: "))
                further_multiple_multiplication = Multiple_multiplication(num1,num2)
        elif choose_option == 8:
                num1 = int(input("\n Enter your number for Multiplication: "))
                num2 = int(input("\n Enter your next number for Multiplicaion: "))
                further_multiple_division = Multiple_division(num1,num2)
        elif choose_option == 9:
                num = int(input("\n Enter your number which you want to find a square: "))
                print(f"\n It's your square which you want: {square(num)}")
        elif choose_option == 10:
                num1 = int(input("\n Enter which number you want to find square root (like 144 = 12): "))
                num2_input = input("\n Enter for which root (e.g., 2 for square root, 3 for cube root) (default is 2): ")
                if num2_input.strip() == "":
                    result = Radical_value(num1) 
                else:
                    num2 = int(num2_input)
                    result = Radical_value(num1, num2)
                print(f"\n It's your square root value:{result} ")
    except ValueError:
        print("\n Just Choose suggested number please not anything else😅 ")
        exit()
        
if __name__ == "__main__":
    main()
