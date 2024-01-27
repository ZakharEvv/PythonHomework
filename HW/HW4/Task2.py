while True:
    if input() == "game":
        print("Угадайте число, у вас три попытки")
        for i in range(3):
            inp = input()
            if inp == "off":
                break
            elif int(inp) == 5:
                print("Вы выиграли билет на концерт")
                break
            else:
                print("Неверно")
        print("Игра окончена")