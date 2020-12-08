import random

SIZE = 5
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f"Массив до перемены чисел: {array}")

max_ = array[0]
min_ = array[0]

for i in array:
    if i > max_:
        max_ = i
    elif i < min_:
        min_ = i

max_index = array.index(max_)
min_index = array.index(min_)
array[max_index], array[min_index], = array[min_index], array[max_index]
print(f"Массив после перемены чисел: {array}")