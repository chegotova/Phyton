#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

#*Пример:*

#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21

import math 

x1 = float(input(('Введите координаты по оси абсцисс более 0. При вводе дроби используйте разделитель "." ')))
y1 = float(input(('Введите координаты по оси ординат более 0 При вводе дроби используйте разделитель "."')))
x2 = float(input(('Введите координаты по оси абсцисс более 0. При вводе дроби используйте разделитель "." ')))
y2 = float(input(('Введите координаты по оси ординат более 0 При вводе дроби используйте разделитель "."')))
print (round(math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)),2)

