# апишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

import os
os.system("cls")

x = int(input('Enter X = '))
y = int(input('Enter Y = '))

if x == 0 or y == 0:
    print('Enter not 0')
elif x > 0 and y > 0:
    print('1 quarter')
elif x < 0 and y > 0:
    print('2 quarter')
elif x < 0 and y < 0:
    print('3 quarter')
else:
    print('4 quarter')