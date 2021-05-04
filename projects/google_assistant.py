import pywhatkit  # To make searches on Yt
import random  # For the random number game and jokes
import webbrowser  # To make urls of news and gmail
import playsound  # Plays background song when a joke is said
import time  # For some time break

name = 'Ankit'
while True:

    print('')
    print(f'Google Assistant: How can I help you {name}?\n')

    tasks = [

        '1. play songs',
        '2. surf news',
        '3. random jokes',
        '4. show last emails',
        '5. random number choosing game',
        '6. Change my name',
    ]

    for task in tasks:
        print(task)

    print('\n')  # For a line break

    print('Enter the task number')
    work = input(f"What's on your mind {name}?: ")
    print('\n')  # Line break

    if work == '1':
        print(f'What do you want to listen {name}? \n')
        song_list = [
            '1: Phao - 2 phut hon',
            '2: how you like that',
            '3: shape of you',
            '4: despacito\n'
        ]
        for songs in song_list:
            print(songs)

        print('Type the number of the song you want to play, type (0) for random song selection')

        try:
            search = int(input('Type the number of the song: '))
            if search == 0:
                random_song = random.choice(song_list)
                pywhatkit.playonyt(random_song)

            elif search == 1:
                pywhatkit.playonyt('2 phut hon(kiaz remix)')

            elif search == 2:
                pywhatkit.playonyt('how you like that blackpink')

            elif search == 3:
                pywhatkit.playonyt('shape of you official')

            elif search == 4:
                pywhatkit.playonyt('despacito official')
                
            else:
                print('Song number invalid or not found!')
                last_search = input(
                    'Type the name of the song you want to listen: ')
                pywhatkit.playonyt(last_search)
        except ValueError:
            print('You entered invalid  input')
            last_search = input(
                'Type the name of the song you want to listen: ')
            pywhatkit.playonyt(last_search)

    # Open news
    elif work == '2':
        webbrowser.open('https://www.cnet.com/news/')

    # Tell a joke
    elif work == '3':
        jokes = [
            'The Problem With Atoms \nQ: Why can’t you trust atoms?\nA: They make up everything.',
            'Q. What is the biggest lie in the entire universe?\nA. "I have read and agree to the Terms & Conditions."',
            'Q: Why was the cell phone wearing glasses?\nA: It lost its contacts.',
            'You know you are texting too much when....you say LOL in real life, instead of just laughing.',
        ]

        selected_joke = random.choices(jokes)

        for joke in selected_joke:
            print(joke)
            time.sleep(2)
            playsound.playsound(r'laugh.mp3')

    # Open email
    elif work == '4':
        webbrowser.open('https://mail.google.com/mail/u/0/#inbox')

    # Number guessing game
    elif work == '5':

        secret_number = random.randint(1, 10)  # Setting the secret number

        guess_count = 0
        guess_limits = 3
        tries = 3

        # Code Below!
        print("Guess a secret number from 1 to 10")

        try:
            while guess_count < guess_limits:
                print(f'You have {tries} tries left')
                guess = int(input("Guess: \n"))

                if guess > 10 or guess < 1:
                    print(
                        f"The number {guess} you guessed is in Invalid range")

                if guess == secret_number:
                    print('You won')
                    print("Maybe due to luck?")
                    break

                elif guess_count >= 2:
                    print("Out of chances, You lose!")
                    print("The secret number was " + str(secret_number))
                    break
                guess_count += 1
                tries -= 1

        except ValueError:
            print("Integers are only allowed!")
            
    # To change the name
    elif work == '6':
        name2 = input('Enter your name, you want me to call you?: ')
        sure = input(
            f'Do you want to change your name to -- {name2} -- Yes or No?: ')

        if sure == 'yes' or sure == 'Yes' or sure == 'YES':
            print('Your name is confirmed!')
            name = name2

        elif sure == 'no' or sure == 'NO' or sure == 'No':
            print('Ok! Not changing your name')
        else:
            print('A error occured while changing your name! Try again')
    else:
        print('Google Assistant: Task Number not found')
