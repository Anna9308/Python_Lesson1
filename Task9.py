"""Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции."""
list1 = [2,3,5,9,7]
a = 0
for i in list1:
    if (list1.index(i)%2==1):
        a+=i
print(a);