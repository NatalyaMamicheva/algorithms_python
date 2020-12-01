num = int(input("Введите натуральное число: "))

chetn = 0
nechetn = 0

while num > 0:
    if num % 2 == 0:
        chetn += 1
    else:
        nechetn += 1
    num = num // 10

print(f"Четных чисел: {chetn} Нечетных чисел: {nechetn}")
