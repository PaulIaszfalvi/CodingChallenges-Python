for i in range(1,106):

    out = ''

    if i % 3 is 0:
        out += "Fizz"
    if i % 5 is 0: 
        out += "Buzz"
    if i % 7 is 0:
        out += "Bazz"
    
    print(out or i)