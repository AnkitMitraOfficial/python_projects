# def odd_even(lst):
#     global odd, even
#     odd = 0
#     even = 0
#     for i in lst:
#         if i % 2 == 0:
#             even += 1
#         else:
#             odd += 1
#     return even, odd    
    
# lst = [2,3,4,5,6,7,8]

# result = odd_even(lst)
# print('Total even numbers are: {} and odd numbers are: {}'.format(even, odd))

def odd_even(lst):
    global odd, even
    odd = 0
    even = 0
    for num in lst:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
       
    return odd, even

lst = [2,3,4,5,6,7,8]

result = odd_even(lst)
print('The total odd numbers are {} and total even numbers are {}'.format(odd, even))