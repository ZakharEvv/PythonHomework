def sum_points():
    sum = 0
    while True:
        name = input("Введите имя студента: ")
        subjects = int(input("Число предметов: "))
        if name.lower() == 'стоп':
            break
        for i in range(subjects):
            point = int(input("Введите баллы: "))
            sum += point
        print(f'Итоговый счёт: {sum}')
        if sum >= 80:
            return 'Наградить дипломом.'
        elif sum >= 50 and sum < 80:
            return 'Наградить похвальной грамотой.'
        else:
            return 'Выдать грамоту об участии.'
