   
        
#solution with function

def fib(n):
    
    a, b = 0, 1
    for i in range(a, n):
#       print(a, end=' ')
        print(a)
        a, b = b, a+b
    print()

    print(b)
    
fib(50)