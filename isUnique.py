

#Check to see if the string provided contains all unique elements
def isUnique(s):
    lengthOfString = len(s)
    stringSet = set(char for char in s)     #create a set of items using the elements of the string
    return len(stringSet) == lengthOfString     #if length of string doesn't match length of set, ther are duplicates