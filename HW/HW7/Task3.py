studentsCount = int(input("Введите кол-во студентов: "))


def isAccepted(points):
    if points > 50:
        return True
    else:
        return False


for i in range(studentsCount):
    print(isAccepted(int(input("Введите свой балл: "))))
