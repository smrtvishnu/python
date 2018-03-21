# Python3 implementation to count
# subsequences in first which are 
# anagrams of the second
 
# import library
import numpy as np
 
SIZE = 26
 
# Returns value of Binomial
# Coefficient C(n, k)
def binomialCoeff(n, k):
     
    res = 1
 
    # Since C(n, k) = C(n, n-k)
    if (k > n - k):
        k = n - k
 
    # Calculate value of
    # [n * (n-1) *---* (n-k+1)] /
    # [k * (k-1) *----* 1]
    for i in range(0, k):
        res = res * (n - i)
        res = int(res / (i + 1))
     
    return res
 
 
# Function to count subsequences 
# in first which are anagrams
# of the second 
def countSubsequences(str1, str2):
     
    # Hash tables to store frequencies 
    # of each character
    freq1 = np.zeros(26, dtype = np.int) 
    freq2 = np.zeros(26, dtype = np.int) 
 
    n1 = len(str1)
    n2 = len(str2)
 
    # Store frequency of each
    # character of 'str1'
    for i in range(0, n1):
        freq1[ord(str1[i]) - ord('a') ] += 1
 
    # Store frequency of each 
    # character of 'str2'
    for i in range(0, n2):
         
        freq2[ord(str2[i]) - ord('a')] += 1
 
    # To store the total count
    # of subsequences
    count = 1
 
    for i in range(0, SIZE):
         
        # if chracter (i + 'a') 
        # exists in 'str2'
        if (freq2[i] != 0):
            # if this character's frequency 
            # in 'str2' in less than or
            # equal to its frequency in 
            # 'str1' then accumulate its 
            # contribution to the count
            # of subsequences. If its 
            # frequency in 'str1' is 'n' 
            # and in 'str2' is 'r', then 
            # its contribution wil be nCr,
            # where C is the binomial 
            # coefficient.
            if (freq2[i] <= freq1[i]):
                count = count * binomialCoeff(freq1[i], freq2[i])
 
            # else return 0 as there could
            # be no subsequence which is an
            # anagram of 'str2'
            else:
                return 0
         
    # required count of subsequences
    return count
 
# Driver code
str1 = "abacd"
str2 = "abc"
ans = countSubsequences(str1, str2)
print ("Count = ", ans)
 
 
# This code contributed by saloni1297
