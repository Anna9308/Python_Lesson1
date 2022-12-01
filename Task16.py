"""Напишите программу, удаляющую из текста все слова, содержащие ""абв"""""

def del_words(txt):
    lst1 = list(filter(lambda x: "abc" not in x , txt.split()))
    return " ".join(lst1)

txt = input("Введите текст\n")
print(f"Исходный текст: {txt}")
print(f'Результат: {del_words(txt)}')

"""data = open("text.txt", "w")
data.write(input())
data.close()

data = open("text.txt", "r+")
del_words(data)
data.close()
"""