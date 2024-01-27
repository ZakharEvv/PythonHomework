amount = input("Введите тег: ")
amount = amount.replace("<span>", "").replace("</span>", "").replace("&nbsp;", "").replace("P", "").replace("Р", "")
print(amount)