
def factorial(n):
    num = 1
    for fact in range(1,n+1):
        num = num*fact

    return num

a = 5
result = factorial(a)

print(result)