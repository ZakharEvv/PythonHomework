dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5'
}

a = dict['five']
dict['five'] = dict['one']
dict['one'] = a
dict.pop('two')
dict['new_key'] = ('new_value')
print(dict)
