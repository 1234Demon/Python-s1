# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)/

import os
os.system("cls")

x = int(input('Enter quarter = '))

if x <= 0 or x > 4:
    print('Wrong quarter')
elif x == 1:
    print('x > 0, y > 0')
elif x == 2:
    print('x < 0, y > 0')
elif x == 3:
    print('x < 0, y < 0')
else:
    print('x > 0, y < 0')