num = raw_input('Please enter your 10 digit number:')
while len(num) != 10 or (not num.isdigit()):
    print 'Not a 10 digit number'
    num = raw_input('Please enter your 10 digit number:')
num = int(num)
print 'The final number is: ', num
