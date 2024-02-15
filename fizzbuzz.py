
for i in range(1,100):

    output = ""        
       
    if i % 3 == 0:
        output += "Fizz"        
      
    if i % 5 == 0:
        output += "Buzz"        
      
    if not output:
        output = i
        
    print(output)