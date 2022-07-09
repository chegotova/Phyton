#2- Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = float(input(('Введите x')))
y = float(input(('Введите y')))
z = float(input(('Введите z')))
f=[x,y,z]
print(f)
if f == -(x+y+z) and f ==(x*-y*-z):
    print('true')
else:
    print('false')