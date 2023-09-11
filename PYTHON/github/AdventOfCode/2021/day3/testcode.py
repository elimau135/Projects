# A=[]
#
# nmrlist = []
# commonValue = 0 
# with open("testvalues.txt", "r") as f:
#     for line in f:
#         A.append(line.strip())
#
# while nmrlist != 1:
#
#     for i in range(len(A[0])):
#         countZero = 0 
#         countOne = 0
#         for binaryString in A:
#             if binaryString == "1":
#                 countOne += 1
#             elif binaryString == "0":
#                 countZero += 1 
#
#         commonValue = "0" if countZero >= countOne else "1"
#         if binaryString[i] == commonValue:
#             print(binaryString[i], commonValue)
#             nmrlist.append(line)
#             print(nmrlist)
#         elif binaryString[i] != commonValue:
#             nmrlist.remove(binaryString[i]!=commonValue) 
#             print(nmrlist)


A = []
nmrlist = []

with open("testvalues.txt", "r") as f:
    for line in f:
        A.append(line.strip())

while nmrlist != []:
    countZero = 0
    countOne = 0
    for binaryString in A:
        if binaryString[i] == "1":
            countOne += 1
        elif binaryString[i] == "0":
            countZero += 1

    commonValue = "0" if countZero >= countOne else "1"

    filtered_binary_strings = []

    for binaryString in A:
        if binaryString[i] == commonValue:
            print(binaryString[i], commonValue)
            nmrlist.append(line)
            print(nmrlist)
        else:
            filtered_binary_strings.append(binaryString)

    A = filtered_binary_strings

print(A)
