from functools import reduce
def create_tuples(values, ind):
    return list(zip(ind, values))


def filtr(array):
    for i in range(len(array)-1, -1, -1):
        num = []
        for c in array[i][1]:
            num.append(ord(c))
        if sum(num) % array[i][0] == 0:
            lang = array[i][1].upper()
            del array[i]
            array.insert(i, (reduce(lambda x,y: x + y, num), lang))
        else:
            del array[i]
    return array

lan = ['python', 'c#', 'Qbasic', 'SQL', 'Pascual', 'C++',
     'XML', 'HTML']
num = [1, 2, 3, 4, 5, 6, 7, 8]
my_tup = create_tuples(lan, num)
print(my_tup)
res = filtr(my_tup)
print(res)




