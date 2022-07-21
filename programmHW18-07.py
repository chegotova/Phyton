#4- В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.
#В файле содержится, например:
#Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны.

print()
s = input()
f = open('text.txt', 'wt')
without_digit = [word for word in s.split() if not any(digit.isdigit() for digit in word)]
f.write(s)
f.close()
print(without_digit)