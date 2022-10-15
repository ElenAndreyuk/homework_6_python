# Задайте список из N элементов, заполненных 
# числами из промежутка [-N, N]. Найдите 
# произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
from functools import reduce
n = int(input('введите число: '))
pos = [2, 4, 7]
list_n = [i for i in range(-n, n +1)]
print(list_n)

li = list(map(lambda x: list_n[x],[x for x in pos]))
print(li)
print(reduce(lambda a, b: a* b, li))







