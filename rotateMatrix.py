

from PIL import Image
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

