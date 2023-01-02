# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

import os
os.system("cls")

print("First coordinates")
x = print(int(input('Enter X = ')))
y = print(int(input('Enter Y = ')))
print("Second coordinates")
a = print(int(input('Enter X = ')))
b = print(int(input('Enter Y = ')))

z = ((x - y) ** 2 + (a - b) ** 2) ** (0.5)

print(z)