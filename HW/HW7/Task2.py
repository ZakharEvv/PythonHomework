def discount(point):
    if point <= 49:
        return "10%"
    elif point <= 99:
        return "15%"
    elif point >= 100:
        return "20%"

print(f'Ваша скидка: {discount(56)}')
