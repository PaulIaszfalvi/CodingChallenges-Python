from itertools import permutations

#Check to see if the string provided contains all unique elements
def isUnique(s):
    lengthOfString = len(s)
    stringSet = set(char for char in s)     #create a set of items using the elements of the string
    return len(stringSet) == lengthOfString     #if length of string doesn't match length of set, ther are duplicates

#checks if s
def isPermutation(s):
    a = permutations(s[::], len(s))
    for item in a:
        print(item)
#Permutation 
def myIsPermutation(s):
    if len(s) == 1:     #Base Case
        return [s]
    
    perms = myIsPermutation(s[1:])
    char = s[0]
    result = []

    for perm in perms:
        for i in range(len(perm)+1):
            result.append(perm[:i] + char + perm[i:])   #iterate through items and place char in every spot between them
    
    return result

#Checks for palindrome
def isPalindrome(s):
    stringReverse = s[::-1]     #Flips the string
    return s == stringReverse       #Compares the original to the reversed

#Convert spaces to %20
def URLify(s, l):
    newString = s[:l:]      #Cut off white spaces after length given
    return newString.replace(" ", "%20")    #Replace spaces with %20

#print(isUnique("Hello"))
print(isPermutation("ABC"))
print(myIsPermutation("ABC"))
#print(isPermutation("racecar"))

#myString = "Hello World How Are You?      "
#print(URLify(myString, 24))
