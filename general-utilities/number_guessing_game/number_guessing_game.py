import random

def greeting_and_rules():
    print('''\n \t 👋 Hello, Welcome to my Number Guessing Game!
    Rules:
      1. Choose a number between 1 and 100.
      2. I will also choose a number between 1 and 100.
      3. You have 10 chances to guess my number.
      4. After each guess, I'll give you a hint.
      5. Enjoy!''')
def main():
    greeting_and_rules()
    our_decided_number = random.randrange(1,100)
    counter = 1
    while counter < 10:
        try:
            user_decided_number = int(input("\n Enter your number: "))
        except ValueError:
            print("\n Error: Enter a Valid Number")
        if user_decided_number < 1 or user_decided_number > 100 :
                print("\n It is Out of range number.......")
                continue
        if user_decided_number == our_decided_number:
                print(f"\n Congratulation , I don't believe that you guess the exact number which is :{our_decided_number}")
                break
        elif user_decided_number < our_decided_number:
                print("\n It is too small , think a little bit bigger number........")
        else :
                print("\n It is too big , think a little bit smaller number........")
        counter+= 1
    else:
        print("\n You lose , Try again next time")


if __name__ == "__main__":
    main()
        
