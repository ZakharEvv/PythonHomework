teachers = []
while True:
    teachers.append([
        input("Введите фамилию преподователя: "),
        input("Должность: "),
        input("Список учеников: ").split()
    ])
    print(teachers)