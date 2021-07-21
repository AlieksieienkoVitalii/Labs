myList = [1, 1]
steps = int(input('Введите количество ступеней - '))
for i in range(steps - 2):
    myList.append(myList[len(myList) - 1] + myList[len(myList) - 2])
print("Количество способов чтобы забраться на лестницу - " + str(myList[len(myList)-1]))

