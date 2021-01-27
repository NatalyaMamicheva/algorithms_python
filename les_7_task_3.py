import random

m = 5
size = (2 * m) + 1
massiv = [random.randint(0, 50) for i in range(size)]

print(f"Начальный массив: {massiv}")


def mediana(massiv):
    for i in massiv:
        m = 0

        for j in massiv:
            if i < j:
                m += 1

        if len(massiv) == ((2 * m) + 1):
            return i


print(f"Медиана в массиве: {mediana(massiv)}")
print(f"Отсортированный массив: {sorted(massiv)}")