pro = int(input("первый товар"))
pro_2 = int(input("второй товар"))
pro_3 = int(input("третий товар"))
sum = pro + pro_2 + pro_3
if pro <pro_2 and pro_2 <pro_3:
    print("Акцмя!")
    print(sum/2)
elif pro_3 <pro_2 and pro <pro_2:
    print("Акция!")
    print(sum/3)
else:
    print("К оплате:")
    print(sum)