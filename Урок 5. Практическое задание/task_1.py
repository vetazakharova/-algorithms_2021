"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1

Предприятия, с прибылью ниже среднего значения: Фирма_2
"""
from collections import namedtuple

def firm_rev_count():
    num_firms = int(input("Введите количество компаний: "))
    FIRMS = namedtuple("Firm", "name first_q second_q third_q fourth_q")
    average_rev = {}

    for i in range(num_firms):
        FIRM = FIRMS(
        name = input("введите название компании: "),
        first_q = int(input("прибыль за первый квартал: ")),
        second_q = int(input("прибыль за второй квартал: ")),
        third_q = int(input("прибыль за третий квартал: ")),
        fourth_q = int(input("прибыль за четвертый квартал: "))
        )
        average_rev[FIRM.name] = (FIRM.first_q + FIRM.second_q + FIRM.third_q + FIRM.fourth_q) / 4

    average_rev_all = 0
    for i in average_rev.values():
        average_rev_all += i
    average_rev_fin = average_rev_all / num_firms

    print("Средняя годовая прибыль всех предприятий:", average_rev_fin)
    for key, value in average_rev.items():
        if value < average_rev_fin:
            print(f"Предприятие, с прибылью ниже среднего значения: {key}")
        elif value > average_rev_fin:
            print(f"Предприятие, с прибылью выше среднего значения:{key}")
        else:
            print(f"Прибыль предприятия {key} равна среднему значению")

firm_rev_count()
