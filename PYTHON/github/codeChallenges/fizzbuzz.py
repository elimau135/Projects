class FizzBuzz:
    
    x = int(1)
    user_input = int(input('Please type in a value from the type integer: '))
    f=str('fizz')
    b=str('buzz')
    fb = str('fizz buzz')
        
    for x in range(x, user_input+1):
        if x%3==0 and x%5==0:
            print(fb)
        elif x%3==0:
            print(f)
        elif x%5==0:
            print(b)
        else:
            print(x) 
            
    
    
    
