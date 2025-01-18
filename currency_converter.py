def convert_currency(source_currency, target_currency, amount):
    exchange_rates = {
        'USD': {'EUR': 0.85, 'JPY': 110.0, 'GBP': 0.75, 'INR': 73.0},
        'EUR': {'USD': 1.18, 'JPY': 129.53, 'GBP': 0.88, 'INR': 85.0},
        'JPY': {'USD': 0.0091, 'EUR': 0.0077, 'GBP': 0.0068, 'INR': 0.67},
        'GBP': {'USD': 1.33, 'EUR': 1.14, 'JPY': 147.0, 'INR': 94.0},
        'INR': {'USD': 0.014, 'EUR': 0.012, 'JPY': 1.5, 'GBP': 0.011}
    }

    if source_currency in exchange_rates and target_currency in exchange_rates[source_currency]:
        rate = exchange_rates[source_currency][target_currency]
        converted_amount = amount * rate
        return converted_amount
    else:
        return None

def main():
    while True:
        print("Currency Converter")
        source_currency = input("Enter source currency (USD, EUR, JPY, GBP, INR): ").upper()
        target_currency = input("Enter target currency (USD, EUR, JPY, GBP, INR): ").upper()
        amount = float(input("Enter amount to convert: "))

        converted_amount = convert_currency(source_currency, target_currency, amount)

        if converted_amount is not None:
            print(f"{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}")
        else:
            print("Invalid currency conversion.")

        another = input("Do you want to convert another amount? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()