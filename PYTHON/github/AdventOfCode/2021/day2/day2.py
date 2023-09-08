#solution one

print("Solution one: ")
A=[]

with open("AOC_day2.txt","r") as f:
    for line in f:
        A.append(line.strip())

increaseValue = 0
horizontalValue = 0
depthValue = 0

value = A[0]

halfValue = value.split()
# for line in A:
for i in range(len(A)):
    if len(halfValue) == 2:
        value = A[i].split()
        command = str(value[0])
        nmr = int(value[1])
        if command == "forward":
            horizontalValue += nmr
        elif command == "up":
            depthValue -= nmr
        elif command == "down":
            depthValue += nmr


print(horizontalValue, depthValue)
result = horizontalValue * depthValue

print("The result is: ", result)

result = 0
#solution two

print(" ")
print(" ")
print(" ")
print(" ")
print("Solution two")


A=[]

with open("AOC_day2.txt","r") as f:
    for line in f:
        A.append(line.strip())

x = 0
y = 0 
aim = 0


for i in range(len(A)):
        value = A[i].split()
        command = str(value[0])
        nmr = int(value[1])
        if command == "forward":
            x += nmr
            if aim == 0 and aim == y:
                y = 0 
            else:
                y += nmr*aim
        elif command == "down":
            aim += nmr
        elif command == "up":
            aim -= nmr
        print(nmr, aim, x, y)

print("--------")

print(x, y)

result = x * y 

print("The result is: ", result)
