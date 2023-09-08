  
class Main:
    
    i=int(0)
    nmr=int(input('Choose a number '))
    is_prime = True
    
    for i in range(2, nmr):
        if nmr%i == 0:  #modulo operator -> 21%5 -> 1
            is_prime = False
            break
    
    if is_prime:
        print(nmr, ' is a prime ')
    else:
        print(nmr, ' is not a prime')