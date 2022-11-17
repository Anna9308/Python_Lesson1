"""Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат."""
print("Введите X");
x=input()
print("Введите Y");
y=input()
print("Введите Z");
z=input()
left = not(x or y or z)
right = not x and not y and not
if left == right:
    print("Утверждение истинно");
else:
    print("Утверждение ложно");