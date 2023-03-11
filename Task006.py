num = int(input('Введите номер билета: '))
left = 0
right = 0

leftnum = num // 1000
rightnum = num % 1000

while(leftnum > 0):
    a = leftnum % 10
    left = left + a
    leftnum = leftnum // 10

while(rightnum > 0):
    a = rightnum % 10
    right = right + a
    rightnum = rightnum // 10

if (left == right):
    print('yes')
else:
    print('no')