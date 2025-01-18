class UnitConverter:
    def __init__(self):
        self.conversions = {
            "km_to_miles": self.km_to_miles,
            "miles_to_km": self.miles_to_km,
            "celsius_to_fahrenheit": self.celsius_to_fahrenheit,
            "fahrenheit_to_celsius": self.fahrenheit_to_celsius
        }

    def km_to_miles(self, km):
        return km * 0.621371

    def miles_to_km(self, miles):
        return miles / 0.621371

    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

    def convert(self, conversion_type, value):
        if conversion_type in self.conversions:
            return self.conversions[conversion_type](value)
        else:
            raise ValueError("Invalid conversion type")

    def display_menu(self):
        print("\nUnit Converter Menu:")
        print("1. Kilometers to Miles")
        print("2. Miles to Kilometers")
        print("3. Celsius to Fahrenheit")
        print("4. Fahrenheit to Celsius")
        print("5. Quit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1/2/3/4/5): ")

            if choice == "1":
                km = float(input("Enter kilometers: "))
                miles = self.convert("km_to_miles", km)
                print(f"{km} km is equal to {miles:.2f} miles")

            elif choice == "2":
                miles = float(input("Enter miles: "))
                km = self.convert("miles_to_km", miles)
                print(f"{miles} miles is equal to {km:.2f} km")

            elif choice == "3":
                celsius = float(input("Enter Celsius: "))
                fahrenheit = self.convert("celsius_to_fahrenheit", celsius)
                print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

            elif choice == "4":
                fahrenheit = float(input("Enter Fahrenheit: "))
                celsius = self.convert("fahrenheit_to_celsius", fahrenheit)
                print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

            elif choice == "5":
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    converter = UnitConverter()
    converter.run()
