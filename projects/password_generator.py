import random
import time

the_password = ''
new_password = ''
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '1234567890'
special = '!@##$^*&%(*)(&$$!#'

all = lowercase + uppercase + numbers + special

try:
    length = int(input('Enter the length of your password: '))
    the_password += "".join(random.sample(all, length))
    print(f'Your password is: + {the_password}')
    print()

    while True:
        print("Type 'new' for new password or 'leave' for exiting")
        ask = input('What do you like to do?: ')

        if ask == 'new':
            new_password += "".join(random.sample(all, length))
            print(new_password)        
            new_password = ''
            print()    

        elif ask == 'leave':
            print('Breaking...')
            time.sleep(1)
            print('Breaking......')
            time.sleep(2)
            print('Program terminated with exit code 0')
            break
        
        else:
            print('Command not found. Program terminated!')
            break


except Exception as e:
    print('Error while executing the program!')
    print()

    print('More error details:')
    print('Error: ', e)
