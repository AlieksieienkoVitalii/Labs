start = int(input("Укажите начало диапазона - "))
end = int(input("Укажите конец диапазона - "))
result = []
for i in range(start, end + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        result.append(i)
print(result)

