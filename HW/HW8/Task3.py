def recursiveSum():
    sum = 0
    n = input('Введите число: ')
    if n != '':
        return int(n) + sum + recursiveSum()
        sum += int(n)
    else:
        return 0.0

print(recursiveSum())
