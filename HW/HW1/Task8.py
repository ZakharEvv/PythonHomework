num = int(input())
first_num = num // 100
ost = num % 100
second_num = ost // 10
third_num = ost % 10
sum = third_num + second_num + first_num
print(sum)