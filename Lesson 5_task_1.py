# 1.Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import defaultdict

d_dict = defaultdict(list)

amount = int(input('Введите количество оцениваемых предприятий: '))
for i in range(0, amount):
    name_x = input('Введите юр. лицо предприятия: ')

    for j in range(1, 5):
        profit = int(input(f'\tВведите прибыль {name_x} за {j} квартал: '))
        d_dict[name_x].append(profit)
        j += 1
    i += 1
# print(d_dict)

s = 0
for val in d_dict.values():
    s += sum(val)
ave = round(s / amount, 2)
print(f'Средняя прибыль всех предприятий за год: {ave} \n')

list_profit = []
list_loss = []
for i in range(0, len(d_dict)):
    if (sum(list(d_dict.values())[i])) >= ave:
        list_profit.append(list(d_dict.keys())[i])
    else:
        list_loss.append(list(d_dict.keys())[i])

print('Прибыльные предприятия:', ", ".join(list_profit))  # если не через запятую, то можно просто *list_profit
print('Убыточные предприятия:', ", ".join(list_loss))  # если не через запятую, то можно просто *list_loss
