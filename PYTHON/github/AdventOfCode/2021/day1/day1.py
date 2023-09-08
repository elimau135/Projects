# A = []
#
# increaseValue = 0 
#
# with open("AOC_day1.txt","r") as f:
#     for line in f:
#         A.append(int(line))
#
# for i in range(len(A)):
#     if A[i] < A[i+1]:
#     # print(A[i])
#         increaseValue += 1
#
# print(increaseValue)


valueOne = None
valueTwo = None

#Aufgabenteil 1 nur mit einer line
A = []

with open("AOC_day1.txt", "r") as f:
    for line in f:
        # Convert the line to an integer
        A.append(int(line))

increaseValue = 0

# Loop up to the second-to-last element to avoid IndexError
for i in range(len(A) - 1):
    if A[i] < A[i + 1]:
        increaseValue += 1

print(increaseValue)

# increaseValue = 0


#Aufgabenteil 2 mit dem Triple

# for i in range(len(A)-2):
#     valueOne = A[i] + A[i+1] + A[i+2]
#     valueTwo = A[i+1] + A[i+2] + A[i+3]
#
#     if valueOne < valueTwo:
#         increaseValue += 1
#
# print(increaseValue)



increaseValue = 0

# Loop through the list up to the third-to-last element
for i in range(len(A) - 3):
    # Calculate the sum of the current triple and the next triple
    valueOne = A[i] + A[i + 1] + A[i + 2]
    valueTwo = A[i + 1] + A[i + 2] + A[i + 3]

    # Compare the sums of the two triples
    if valueOne < valueTwo:
        increaseValue += 1

print(increaseValue)

