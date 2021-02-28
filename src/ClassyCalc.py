class PyCalculator():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def addition(self):
        return self.x+self.y

    def subtraction(self):
        return self.x - self.y

    def multiplication(self):
        return self.x*self.y

    def division(self):
        if self.y == 0:
            print("Division by zero. We cannot perform this operation.")
        else:
            return self.x/self.y



def main():
    print("Select please one of the following operations: ")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")

    choice = input("What kind of operation should be performed? [Insert one of the options(1 2 3 4)]: ")
    if choice in ('1', '2', '3', '4'):
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        calculator = PyCalculator(x,y)

        if choice == '1':
                print(calculator.addition())
        elif choice == '2':
                print(calculator.subtraction())
        elif choice == '3':
                print(calculator.multiplication())
        else:
                print(calculator.division())


if __name__ == '__main__':
    main()
