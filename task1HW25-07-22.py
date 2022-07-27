#1- Определить, присутствует ли в заданном списке строк, некоторое число

# import random
# num = [random.randint(0, 100) for i in range(20)]
 
# print(num)

# a = int (input('enter a'))
# int = a
# def filter_input(in_num):
#     if (in_num) == a:
#         return True
#     else:
#         return False

# out_filter = filter(filter_input, num)

# print("Отфильтрованный список: ", list(out_filter))
idss = []
i = 1
print('Введи данные. Пустая строка - выход')
while True:
    ids = input(f'{i}. ')
    if not ids:
        break
    idss.append(ids)
    i += 1
 
for ids in idss:
    print(ids)

print(list(filter(str.isdigit, idss)))