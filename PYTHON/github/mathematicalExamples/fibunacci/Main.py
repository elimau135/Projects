class Main:

    startvalue1 = int(0)
    startvalue2 = int(1)
    i = int(0)
    currentValue = None
    stop = int(input('Choose the stop value'))    
    
    for i in range(i,stop):
        currentValue = startvalue1 + startvalue2
        startvalue1 = startvalue2
        startvalue2 = currentValue
        print(currentValue)
        
        
#solution with function

def fib(n):
    
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()