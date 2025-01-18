class Calculator:
    def __init__(self):
        self.operations = {
            "1": self.add,
            "2": self.subtract,
            "3": self.multiply,
            "4": self.divide
        }

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return num1 / num2

    def display_menu(self):
        print("\nSimple Calculator Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1/2/3/4/5): ")

            if choice in self.operations:
                try:
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))
                    result = self.operations[choice](num1, num2)
                    print(f"{num1} {self.get_operator(choice)} {num2} = {result:.2f}")
                except ZeroDivisionError as e:
                    print(str(e))
                except ValueError as e:
                    print(str(e))

            elif choice == "5":
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")

    def get_operator(self, choice):
        operators = {
            "1": "+",
            "2": "-",
            "3": "*",
            "4": "/"
        }
        return operators[choice]

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()