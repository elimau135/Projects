import math

original_list = [6, 14, 8,7,10,13,1,4,3]
newList = []

def sortList():
    for i in range(0, len(original_list)):
        for j in range(0, len(original_list)-i-1):
            if original_list[j]>original_list[j+1]:
                original_list[j], original_list[j+1]= original_list [j+1], original_list[j]
    print(original_list)


def splitList():
    sortList()
    x = len(original_list)
    midValue = math.ceil(x/2)
    index = midValue-1
    print(original_list[index])



splitList()