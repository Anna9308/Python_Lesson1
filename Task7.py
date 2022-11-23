"""Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N."""
print("Введите число");
n = int(input())
l = []
factorial=1
for i in range(1, n+1):
    factorial*=i
    l.insert(i,factorial)
print(l)