A = [2,6,5,4,9,14, 11,13, 8,1]

for i in range(0, len(A)):

    for j in range(0, len(A)-i-1):
        if A[j]> A[j+1]:
            for k in range(len(A), 0, -1):
                if A[j]>A[j+1]:
                    A[j], A[j+1] = A[j+1], A[j]
                else: 
                    break
print(A)


#code that chatGPT provided:

A = [2, 6, 5, 4, 9, 14, 11, 13, 8, 1]

for i in range(1, len(A)):
    key = A[i]
    j = i - 1

    while j >= 0 and key < A[j]:
        A[j + 1] = A[j]
        j -= 1

    A[j + 1] = key

print(A)
