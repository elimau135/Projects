values = []
inputList = []
bingoList = []
bingoNumbers = []

# Store the values that are for the winning conditions in a list called inputlist
with open('testvalues.txt', 'r') as f:
    for i, line in enumerate(f):
        values.append(line.strip())
        if i == 0:
            break
        
    for i, line in enumerate(f):
        bingoList.append(line.strip())

bingoList.pop(0)  # remove the first value from bingoList
inputList = values[0].split(',')  # split up the values that are split with ,

# Append the bingo values to each other because they are split at the moment
bingoField1 = []

for i in range(len(bingoList)):
    input_string = bingoList[i]
    newValues = [int(val) for val in input_string.split()]
    for j in range(len(newValues)):
        bingoField1.append(newValues[j])
    if i == 4:
        break

print('input_string:', input_string)
print('bingoField1:', bingoField1)

# Compare values and insert into bingoNumbers
for i in range(len(inputList)):
    for j in range(len(bingoField1)):
        if str(bingoField1[j]) ==inputList[i]:  # Convert to string for comparison
            bingoNumbers.append(int(inputList[i]))  # Insert matching values

print('bingoNumbers:', bingoNumbers)



#winconditionz