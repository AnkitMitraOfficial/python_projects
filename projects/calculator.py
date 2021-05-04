from . import my_math
from . my_math import add, subtract, divide, multiply, mod, power
print('Welcome to my calculator')

print('What do you want to do? ')
try:
    number1 = int(input('Enter first number: '))
    operator = input('Enter your operator: ')
    number2 = int(input('Enter second number: '))

    if operator == '+':
        result = add(number1, number2)
        print(result)

    elif operator == '-':
        result = subtract(number1, number2)
        print(result)
    elif operator == '/':
        result = divide(number1, number2)
        print(result)

    elif operator == '%':
        result = mod(number1, number2)
        print(result)

    elif operator == '*':
        result = multiply(number1, number2)
        print(result)

except Exception as e:
    print('Error: ',e)