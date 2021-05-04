def factorial(n):
    base = 1

    for num in range(1, n+1):
        base = base * num

    return base


var = 5
res = factorial(var)
print(res)