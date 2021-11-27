
#Check to see if the string provided contains all unique elements
def isUnique(s):
    lengthOfString = len(s)
    stringSet = set(char for char in s)     #create a set of items using the elements of the string
    return len(stringSet) == lengthOfString     #if length of string doesn't match length of set, ther are duplicates

#Checks for permutation
def isPermutation(s):
    stringReverse = s[::-1]     #Flips the string
    return s == stringReverse       #Compares the original to the reversed

#Convert spaces to %20
def URLify(s, l):
    newString = s[:l:]      #Cut off white spaces after length given
    return newString.replace(" ", "%20")    #Replace spaces with %20

print(isUnique("Hello"))
print(isPermutation("Hello"))
print(isPermutation("racecar"))

myString = "Hello World How Are You?      "
print(URLify(myString, 24))
