# 1. Show a menu of unit options (Celsius, Fahrenheit, Kelvin)
# 2. Ask user to pick source unit and target unit
# 3. Ask for the temperature value
# 4. Convert using the correct formula
# 5. Display the result cleanly
# 6. Ask to convert again or exit

UNITS = ['C', 'F', 'K']

def show_menu():
    print(f"\n 🍸 Units Menu: 'C' - Celsius, 'F' - Fehrenheit, 'K' - Kelvin")

def get_unit(prompt):
    while True:
        user_unit = input(f"\n 📌 Pick a Unit as {prompt} unit: ").strip().upper() 
        if user_unit in UNITS: 
            return user_unit
        else:
            print("\n ❌ Error: Choose in provided Units Menu!")
    
def get_temperature():
    while True:
        try:
            temp_value = float(input("\n 🌡️  Enter TEMPERATURE VALUE for Conversion: ").strip())
            return temp_value
        except ValueError:
            print("\n ❌ Error: Invalid Input, please enter a NUMBER here!") 
 
def convert(value, from_unit, to_unit):

    if from_unit == 'C' and to_unit == 'F':
        result = (value * 9 / 5) + 32
    elif from_unit == 'C' and to_unit == 'K':
        result = value + 273.15
    elif from_unit == 'F' and to_unit == 'C':
        result = (value - 32) * 5 / 9
    elif from_unit == 'F' and to_unit == 'K':
        result = (value -32) * 5 / 9 + 273.15
    elif from_unit == 'K' and to_unit == 'C':
        result = value - 273.15
    elif from_unit == 'K' and to_unit == 'F':
        result = (value - 273.15) * 9/5 + 32

    if from_unit == to_unit:
        return float(value)
    
    return float(result)

def absolute_zero(value, from_unit):
    abs_zero_condition = False
    if from_unit == 'C' and value < -273.15:
        abs_zero_condition = True
    elif from_unit == 'F' and value < -459.67:
        abs_zero_condition = True
    elif from_unit == 'K' and value < 0:
        abs_zero_condition = True
    return abs_zero_condition

def substitue_result(target_unit, result):
    if target_unit == 'C':
        print(f"\n 🍨 Your Desiresd Result: {round(result,2)} °C")
    if target_unit == 'K':
        print(f"\n 🍨 Your Desiresd Result: {round(result,2)} °K")
    if target_unit == 'F':
        print(f"\n 🍨 Your Desiresd Result: {round(result,2)} °F")

    

def main():
    print("\n- Welcome in Temperature Convertor program -")
    show_menu()
    while True:
        source_unit = get_unit('SOURCE')
        target_unit = get_unit('TARGET')
        while True:
            temp_value = get_temperature()
            if absolute_zero(temp_value, source_unit):
                print("\n ❌ Rejected as physically impossible!")
            else:
                converted_result = convert(temp_value, source_unit, target_unit)
                substitue_result(target_unit, converted_result)
                break
        play_again = input('\n 🤔 Do you want to convert again something [y/n]: ').strip().lower()

        if play_again != 'y':
            print("\n 👋 Goodbye!")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n 👋 Goodbye!")
