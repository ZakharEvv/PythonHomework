arr = input("Введите последовательность чисел: ").split(" ")
isIncreasing = True
for i in range(len(arr) - 1):
    if int(arr[i+1])-int(arr[i]) != 1:
        isIncreasing = False
        break

if isIncreasing:
    print("Возрастает непрерывно")
else:
    print("Возрастает не непрерывно :)")