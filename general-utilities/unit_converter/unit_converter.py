
# Functions Room: Where we create functions-

# Here i calculate length
def kilometers_to_meters(kilometer):
    meter_calc = kilometer * 1000
    return meter_calc

def meters_to_centimeter(meter):
    centimeter_calc = meter * 100
    return centimeter_calc

def meter_to_feet(meter):
    feet_calc = meter * 3.28
    return feet_calc

def inches_to_centimeter(inches):
    centimeter_calc = inches * 2.54
    return centimeter_calc

# Here I calculate Mass

def kilogram_to_gram(kilogram):
    gram_calc = kilogram * 1000
    return gram_calc

def gram_to_miligram(gram):
    miligram_calc = gram * 1000
    return miligram_calc

def kilogram_to_pounds(kilogram):
    pound_calc = kilogram * 2.2046
    return pound_calc

# Here I calculate Time

def hour_to_min(hour):
    min_calc = hour * 60
    return min_calc

def min_to_sec(min):
    sec_calc = min * 60
    return sec_calc

def sec_to_min(sec):
    min_calc = sec / 60
    return min_calc

def min_to_hour(min):
    hour_calc = min / 60
    return hour_calc

def sec_to_hour(sec):
    hour_calc = sec / 3600 #(60 x 60 basic maths)
    return hour_calc

def hour_to_sec(hour):
    sec_calc = hour * 3600 #(same as here 60 x 60)
    return sec_calc

def check_rerun():
    while True:
        exit_or_rerun = input(" Do you want to exit or rerun the program? (Type 'exit' to quit or 'rerun' to run again): ").strip().lower()
        if exit_or_rerun == 'exit':
            print("\n Exiting the program. Goodbye!")
            return False
        elif exit_or_rerun == 'rerun':
            return True
        else:
            print(" Invalid input. Please type 'exit' or 'rerun'.")

# Main Room: Where we interact with user

