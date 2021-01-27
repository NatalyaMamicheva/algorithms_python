import random

array = [round(random.uniform(0, 50), 1) for i in range(10)]
print(f"Начальный массив: {array}")


def sort(array):
    if len(array) == 1:
        return array

    middle = len(array) // 2  # это середина списка
    left = sort(array[:middle])
    right = sort(array[middle:])
    i = 0
    j = 0

    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            array[i + j] = left[i]
            i += 1
        else:
            array[i + j] = right[j]
            j += 1

    if len(left) > i:
        array[i + j] = left[i]
        i += 1
    if len(right) > j:
        array[i + j] = right[j]
        j += 1

    return array


sort(array)
print(f"Отсортированный массив: {array}")