category = str(input("Категория товара: "))
if category == "продукты":
    money = int(input("введите ценну:"))
    if money <100:
        print("Попробуйте нашу выпечку!")
    elif money >=100 and money <500:
        print("Как насчёт орехов в шоколаде?")
    elif money >=500:
        print("Попробуйте экзотические фрукты!")
else:
    print("Загляните в товары для дома")