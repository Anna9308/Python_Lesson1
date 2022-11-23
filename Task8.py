"""Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму."""
print("Введите число N");
n = int(input())
l = []
for i in range(0, n):
    l.insert(i,((1+1/n)**n))
sum = 0
for i in l:
    sum += i
print(sum);

