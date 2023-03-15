lenhgt = int(input('Введите длину строки: '))
c = 1
while 2 ** c and c <= lenhgt:
    print(2 ** c, end =' ')
    c += 1