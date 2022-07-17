#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

#*Пример:*

#- [1.1, 1.2, 3.1, 5.561, 10.01] => 0.56 или 56

import random
import math
 
number = 123.345
split_number = list(str(number).split('.'))
print(split_number)
 
matrix = [random.uniform (2, 6) for item in range(4)]
for x in range(len(matrix)):
   print  (math.modf(x))
    if 
 
