"""Задайте последовательность чисел.
Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности."""

numbers=[1, 2, 3, 5, 10, 10, 4, 1, 2]
n=set(numbers)
print("Отфильтрованный список: ", list(n))