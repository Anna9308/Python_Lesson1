#дан список a = [4, 3, -10, 1, 7, 12], изменить его а=[4, -10, 12, 3, 1, 7]

a = [4, 3, -10, 1, 7, 12]
a.sort(key=lambda x: x%2)
print(a)