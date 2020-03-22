# The Collatz Sequence
# Project 3.1 from Automate the Boring Stuff
# Created by Blue Lagoon, 2020
def collatz(number):
    if number%2==0:
        print (number//2)
        return number//2
    elif number%2==1:
        print (number+1)
        return (number+1)

try:
    inputNumber=input('Enter number: ')
    while inputNumber!=1:
        inputNumber=collatz(int(inputNumber))

except ValueError:
    print('Please enter an integer')
