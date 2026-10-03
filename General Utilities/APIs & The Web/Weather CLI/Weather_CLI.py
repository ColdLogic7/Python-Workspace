import requests

api_key = 'd4fb98ed18664a959ad6af8dc1d80933'
CURRENT_URL  = 'https://api.openweathermap.org/data/2.5/weather'
FORECAST_URL = 'https://api.openweathermap.org/data/2.5/forecast'
SEPARATOR = '-'*50

def print_menu():
    print("\n 🎲 MENU:")
    print("\t 1. 🏙️  Current Weather by City Name")
    print("\t 2. 🌍 Current Weather by ZIP/Postal Code")
    print("\t 3. 🔮 View 5-Day Forecast by City Name")
    print("\t 4. [← Exit")

    print(SEPARATOR)
    while True:
        try:
            desired_option = int(input("\n 👉 Choose a Option [1-4]: ").strip())
            if 1 <= desired_option <= 4:
                return desired_option
            else:
                print("❌ Error: Choose a number between 1-4")
        except ValueError:
            print("❌ Error: Choose a Valid Number")
    

def unit_confirmation():
    print("\n➡️  Before any further operation Please choose result UNIT here -")
    while True:
        try:
            get_unit = input("📌 Choose a Unit ['C' - Celsius and 'F' - Fehrenheit] (default: Celsius): ").strip().upper() or 'C'
            if get_unit == 'C':
                return 'metric'
            elif get_unit == 'F':
                return 'imperial'
            else:
                print("❌ Error: Please Enter either 'C' or 'F', nothing else!")
        except ValueError:
            print("❌ Error: Please Enter a Valid Temperature Unit")

def take_query(selected_option):
    if selected_option == 1:
        get_city = input("\n🏙️  Enter City Name for TODAY's Weather [e.g. Landon,Paris,etc]: ").strip().title()
        return get_city
    elif selected_option == 2:
        get_zip = input("\n🌍 Enter ZIP code for Todays's weather (ZIP, Country_code) [e.g. 400001,IN]: ").strip()
        return get_zip
    else:
        get_forecast_ct = input("\n🏙️  Enter city to check the FORECAST [e.g. Landon,Paris,etc]: ").strip().title()
        return get_forecast_ct
            
def make_requests(request_type, query, unit) -> dict | None:
    if request_type == 'zip':
        url, param_key = CURRENT_URL, 'zip'
    elif request_type == 'city':
        url, param_key = CURRENT_URL, 'q'
    else:
        url, param_key = FORECAST_URL, 'q'

    param = {
        param_key: query,
        'appid': api_key,
        'units': unit
    }

    try:
        response = requests.get(url=url, params=param, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        print("⚠️  No Internet Connection!")
    except requests.exceptions.Timeout:
        print("⚠️  Request Timed Out!")
    except requests.exceptions.HTTPError as err:
        print(f"❌ HTTP Error: {err}")
    except requests.exceptions.RequestException as err:
        print(f"❌ An unexpected error occurred: {err}")
    return None



def display_weather(request_type, query, unit):
    json_data = make_requests(request_type,query,unit)
    if json_data is None:
        print("⚠️  Could not display weather data due to a request error.")
        return
    
    print(SEPARATOR)
    print("\n🌱 Weather Details: ")
    print(f"\t 🔆 Condition: {json_data['weather'][0]['description']}")
    print(f"\t 🌡️  Temperature: {json_data['main']['temp']} °{'C' if unit == 'metric' else 'F'}")
    print(f"\t 💧 Humidity: {json_data['main']['humidity']}")
    print(f"\t 🫧  Wind speed: {json_data['wind']['speed']}")
    print(SEPARATOR)

def wthr_forecast(request_type, query, unit):
    json_data = make_requests(request_type, query, unit)
    if json_data is None:
        print("⚠️  Could not display weather data due to a request error.")
        return
    
    print(SEPARATOR)
    print("\n🔮 Weather Forecast: ")
    for block in json_data['list']:
        if '12:00:00' in block['dt_txt']:
            print(f"\n\t-[{block['dt_txt'][:10]}]-")
            print(f"\t🔆 Condition: {block['weather'][0]['description']}")
            print(f"\t🌡️  Temperature: {block['main']['temp']} °{'C' if unit == 'metric' else 'F'}")
            print(f"\t💧 Humidity: {block['main']['humidity']}")
            print(f"\t🫧  Wind speed: {block['wind']['speed']}")

    print("\n\t- [🚩 Forecast Report END Here!] -")
    print(SEPARATOR)


def main():
    print(f"\n{'-'*5}[🌦️  Weather Report Program]{'-'*5}")
    get_unit = unit_confirmation()
    while True:
        get_operation = print_menu()
        if get_operation == 1:
            get_query = take_query(1)
            display_weather(request_type='city', query=get_query, unit=get_unit)
        elif get_operation == 2:
            get_query = take_query(2)
            display_weather(request_type='zip', query=get_query, unit=get_unit)
        elif get_operation == 3:
            get_query = take_query(3)
            wthr_forecast(request_type='forecast', query=get_query, unit=get_unit)
        else:
            print("\n\t 👋 Good Bye!")
            exit(0)

        print()
        restart_loop = input("💡 Do you want to search another weather [y/n]: ").strip().lower()
        if restart_loop != 'y':
            print("\n\t 👋 Good Bye!")
            exit(0)

if __name__ == '__main__':
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print("\n\t 💥 Interrupted by User!")
            exit(0)