
def countBmi(weight, height):
    index = weight / ((height ** 2) / 10000)
    return index

def bmiResult(weight, height):
    bmi = countBmi(weight, height)
    if bmi < 18.5:
        return "Недостаточный вес"
    elif 18.5 < bmi < 25:
        return "ИМТ в норме"
    elif bmi > 25:
        return "Избыточный вес"

print(bmiResult(int(input("Вес: ")), int(input("Рост: "))))
