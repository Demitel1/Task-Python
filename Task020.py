list_l = {1:"AEIOULNSTRАВЕИНОРСТ",
                2:"DGДКЛМПУ",
                3:"BCMPБГЁЬЯ",
                4:"FHVWYЙЫ",
                5:"KЖЗХЦЧ",
                8:"JXШЭЮ",
                10:"QZФЩЪ"}

word = input("Введите слово: ").upper()
sum = 0
for i in word:
    for k, v in list_l.items():
        if i in v:
            sum += k
print(f"Стоимость слова: {sum}")