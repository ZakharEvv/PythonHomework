login = input('Логин: ')
forbidden_characters = '=?*^$№@_'
for i in forbidden_characters:
    if i in login:
        print('Запрещенный символ', i)