"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать где какая сложность.

Примечание:
Построить список можно через списковое включение.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""

"""Cложность: n^2"""

list1 = list(range(1, 1000))
min = list1[0];
for i in range(0, len(list1)):
    if i<min:
        min = i
print("Минимальное значение списка:" min)

"""Сложность: nlogn"""

list1 = list(range(1, 1000)) #1
list1.sort() #nlogn
min = list1[0] #1
print("Минимальное значение списка:" min)
