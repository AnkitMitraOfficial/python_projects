#Time to put your luck on a test 
import random as rd# Imports the random module

secret_number = rd.randint(1,10)#Setting the secret number 

guess_count = 0
guess_limits = 3

#Code Below!
print("Guess a secret number from 1 to 10")
try: 
    while guess_count < guess_limits:
        guess = int(input("Guess: \n"))
        
        if guess > 10 or guess < 1:
            print("Invalid range")
             
        if guess == secret_number:
            print("You won")
            print("Maybe due to luck?")
            break
        
        elif guess_count >= 2:
            print("Out of chances!")
            print("The secret number was " + str(secret_number))
            break
        guess_count += 1
            
except:
    print("Integers are only allowed!")
    