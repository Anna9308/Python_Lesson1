"""Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится)."""
print("Введите X");
x=int(input())
print("Введите Y");
y=int(input())
if (x>0 and y >0):
    print("Точка находится в I четверти");
elif (x<0 and y>0):
    print("Точка находится во II четверти");
elif (x<0 and y<0):
    print("Точка находится в III четверти");
elif (x>0 and y<0):
    print("Точка находится в IV четверти");
elif (x==0 and y!=0):
    print("Координата находится на оси Y");
elif (y==0 and x!=0):
    print("Точка находится на оси X");
else:
    print("Вы ввели точку с координатами (0,0)");