
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

A = []
list1=[]
# Read binary strings from the file "testvalues.txt"
with open("AOC_day3.txt", "r") as f:
    for line in f:
        A.append(line.strip())

for i in range(len(A[0])):
    list1.clear()
    count0 = 0 
    count1 = 0 
    commonValue = 0 
    for j in A:
        if j[i]== "1":
            count1+=1
        elif j[i]=="0":
            count0+=1
    commonValue = '1' if count1 >= count0 else '0'
    
    for j in A:
        if j[i] == commonValue:
            list1.append(j)
        
    A = list1.copy()
   
    

    if len(A) == 1:
        print(A)
        value1 = A[0]
        break

sum1 = 0
for i in range(len(value1)-1 , -1, -1):
    if value1[i]=="1":
        sum1 += 2** (len(value1)-1-i)
print(sum1)
ogr = sum1
    
    
#least common value
    
B = []
list2 = []
uncommonValue = 0 

with open('AOC_day3.txt', 'r') as f:
    for line in f:
        B.append(line.strip())
        
for i in range(len(B[0])):
    list2.clear()
    count0 = 0 
    count1 = 0
    commonValue = 0 
    for j in B:
        if j[i] == '1':
            count1 += 1
        elif j[i] == '0':
            count0 += 1
    uncommonValue = '0' if count1 >count0 or count1 == count0 else '1'
    
    
    for j in B:
        if j[i] == uncommonValue:
            list2.append(j)
    
    B = list2.copy()

    if len(B) == 1:
        print(B)
        value2 = B[0]
        break
    

sum2 = 0
for i in range(len(value2)-1 , -1, -1):
    if value2[i]=="1":
        sum2 += 2** (len(value2)-1-i)
print(sum2)
csr = sum2




lsr = ogr * csr

print(lsr)





