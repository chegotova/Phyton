# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
#'абвгдейка - это передача' = >" - это передача"


a = input ('введите текст')
a = a.lower().split()
i = 0
while i < len(a):
  if a[i].startswith('абв'):
    del a[i]
    continue
  i += 1
  print (a)