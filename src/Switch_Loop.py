def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

def switch(choice):
    switcher = {
        1: addition(),
        2: subtraction(),
        3: multiplication(),
        4: division()
    }
    return switcher.get(choice, "There is no such an option")

print("Select please one of the following operations: ")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

#Take input from user
choice = input("What kind of operation should be performed? [Insert one of the options(1 2 3 4)]: ")
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
print (switch(choice))
