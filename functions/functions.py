# A function is a block of code runs when it is called
def greet():
    print('Hello World')
    print('Good Day Ankit')

greet()


def add(x,y):
    c = x + y
    print(c)

add(3,4)

# return keyword we use when we have to return any value from the function
# n1 = int(input('Enter a number: '))
# n2 = int(input('Enter another number: '))

# def add_sub(p=n1,q=n2):# Default values to the arguments
#     a = p + q
#     s = p - q

#     return a,s

# result1, result2 = add_sub()
# print(result1, result2)

# Function Arguments

#Pass by value or Pass by reference

def update(x):
    x = 8
    print(x)

a = 10
update(a)
print(a)















