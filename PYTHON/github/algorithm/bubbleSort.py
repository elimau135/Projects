import math

A = [5,2,8,4,9,7]

for i in range(0, len(A)):
    for j in range(0, len(A)-i-1):
        if A[j]< A[j+1] | A[j]==A[j+1]:
            break
        elif A[j]>A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
            left, right = left+1, right+1

print(A)