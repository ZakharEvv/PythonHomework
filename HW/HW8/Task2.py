def price(distance):
    base = 4
    plus = 0.25
    return (round((base + plus * distance / 140), 2))


print("Ваша стоимость за проезд: ", price(int(input("Введите расстояние поездки: "))))

