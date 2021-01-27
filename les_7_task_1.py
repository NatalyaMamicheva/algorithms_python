import random

array = [random.randint(-100, 99) for x in range(10)]
print(f"Начальный массив: {array}")


def bubble():
    n = 1
    while n < len(array):
        sorted_ = True
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted_ = False
        if sorted_:
            break
        n += 1

    print(f"Отсортированный массив: {array}")


bubble()
