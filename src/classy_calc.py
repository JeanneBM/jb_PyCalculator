class PyCalculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self):
        return self.x + self.y

    def subtraction(self):
        return self.x - self.y

    def multiplication(self):
        return self.x * self.y

    def division(self):
        if self.y == 0:
            return "Division by zero is not allowed."
        return self.x / self.y


def main():
    while True:
        print("\nSelect one of the following operations: ")
        print("1 - Addition")
        print("2 - Subtraction")
        print("3 - Multiplication")
        print("4 - Division")
        print("5 - Exit")

        choice = input("Choose an operation (1-5): ")
        if choice == '5':
            print("Goodbye!")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numerical values.")
                continue

            calculator = PyCalculator(x, y)

            operations = {
                '1': calculator.addition,
                '2': calculator.subtraction,
                '3': calculator.multiplication,
                '4': calculator.division
            }

            print("Result:", operations[choice]())
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == '__main__':
    main()
