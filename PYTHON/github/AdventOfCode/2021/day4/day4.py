#Part one

drawOrder = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
values = []
inputList = []
bingoList = []
bingoNumbers = []

def create_bingo_board(board):
    
    
    
    
    
def check_winning():
    


















#store the values that are for the winning conditions in a list that is called inputlist
with open('testvalues.txt', 'r') as f:
    for i,line in enumerate(f):
        values.append(line.strip())
        if i == 0:
            break
        
    for i, line in enumerate(f):
        bingoList.append(line.strip())    
        
bingoList.pop(0) # remove the first value from bingoList
inputList = values[0].split(',') #split up the values that are split with ,

#append the bingo values to each other because they are split at the moment
bingoField1 = []

for i in range(len(bingoList)):
    input_string = bingoList[i]
    newValues = [int(val) for val in input_string.split()]
    for j in range(len(newValues)):
        bingoField1.append(newValues[j])
    if i == 4:
        break
print(input_string)
print(bingoField1)

for i in range(len(inputList)):
    for j in range(len(bingoField1)):
        if inputList[i] == str(bingoField1[j]):
            bingoNumbers.appends(int(inputList[i]))

print(bingoNumbers)








#Part two



