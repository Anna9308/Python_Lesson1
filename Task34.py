#Вводится строка. Требуется, используя введенную строку, сформировать N=10 пар кортежей в формате:
#(символ, порядковый индекс)
#Используя функцию zip сформируйте указанные кортежи и сохраните в список с именем lst.

a = "ghfgh dfere uitt"
str1 = list(zip(a,range(0,len(a))))
print(str1)
