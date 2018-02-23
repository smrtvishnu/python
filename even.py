import math

number = int (input ('Enter number: '))

if number % 2 == 0 and number != 0:
    print ('Even number')
elif number == 0:
    print ('Zero is neither even, nor odd.')
else:
    print ('Odd number')
