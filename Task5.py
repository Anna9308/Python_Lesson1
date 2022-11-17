"""Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве."""
import math
print("Введите координаты точки А");
print("X=");
xa=float(input())
print("Y=");
ya=float(input())
print("Введите координаты точки B");
print("X=");
xb=float(input())
print("Y=");
yb=float(input())
AB=math.sqrt((xb - xa)**2 + (yb - ya)**2)
print(AB);