numStr = input()
digit = int(numStr)

#Проверка валидности
if digit < 0 or digit > 9:
    print('input is not a digit')

#Решение1
numnumStr = numStr + numStr
tripleNumStr = numnumStr + numStr
tripleNumStr2 = numStr * 3 #Другой способ склеивания строк
print(int(numStr)+int(numnumStr)+int(tripleNumStr))
