time = int(input())
sum = int(input())
if time <= 12 and time >= 10:
    print(sum/2)
elif time <= 20 and time >= 22:
    print(sum/4)
elif time <9 and time>=8:
    print(sum)
elif time <20 and time>12:
    print(sum)
else:
    print("Магазин не работает")