def person(name, age=18): # 18 is the default value
    print(name)
    print(age-5)


person('Ankit',15)# this value will ovverride the default value

# Variable length argument
def sum(*b):
    a = 0
    for i in b:
        a = a + i

    print(a)

sum(6,8)

# Keyword length argument
def data(name, **other):
    print(name)
    for i,j in other.items():
        print(i,j)


data('Ankit', age=15,city='kolkata',mob=100)

#Scope
num = 5

def something():
    num = 10
    num2 = 20 # we can't call this number outside the function, cause it's a local variable
    print('Num inside function:',num)

something()

print('Num outside function',num)

