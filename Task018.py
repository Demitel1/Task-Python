number = int(input('Введите количество элементов массива: '))
I = input("Введите целые числа: ").split()
A = list(map(int, I))
if len(A) != number or number == 0:
    print('Введенные элементы не соответствуют заявленному количеству!')
else:   
    X = int(input('Введите число, с которым необходимо сравнивать элементы списка: '))
    min = abs(X - A[0])
    index = 0
    for i in range(1, number):
        count = abs(X - A[i])
        if count < min:
            min = count
            index = i
    print(f'Число {A[index]} в списке наиболее близко по величине к {X}, разница = {abs(X - A[index])}')