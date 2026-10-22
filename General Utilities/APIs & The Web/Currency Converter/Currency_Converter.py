import requests
import argparse

API_KEY = 'Your_API_Key' # Insert Your token & Get from http://v6.exchangerate-api.com
SEPARATOR = '-'*30

if not API_KEY or API_KEY == 'Your_API_Key':
    raise ValueError("❌ Error: Please Insert your Valid token before running.")

parser = argparse.ArgumentParser(
    description='💱 Currency Converter — Live exchange rates',
    epilog='Top currencies: USD EUR GBP JPY INR AUD CAD CHF AED SGD'
)
parser.add_argument('--amount', type=float, help='Amount to convert')
parser.add_argument('--from', dest='from_currency',default='USD', help='Currency code to convert FROM (e.g. USD) [default:USD]')
parser.add_argument('--to', dest='to_currency', help='Currency code to convert TO (e.g. INR)')
parser.add_argument('--list', action='store_true', help='List all available currency codes.')
args = parser.parse_args()

def fetch_rates(from_currency):
    url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}'

    try:
        response = requests.get(url=url, timeout=5)
        response.raise_for_status()
        data = response.json()
        if isinstance(data, list) or len(data) == 0:
            print("\n\t [⚠️ No Data Available!]")
        if data.get('result') == 'error':
            print(f"❌ Invalid base currency: {from_currency}")
            return False
        return data
    except requests.exceptions.ConnectionError:
        print("\n\t [⚠️  No Internet Connection!]")
    except requests.exceptions.Timeout:
        print("\n\t [⚠️  Request Timed Out!]")
    except requests.exceptions.HTTPError as err:
        print(f"\n\t [❌ HTTP Error: {err}!]")
    except requests.exceptions.RequestException as err:
        print(f"\n\t [❌ An unexpected error occurred: {err}!]")

def validate_args(amount, from_currency, to_currency, data):
    if data is None or not data:
        print("\n\t [❌ Error: Something Went Wrong]")
        return
    rates = data.get('conversion_rates')
    if amount <= 0:
        print("\n \t[❌ Error: Please Enter a Valid Amount!]")
        return False
    elif from_currency.upper() not in rates or to_currency.upper() not in rates:
        print("\n\t [❌ Error: Please Enter a Valid Code!]")
        return False
    return True

def convert(to_currency, amount, data):
    if data is None or not data:
        print("\n\t [❌ Error: Something Went Wrong]")
        return
    
    to_currency_upper = (to_currency).upper()
    rates = data.get('conversion_rates')
    rate = rates.get(to_currency_upper)
    
    result = amount * rate
    return result, rate

def display_result(to_currency, from_currency, amount, data):
    if data is None or not data or convert(to_currency, amount, data=data) is None:
        print("\n\t [❌ Error: Something Went Wrong]")
        return
    result, rate = convert(to_currency, amount, data=data)
    
    print(SEPARATOR)
    print("💱 Currency Conversion Result")
    print(f"Amount      : {amount} {(from_currency).upper()}")
    print(f"Converted to: {(to_currency).upper()}")
    print(f"Result      : {result:.2f}")
    print(f"Rate        : 1 {(from_currency).upper()} = {rate} {(to_currency).upper()}")
    print(f"Updated     : {data.get('time_last_update_utc')[:16]}")
    print(SEPARATOR)

def list_currencies(from_currency, data):
    if data is None or not data:
        print("\n\t [❌ Error: Something Went Wrong]")
        return
    print(f"\n[+] Note: Current rate print - [Acoording to {(from_currency).upper()}]")
    print("\nListing of Available Currency Code -")
    rate_list = data.get('conversion_rates')
    print("Code  -   Current Rate")
    print(SEPARATOR)
    for currency, rate in rate_list.items():
        print(f"{currency}    =    {rate}")
    print(SEPARATOR)

def main():
    data = fetch_rates(args.from_currency)
    if args.list:
        list_currencies(from_currency=args.from_currency, data=data)
    elif args.amount is None or args.to_currency is None:
        parser.error("The following arguments are required for conversion: --amount, --to")
    else:   
        validation = validate_args(amount=args.amount, from_currency=args.from_currency, to_currency=args.to_currency, data=data)
        if validation is True:
            display_result(to_currency=args.to_currency, from_currency=args.from_currency, amount=args.amount, data=data)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("[💥 Interrupted by User!]")
        exit(0)