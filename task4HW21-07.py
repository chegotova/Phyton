#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах. При декодировании попробуйте сделать через четный-нечетный элемент.
print()
s = input('введите данные')
f = open('text.txt', 'wt')

def main():
   
    rle = s
    encoded = encode(rle)
    decoded = decode(encoded)
 
    print("введенные данные:  " + rle)
  
    print("сжатый результат: " + formatOutput(encoded))
 
    print("восстановленный результат: " + decoded)
 
 
def encode(sequence):
    
    count = 1
    result = []
 
    for x,item in enumerate(sequence): 
        if x == 0:
            continue
        elif item == sequence[x - 1]:
            count += 1
        else:        
            result.append((sequence[x - 1], count))
            count = 1            
    
    result.append((sequence[len(sequence) - 1], count))

 
    return result
    f.write(s)
    f.close()

f = open('text1.txt', 'wt') 
def decode(sequence):
    
    result = []
 
    for item in sequence:
        result.append(item[0] * item[1])
 
    return "".join(result)
 
 
def formatOutput(sequence):
    
    result = []
 
    for item in sequence:
        if (item[1] == 1):
            result.append(item[0])
        else:
            result.append(str(item[1]) + item[0])
 
    return "".join(result)
    
 
if __name__ == "__main__":
    main()
    
f.write(s)
f.close()

