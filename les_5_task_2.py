from _collections import deque

x = input('Введите 1-е шестнадцатиричное число: ').upper()
y = input('Введите 2-е шестнадцатиричное число: ').upper()


def sixteen(x, y):
    numbers = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    additional_number = 0

    if len(y) > len(x):
        x, y = deque(y), deque(x)

    else:
        x, y = deque(x), deque(y)

    while x:
        if y:
            res = numbers[x.pop()] + numbers[y.pop()] + additional_number
        else:
            res = numbers[x.pop()] + additional_number
        additional_number = False

        if res < 16:
            result.appendleft(numbers[res])

        else:
            result.appendleft(numbers[res - 16])
            additional_number = True

    if additional_number == True:
        result.appendleft("1")

    return list(result)


print(f"{x} + {y} = {''.join(sixteen(x, y))}")
