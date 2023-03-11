n = int(input('Введите первое значиение: '))
m = int(input('Введите второе значение: '))
k = int(input('Введите количество долек: '))

if (k % n == 0 or k % m == 0):
    print('Yes')
else:
    print('No')