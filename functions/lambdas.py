# Lambda functions don't have any name


# Example of lamda functions
# square = lambda a : a * a

# result = square(5)
# print(result)

# a simple function like me
# def square2(b):
#     return b * b


# res = square2(6)
# print(res)


# More applicaions
def is_even(n):
    return n % 2 == 0


nums = [3, 2, 6, 8, 4, 6, 2, 9]

# We want the result as list and we have to pass the function name and list
evens = list(filter(is_even, nums))
print(evens)

# or
evens = list(filter(lambda n: n % 2 == 0, nums))
print(evens)
