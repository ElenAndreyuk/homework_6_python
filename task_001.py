# Задайте последовательность чисел. 
# Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.


list_1 = [1, 1, 3, 4, 4, 3, 2, 5, 6]
print(*filter(lambda i: list_1.count(i) == 1, list_1))
