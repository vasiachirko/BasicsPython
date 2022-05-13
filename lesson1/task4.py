numStr = input()
num = int(numStr)

#Решение 1
max2 = 0
while num != 0:
    cif = num % 10
    if cif > max2:
        max2 = cif
    num //= 10
print(max2)

#Решение 2
print(max(list(numStr)))
