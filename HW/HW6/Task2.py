numbers = "010293478389201134089567348076"
dict_num = {}
for i in range(0, 10):
    dict_num[i] = numbers.count(str(i))
print(dict_num)
