#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#*Пример:*

#[2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random
 
 
matrix = [random.randint(0, 6) for item in range(4)]
 
print(matrix)
 
for idx in range(len(matrix) -2):
    pair_mult = matrix[idx+2] * matrix[idx+1]
    print (pair_mult)
