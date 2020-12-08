SIZE = [0] * 8

MIN_ITEM_I = 2
MAX_ITEM_I = 100

MIN_ITEM_J = 2
MAX_ITEM_J = 10

for i in range(MIN_ITEM_I, MAX_ITEM_I):
    for j in range(MIN_ITEM_J, MAX_ITEM_J):
        if i % j == 0:
            SIZE[j - 2] += 1

i = 0
while i < len(SIZE):
    print(f"{i + 2} - {SIZE[i]}")
    i += 1
