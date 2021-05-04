# Fibonacci sequence -- 0 1 1 2 3 5 8 13 21 34 55.........
def fibonacci(n):
    a = 0
    b = 1
    if n == 1:
        print(a)

    else:
        print(a)
        print(b)

        for _ in range(2,n):

            c = a + b
            a = b
            b = c

            print(b)


fibonacci(10)