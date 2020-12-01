num = int(input("Введите натуральное число: "))
obr_num = 0

while num > 0:
    b = num % 10
    obr_num = obr_num * 10
    obr_num = obr_num + b
    num = num // 10

print(f"Обратное число, введенному Вами числу: {obr_num}")
