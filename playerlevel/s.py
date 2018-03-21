# Python program to reverse a string with special characters
 
# Returns true if x is an aplhabatic character, false otherwise
def isAlphabet(x):
    return x.isalpha()
 
def reverse(string):
    LIST = toList(string)
 
    # Initialize left and right pointers
    r = len(LIST) - 1
    l = 0
 
    # Traverse LIST from both ends until
    # 'l' and 'r'
    while l < r:
 
        # Ignore special characters
        if not isAlphabet(LIST[l]):
            l += 1
        elif not isAlphabet(LIST[r]):
            r -= 1
 
        else:   # Both LIST[l] and LIST[r] are not special
            LIST[l], LIST[r] = swap(LIST[l], LIST[r])
            l += 1
            r -= 1
 
    return toString(LIST
