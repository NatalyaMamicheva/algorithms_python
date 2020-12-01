n = int(input("Введите количество элементов: "))
num = -0.5

def sum_n(num, n):
    if (n == 0):
        return 1
    else:
        return (num * sum_n(num, n - 1))

print(f"Сумма n элементов = {sum_n(num, n)}")