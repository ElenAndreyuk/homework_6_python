# Задайте список из n чисел последовательности 
# по формуле (1+ 1 /n)**n и выведите на экран их сумму.
# Пример:
# - Для n = 6: [2, 2, 2, 2, 2, 3]   13
n = int(input('введите число: '))

print(sum(list(map(lambda i: round( (1 + 1/i)**i ), [i for i in range(1, n+1)]))))    
