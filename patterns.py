# Print this pattern below
#--------->

# # # #
# # # #
# # # #
# # # #

#---------->

# Code goes here
for i in range(4):
    for j in range(4):
        print('# ', end='')

    print()


# Print this pattern below
#--------->

#
# #
# # #
# # # #

#--------->

# Code
print()
for i in range(4):
    for j in range(i+1):
        print('# ', end='')

    print()


# Print this pattern below

#--------->

# # # # 
# # #
# #
#

#--------->
print()
for i in range(4):
    for j in range(4-i):
        print('# ', end='')

    print()


print()
str1='ABCD'
str2='PQR'
for i in range(4):
     print(str1[ : i+1 ] + str2[ i : ])


# Practice
print()
for i in range(4):
    for j in range(4):
        print('# ',end='')
    print()

print()
for i in range(4):
    for j in range(i+1):
        print('# ',end='')

    print()

print()
for i in range(4):
    for j in range(4-i):
        print('# ',end='')

    print()