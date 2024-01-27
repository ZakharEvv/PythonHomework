songs = dict()
while True:
    place = input('Место: ').lower()
    if place != 'off':
        songs[place, input('Исполнитель: ').lower()] = input('Песня:').lower()
        print(songs)
    else:
        print('До свидания')
        break
