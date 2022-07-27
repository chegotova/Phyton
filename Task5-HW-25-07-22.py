import random


def digit_check():
    try:
        lenght = int(input('Задайте размер списка:\n'))
        return lenght
    except ValueError:
        print('Это должно быть число!\n')
        digit_check()


size = digit_check()

lst = []
for i in range(0, 11):
    for i in range(0, size):
        lst.append(random.randint(0, 10))
print(lst)

def get_poduct(list):
    product = []
    stop = int(len(list)/2)
    j = len(list)-1
    for i in range(0, stop):
        product.append(list[i] * list[j])
        j -= 1
    if len(list) % 2 > 0:
        for i in range(0, stop):
            product.append(list[i] * list[j])
            j -= 1
        product.append(list[j]**2)
    else:
        for i in range(0, stop):
            product.append(list[i] * list[j])
            j -= 1
        return product


prod = get_poduct(lst)
print(prod)