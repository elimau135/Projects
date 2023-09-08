import math

user_list = [14, 5, 6, 8, 13, 10, 1, 3, 2]
searchValue = 5
middleValue = math.ceil(len(user_list)/2)

for i in range(0, len(user_list)):
    for j in range(0, len(user_list)-i-1):
        if user_list[j]>user_list[j+1]:
            user_list[j], user_list[j+1] = user_list[j+1], user_list[j]

for i in range(0, len(user_list)):
    if searchValue == user_list[i]:
        print(user_list)
        print("Value was found at index: ", i-1)
        break
