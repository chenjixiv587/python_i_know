myList = [10, 20]
for i in range(0, len(myList)):
    for j in range(1, myList[i]):
        print(j, end=" ")
        if myList[i] % j == 3:
            break
# 1 2 3 4 5 6 7  1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
