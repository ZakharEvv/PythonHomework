games = []
while True:
    inp = input("Введите игру")
    if inp == "0":
        break
    elif inp in games:
        print("Игра уже есть в списке")
    else:
        games.append(inp)

print(sorted(games))