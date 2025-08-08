# to create a simple calculator that accepts two numbers and an operation, 

numbers = input("Enter two numbers: ").split()
num1, num2 = [float(n) for n in numbers]
operator = input("Enter the operation to be performed: ")

if (operator == '+') | (operator == 'sum') :
    print("Result", num1 + num2)
elif (operator == "-") | (operator == 'subtract'):
    print("Result", num1 - num2)
elif (operator == "x") | (operator == 'mutiply'):
    print("Result", num1 * num2)
elif (operator == "/") | (operator == 'divide'):
    if num2 == 0:
     print("Can not divide by zero(Undefined)")
    else:
        print("Result", num1 / num2)
else:
    print("Non specified operator. Please try again!")

