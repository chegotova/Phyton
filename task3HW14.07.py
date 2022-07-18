a = [ ]             
n = 4   
for i in range (n):  
    new = float (input ('введите 4 числа в виде десятичных дробей через разделитель "."'))  
    a.append (new)      
print (a)
def MaxMin(list):
    for i in range(len(list)):
        list[i]=(round(list[i]%1,2)*100)
    Result=int(max(list)-min(list))
    return f'Разница между остатком дробей {int(max(list))} и {int(min(list))} = {Result}'
print(MaxMin(a))