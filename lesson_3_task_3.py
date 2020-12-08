import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

max_ = array[0]
min_ = array[0]

for i in array:
    if i > max_:
        max_ = i
    elif i < min_:
        min_ = i

max_index = array.index(max_)
min_index = array.index(min_)

for i in array:
    if min_index > max_index:
        min_index, max_index = max_index, min_index
print(f"Массив чисел: {array}")

summa = 0
for i in range(min_index + 1, max_index):
    summa += array[i]
print(f"Сумма чисел между минимальным и максимальным элементом = {summa}")