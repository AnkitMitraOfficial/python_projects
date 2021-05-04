# Just for knowledge, how to swap variables in python

a = 'Ankit'
b = 'Mitra'

temp = a
a = b
b = temp

print(a,b)


# or 
a = 5
b = 6

a,b = b,a

print(a,b)


# While loop runs until the given condition is met
num = 0

while num<10:
    if num % 5 == 0:
        print(num)
    num += 1
else:
    print('Finished')