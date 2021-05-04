# Print this pattern below
#--------->

# # # #
# # # #
# # # #
# # # #

#---------->

# Code

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
for j in range(4):
    for i in range(4-j):
        print('# ', end='')
    print()