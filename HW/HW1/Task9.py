num = int(input())
first_num = num // 100
ost = num % 100
second_num = ost // 10
third_num = ost % 10
finally_num = third_num * 100 + second_num * 10 + first_num
print(finally_num)