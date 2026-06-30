# 1. Ask user which number's times table they want
# 2. Ask how far the table should go (up to what multiplier)
# 3. Print the times table with clean aligned formatting
# 4. Ask to print another or exit


def times_table():
    while True:
        try: 
            which_table = int(input("\n 🧩 Which number's table do you want: ").strip())
            return which_table
        except ValueError:
            print("\n ❌ Please enter a number here ")

def how_far():
    while True:
        try:
            upto_end = input("\n 🚀 How far should this table go [default: 10]: ").strip() or '10'
            return int(upto_end)
        except ValueError:
            print("\n ❌ Please enter a number here ")

def align_formatting(table_numb, end_numb):
    max_result = table_numb * end_numb
    result_width = len(str(max_result))
    for i in range(1,end_numb+1):
        result = table_numb * i
        print(f"{table_numb:>{result_width}} x {i:>{result_width}} = {result:>{result_width}}")

def main():
    while True:
        print("\n -------------- 🧮 Times Table Program -------")
        table_number = times_table()
        table_end = how_far()
        print("\n 🍰 Your Desired Table - \n")
        align_formatting(table_number,table_end)

        play_again = input("\n 🤖 Do you want another number's table [y/n]: ").strip().lower()
        if play_again != 'y':
            print("\n 🤗 Goodbye!")
            break

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n 🤗 Goodbye!")

