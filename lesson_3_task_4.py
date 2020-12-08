import random

SIZE = 5
MIN_ITEM = 0
MAX_ITEM = 30
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

a = []
for index, i in enumerate(array):
    if i % 2 == 0:
        a.append(index)
print(f"Индексы четных чисел массива: {a}")