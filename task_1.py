# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.

number = int(input("Введите размер списка: "))
list = [ ]
sum = 0
for i in range(number):
    list_number = int(input(f"Введите число {i+1} "))
    list.append(list_number)
    if i % 2 != 0:
        sum += list[i]

print(list)
print(f"Сумма нечетных чисел равна {sum}")
