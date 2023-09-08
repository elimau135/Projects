
#First part

value = "10110"

# value = [char for char in string] 

# print(len(value))


# calculating binary to decimals for gamma and epsilon.
#use epsilon and gamma for calculating and not value
def calc():
    sum = 0
    for i in range(len(value)-1 , -1, -1):
        if value[i]=="1":
            sum += 2** (len(value)-1-i)


#converting binary to complentary binary
def convertBinary():
    epsilon = list(value) 

    for i in range(0, len(value)):
        if epsilon[i] == "1":
            epsilon[i]= "0"
        else:
            epsilon[i]="1"


    epsilon = ''.join(epsilon)

    print(epsilon)



#getting the most common number in a column of list 
# because there are 1000 lines, if the values 
# are beneath or above 500 it is the most common in this column

         
    print(B)

def mostValue():

    A = []
    gamma = []

    with open("AOC_day3.txt", "r") as f:
        for line in f:
            A.append(line.strip())


    # for i in A:
    #     # print(i)
    #     commonValue = 0
    #     for j in i:
    #         # print(j)
    #
    #         if j == "1":
    #             # print(j, commonValue)
    #             commonValue += 1
    #         if commonValue > 6:
    #             gamme.append("1")
    #         else:
    #             gamma.append("0")



    for i in range(len(A[0])):

        count_0 = 0
        count_1 = 0

        for binary_string in A:
            if binary_string[i]=="0":
                count_0 += 1
            elif binary_string[i]=="1":
                count_1 += 1

        commonBit = "0" if count_0 > count_1 else "1"

        gamma.append(commonBit)

        gammaString = "".join(gamma)




    print(gamma)
    print(gammaString)






#----------------------------------#----------------------------------#----------------------------------

#first we calculate the most commen value also known as gamma
# A = []
# gamma = []
# print("Hello")
#
# with open("AOC_day3.txt", "r") as f:
#     for line in f:
#         A.append(line.strip())
#
# for i in range(len(A[0])):
#     count_0 = 0
#     count_1 = 0
#     for binary_string in A:
#         if binary_string[i]=="0":
#             count_0 += 1
#         elif binary_string[i]=="1":
#             count_1 += 1
#     commonBit = "0" if count_0 > count_1 else "1"
#     gamma.append(commonBit)
#     gammaString = "".join(gamma)
#
#
# #then we convert gamma into epsilon. With this we create a new value
# epsilon = list(A) 
# for i in range(0, len(A)):
#     if epsilon[i] == "1":
#         epsilon[i]= "0"
#     else:
#         epsilon[i]="1"
#         epsilon = ''.join(epsilon)
#
#
# #after this we convert the binary numbers gamma and epsilon into decimals 
# sum = 0
# for i in range(len(gamma)-1 , -1, -1):
#     if A[i]=="1":
#         sum += 2** (len(gamma)-1-i)
# gammaDecimal = sum
#
# sum = 0
# for i in range(len(epsilon)-1 , -1, -1):
#     if value[i]=="1":
#         sum += 2** (len(epsilon)-1-i)
# epsilonDecimal = sum
#
# #calculating the result through gamma*epsilon
# result = gammaDecimal * epsilonDecimal
# print(result)

#ChatGPT corrected

A = []
gamma = []

# Read binary strings from the file "AOC_day3.txt"
with open("AOC_day3.txt", "r") as f:
    for line in f:
        A.append(line.strip())

# Calculate gamma values
for i in range(len(A[0])):
    count_0 = 0
    count_1 = 0
    for binary_string in A:
        if binary_string[i] == "0":
            count_0 += 1
        elif binary_string[i] == "1":
            count_1 += 1
    commonBit = "0" if count_0 > count_1 else "1"
    gamma.append(commonBit)

# Convert gamma to a string
gammaString = "".join(gamma)

# Convert A to epsilon
epsilon = list(gammaString)
for i in range(len(gammaString)):
    if epsilon[i] == "1":
        epsilon[i] = "0"
    else:
        epsilon[i] = "1"
epsilonString = "".join(epsilon)

# Convert binary numbers (gammaString and epsilonString) to decimals
gammaDecimal = int(gammaString, 2)
print("Gamma: ",gammaDecimal)
epsilonDecimal = int(epsilonString, 2)
print("Epsilon: ",epsilonDecimal)

# Calculate the result through gamma * epsilon
result = gammaDecimal * epsilonDecimal
print(result)


#-------------------------------
#-------------------------------
#-------------------------------
#-------------------------------
#-------------------------------
#-------------------------------

#Part two


A=[]

with open("testvalues.txt","r") as f:
    for line in f:
        A.append(line.strip())

binaryValue = []
ogr = 0 #oxygen generator rating -> most common value
csr = 0 #C02 scrubber rating -> least common value
lsr = 0 #result -> lsr = ogr * csr

# while len(binaryValue) != 1:
#     for i in range (len(A[0])):
#         count0=0
#         count1=0
#         for binaryString in A:
#             if binaryString[i] == "0":
#                 count0+=1
#             elif binaryString[i]=="1":
#                 count1+=1
#         mostCommonBit = "0" if count0 > count1 else "1"
#         index = int(mostCommonBit)
#         binaryValue.append(binaryString[index])



# while len(binaryValue) != 1:
#     for i in range (len(A[0])):
#         count0=0
#         count1=0
#         for binaryString in A:
#             if binaryString[i] == "0":
#                 count0+=1
#             elif binaryString[i]=="1":
#                 count1+=1
#         mostCommonBit = "0" if count0 > count1 else "1"
#         index = int(mostCommonBit)
#         if binaryString[i]== binaryString[index]:
#             binaryValue.append(binaryString[i])
#
# print(binaryValue)











A = []

# Read binary strings from the file "testvalues.txt"
with open("testvalues.txt", "r") as f:
    for line in f:
        A.append(line.strip())

binaryValue = []

while len(binaryValue) != 1:
    common_bits = []  # List to store common bits at each index
    
    for i in range(len(A[0])):
        count_0 = 0
        count_1 = 0
        for binaryString in A:
            if binaryString[i] == "0":
                count_0 += 1
            elif binaryString[i] == "1":
                count_1 += 1
        mostCommonBit = "0" if count_0 > count_1 else "1"
        
        # Check if there is more than one common bit at this index
        if count_0 > 0 and count_1 > 0:
            common_bits.append(mostCommonBit)
        
    # If there are common bits at any index, append them to binaryValue
    if common_bits:
        binaryValue.extend(common_bits)
    else:
        # If no common bits found, pick the most common bit from the last index
        count_0 = sum(1 for binaryString in A if binaryString[-1] == "0")
        count_1 = len(A) - count_0
        mostCommonBit = "0" if count_0 > count_1 else "1"
        binaryValue.append(mostCommonBit)

print(binaryValue)