def main():
    while True:
        print('''\n 👋 Hey, Welcome in my another 😞 stupid program , \n \t \t As its name suggests it converts units like Length, Mass and Time  \n\t
            Choose Number Following This Chart:
            1 - Convert Length like Kilometer to Meter \n
            2 - Convert Mass  like kilogram to Gram \n 
            3 - Convert Time like Hour to Minute \n''')
    
        # Error handling for user input
        try:
            user_input = int(input("\n SO 🤔, Which number you want to choose: "))
        except ValueError:
            print("\n Error: Please enter a valid integer. Rerun the program.")
            continue

    # Here we Convert Length :
        if user_input == 1:
            print("\n You Selected: Convert length like kilometer to Meter Conversion")
            print('''\n Hey, We have Four operations (Choose its corresponding number): 
                                1 - Kilometers to Meters Conversion
                                2 - Meter to Centimeter Conversion
                                3 - Meter to Feet Conversion
                                4 - Inches to Centimeter Conversion   ''')
        try:
            user_choose = int(input("\n Which Operation should we perform: "))

            # For Kilometer to meter conversion
            if user_choose == 1:
                print("\n You Selected : 1 - Kilometers to meters Conversion ")
                kilometer_to_meter = float(input("\n Enter kilometer (Km) here: "))
                print(f"\n Your 'kilometer to meter conversion' answer: {kilometers_to_meters(kilometer_to_meter):.2f} meter \n")

            # For meter to centimeter conversion
            elif user_choose == 2:
                print("\n You Selected : 2 - meter to centimeter Conversion ")
                meter_to_centimeter = float(input("\n Enter meter (m) here: "))
                print(f"\n Your 'meter to centimeter' answer: {meters_to_centimeter(meter_to_centimeter):.2f} centimeter \n")

            # For meter to feet conversion
            elif user_choose == 3:
                print("\n You Selected : 3 - Meter to feet Conversion")
                meter_to_feet_var = float(input("\n Enter Meter (m) here: "))
                print(f"\n Your 'Meter to Feet' answer: {meter_to_feet(meter_to_feet_var):.2f} feet \n")

            # for inches to centimeter conversion
            elif user_choose == 4:
                print("\n You Selected : 4 - Inches to Centimeter Conversion ")
                inches_to_centimeter_var = float(input("\n Enter Inches (in) here: "))
                print(f"\n Your 'Inches to Centimeter' answer: {inches_to_centimeter(inches_to_centimeter_var):.2f} centimeter \n")

            # Handling invalid operation choice
            else:
                print("\n Error: Invalid operation choice. Please rerun the program and select a valid option.")
                return
        except ValueError:
            print("\n Error: Please rerun this program and insert a valid number (integer or decimal).")
            continue
        if not check_rerun():
            break

    # Here we convert Mass:
        elif user_input == 2:
            print("\n You Selected: Convert Mass like kilogram to Gram ")
            print('''\n Hey, We have Three operations (Choose its corresponding number): 
                               1 - kilogram to Gram Conversion \n
                               2 - Gram to MiliGram Conversion \n
                               3 - kilogram to Pounds Conversion \n''')
        try: 
            user_choose2 = int(input("\n Which Operation should we perform: "))
            
            # For Kilogram to Gram Conversion
            if user_choose2 == 1:
                print("\n You Selected : 1 - Kilogram to Gram conversion ")
                kilogram_to_gram_var = float(input("\n Enter Kilogram (kg) here: "))
                print(f"\n Your 'Kilogram to Gram' answer: {kilogram_to_gram(kilogram_to_gram_var):.2f} gram \n")

            # For Gram to Miligram Conversion:
            elif user_choose2 == 2:
                print("\n You Selected : 2 - Gram to Miligram Conversion ")
                gram_to_miligram_var = float(input("\n Enter Gram (g) here: "))
                print(f"\n Your 'Gram to Miligram Conversion' answer: {gram_to_miligram(gram_to_miligram_var):.2f} milligram \n")

            # For Kilogram to Pound Conversion:
            elif user_choose2 == 3:
                print("\n You Selected : 3 - Kilogram to Pound Conversion ")
                kilogram_to_pound_var = float(input("\n Enter Kilogram (kg) here: "))
                print(f"\n Your 'Kilogram to Pound Conversion' answer: {kilogram_to_pounds(kilogram_to_pound_var):.2f} pound \n")

            # Handling invalid operation choice
            else:
                print("\n Error: Invalid operation choice. Please rerun the program and select a valid option.")
                return
            
        except ValueError:
            print("\n Error: Please rerun this program and insert a valid number (integer or decimal).")
            continue
        if not check_rerun():
            break

    # Here we convert Time:
        elif user_input == 3:
            print("\n You Selected: Convert Time like Hour to Minute Conversion")
            print('''\n Hey, We have Six operations (Choose its corresponding number) : 
                             1. Hour to Minute Conversion \n
                             2. Minute to Second Conversion \n
                             3. Second to Minute Conversion \n
                             4. Minute to Hour Conversion \n
                             5. Second to Hour Conversion \n 
                             6. Hour to Second Conversion  \n''')
        try:
            user_choose3 = int(input("\n Which Operation should we perform: "))
                
            # For Hour to Minute Conversion
            if user_choose3 == 1:
                print("\n You Selected : 1 - Hour to Minute Conversion ")
                hour_to_min_var = float(input("\n Enter Hour (h) here: "))
                print(f"\n Your 'Hour to Minute conversion' answer: {hour_to_min(hour_to_min_var):.2f} minute \n")

            # For Minute to Second Conversion
            elif user_choose3 == 2:
                print("\n You Selected : 2 - Minute to Second Conversion ")
                min_to_sec_var = float(input("\n Enter Minute (min) here: "))
                print(f"\n Your 'Minute to Second conversion' answer: {min_to_sec(min_to_sec_var):.2f} second \n")

            # For Second to Minute Conversion                    
            elif user_choose3 == 3:
                print("\n You Selected : 3 - Second to Minute Conversion ")
                sec_to_min_var = float(input("\n Enter Seconds (s) here: "))
                print(f"\n Your 'Second to Minute conversion' answer: {sec_to_min(sec_to_min_var):.2f} minute \n")

            # For Minute to Hour Conversion
            elif user_choose3 == 4:
                print("\n You Selected : 4 - Minute to Hour Conversion ")
                min_to_hour_var = float(input("\n Enter Minutes (min) here: "))
                print(f"\n Your 'Minute to Hour Conversion' answer: {min_to_hour(min_to_hour_var):.2f} hour \n")

            # For Second to Hour Conversion
            elif user_choose3 == 5:
                print("\n You Selected : 5 - Second to Hour Conversion ")
                sec_to_hour_var = float(input("\n Enter Seconds (s) here: "))
                print(f"\n Your 'Second to Hour Conversion' answer: {sec_to_hour(sec_to_hour_var):.2f} hour \n")
                    
            # For Hour to Second Conversion
            elif user_choose3 == 6:
                print("\n You Selected : 6 - Hour to Second Conversion ")
                hour_to_sec_var = float(input("\n Enter Hour (h) here: "))
                print(f"\n Your 'Hour to Second Conversion' answer: {hour_to_sec(hour_to_sec_var):.2f} second \n")

            # Handling invalid operation choice
            else:  
                print("\n Error: Invalid operation choice. Please rerun the program and select a valid option.")
                continue
        except ValueError:
            print("\n Error: Please rerun this program and insert a valid number (integer or decimal).")
            continue
        if not check_rerun():
            break
    # Handling invalid main choice
        else:
            print("\n Error: Invalid choice. Please rerun the program and select a valid option.")
            continue
print("\n Thank you for using this program. Goodbye!")

if __name__ == "__main__":
    main()
