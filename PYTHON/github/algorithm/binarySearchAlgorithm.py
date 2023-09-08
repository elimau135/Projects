import math

A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
n = len(A)
T = 13  # Targetvalue 
middle = math.ceil(n/2)
midValue = A[middle]

L = 0
R = n-1

while L <=R:
    if T > midValue:
        middle = middle + (len(A)-middle)/2
        print(middle)
        L= L+1

    elif T< midValue:
        middle = middle - (len(A)/2-middle)/2
        print(middle)
        L=L+1
        
    else:
        print("Value was found immediatly")
        L = R+1
