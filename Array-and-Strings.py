from itertools import permutations
from PIL import Image

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

#One Away
def oneAway(s1, s2):
    pass


#NxN matrix rotate 
def rotateMatrix(img):
   

    right, top = img.size 
    left, bottom = 0, 0
    #print(width, height)
    top -= 1
    right -= 1

    while left < right:          
        for i in range(right - left):
            top, bottom = right, left
            coordinates_top = left + i, top          
            temp = img.getpixel(coordinates_top)
           

            coordinates2 = right, top - i
            coordinates3 = right - i, bottom
            coordinates4 = left, bottom + i 

            #if i%500 == 0:
                #print(coordinates_top, coordinates2)

            img.putpixel((coordinates_top), img.getpixel(coordinates2))
            img.putpixel((coordinates2), img.getpixel(coordinates3))
            img.putpixel((coordinates3), img.getpixel(coordinates4))
            img.putpixel((coordinates4), temp)
        right -= 1
        left += 1
        
    #img.rotate(deg).show()     #Python built in image rotate
    return img

    # for w in range(width):
        # for h in range(height):
        #     coordinates1 = width-h-1, w
        #     coordinates2 = w, h
        #    # print(coordinates1, coordinates2)
        #     color1 = img.getpixel(coordinates1)
        #     color2 = img.getpixel(coordinates2)

        #     img.putpixel((coordinates2), color1)
        #     img.putpixel((coordinates1), color2)

    # return img      


#print(isUnique("Hello"))
#print(isPermutation("ABC"))
#print(myIsPermutation("ABC"))
#print(isPermutation("racecar"))

#myString = "Hello World How Are You?      "
#print(URLify(myString, 24))

img = Image.open('Goku.jpg')
image = rotateMatrix(rotateMatrix(img))
image.show()

