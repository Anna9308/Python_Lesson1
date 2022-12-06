"""Напишите программу, удаляющую из текста все слова, содержащие ""абв"""""

def del_words(txt):
    lst1 = list(filter(lambda x: "abc" not in x , txt.split()))
    return " ".join(lst1)

txt = input("Введите текст\n")
print(f"Исходный текст: {txt}")
print(f'Результат: {del_words(txt)}')