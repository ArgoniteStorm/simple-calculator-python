from time import sleep

def some(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mult(n1, n2):
    return n1 * n2
def div(n1,n2):
    if n2 == 0:
        return "Error: Division by zero!"
    else:
        return n1 / n2
while True:
    print("_"*30)
    print("{:^30}".format("Simple Calculator"))
    print("-"*30)
    print('''{:^30}
    [1] Sum
    [2] Subtraction
    [3] Multiplication
    [4] Division'''.format('Desired Calculation'))
    try:
        operation = int(input("What is your operation? "))
        if operation not in [1, 2, 3, 4]:
            print("Invalid operation. Try again.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue

    print("{:^30}".format("Enter the operands"))
    try:
        n1 = int(input("1st Num: "))
        n2 = int(input("2nd Num: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue

    print("Calculating...")
    sleep(1)

    if operation == 1:
        result = some(n1, n2)
    elif operation == 2:
        result = sub(n1, n2)
    elif operation == 3:
        result = mult(n1, n2)
    elif operation == 4:
        result = div(n1, n2)

        print(f"Result: {result}")
    print('-' * 30)

    choice = input("{:^30}".format("Do another operation? [Y/N]: ")).strip().upper()
    if choice != "Y":
        print("Have a great day...")
        break