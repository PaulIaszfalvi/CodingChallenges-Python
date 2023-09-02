


#Convert spaces to %20
def URLify(s, l):
    newString = s[:l:]      #Cut off white spaces after length given
    return newString.replace(" ", "%20")    #Replace spaces with %20


#print(isUnique("Hello"))
#print(isPermutation("ABC"))
#print(myIsPermutation("ABC"))
#print(isPermutation("racecar"))

#myString = "Hello World How Are You?      "
#print(URLify(myString, 24))

# img = Image.open('Goku.jpg')
# image = rotateMatrix(img)
# image.show()
#img.show()
