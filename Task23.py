"""Задайте список из нескольких чисел.
Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции."""

list1 = [2,3,5,9,7]

def even_items(iterable):
    return [v for i, v in enumerate(iterable, start=0) if i % 2]

print(even_items(list1))
s = sum(even_items(list1))
print(s)