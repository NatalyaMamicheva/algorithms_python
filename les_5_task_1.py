import collections

quarter_num = 4
Company = collections.namedtuple("Company", ("name", "quarter_num", "profit"))
all_companies = set()

number = int(input("Введите количество предприятий: "))
total_profit = 0
for i in range(1, number + 1):
    profit = 0
    quarters = []
    name = input(f"Введите название предприятия {i}: ")

    for j in range(quarter_num):
        quarters.append(int(input(f"Прибыль за {j + 1} квартал: ")))
        profit += quarters[j]

    company = Company(name=name, quarter_num=tuple(quarters), profit=profit)

    all_companies.add(company)
    total_profit += profit

average = total_profit / number

print(f"Средняя прибыль всех предприятий = {average}")

for org in all_companies:
    if org.profit > average:
        print(f"Предприятие {org.name} заработало {org.profit}. Его прибыль выше среднего.")

    if org.profit < average:
        print(f"Предприятие {org.name} заработало {org.profit}. Его прибыль ниже среднего.")