#Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.

list = [str(input('введите строку'))]
check = list
list1 = [str(input('введите строку'))]
x=list1
for x in list:
    if x ==check:
        x = (list.index(x))
        print (x)
check = lambda s: all(x for list in s.lower())
print(check('('))