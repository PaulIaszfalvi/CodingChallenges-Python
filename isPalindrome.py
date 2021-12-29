

#Checks for palindrome
def isPalindrome(s):
    stringReverse = s[::-1]     #Flips the string
    return s == stringReverse       #Compares the original to the reversed