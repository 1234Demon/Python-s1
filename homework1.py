# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

import os
os.system("cls")

a = int(input('Enter number of weekday = '))
if a == 6 or a == 7:
    print('yes')
elif a > 7:
    print('wrong number')
else:
    print('no')