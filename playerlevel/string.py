# Python3 implementation to check if
# both halves of the string have
# at least one different character
MAX = 26
 
# Function which break string into two
# halves Increments frequency of characters
# for first half Decrements frequency of
# characters for second half true if any
# index has non-zero value
def function(st):
    global MAX
    l = len(st)
     
    # Declaration and initialization
    # of counter array
    counter = [0] * MAX
     
    for i in range(l // 2):
        counter[ord(st[i]) - ord('a')] += 1
         
    for i in range(l // 2, l):
        counter[ord(st[i]) - ord('a')] -= 1
         
    for i in range(MAX):
        if (counter[i] != 0):
            return True
             
    return False
 
# Driver function
st = "abcasdsabcae"
if function(st): 
    print("Yes, both halves differ by at ",
          "least one character")
else:
    print("No, both halves do not differ at all")
 
# This code is contributed by Ansu Kumari
