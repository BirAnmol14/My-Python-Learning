#Random Number Guessing Game
#input always returns a string 
import random
import sys
import time
def welcome():
    for i in range(100):
        print('')
    print('welcome to the guessing game')
    print('Loading.....')
    time.sleep(1)
def game():
    welcome()
    ran=random.randint(1,21)
    flag=True
    count=0
    while flag:
        print('I am guessing a number between 1 and 20')
        n=input('Enter your Guess: ')
        try:
            val=int(n)
            count+=1
            if val == ran:
                print('You guessed it correctly in '+str(count)+' guesses')
                flag=False
                replay()
            elif val>ran:
                print('Your guess was too high')
            else:
                print('Your guess is too low')
        except:
            print('You Did Not Enter a valid Number')
def replay():
    print('Do You Want to play again?')
    a=input()
    if a[0].lower()=='y':
        game()
    elif a[0].lower=='n':
        print('Bye...')
        sys.exit()
game()
