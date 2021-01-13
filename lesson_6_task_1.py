import sys

n = 2


def first(num, n):
    if (n == 0):
        return 1
    else:
        return num * first(num, n - 1)


num = -0.5
a = []
a.append(num)
a.append(n)
print(sys.getsizeof(a))  # Python 3.8.5, разрядность ОС 64,  результат 88


def second(n):
    num = 1
    sum_ = 1
    a = []
    a.append(num)
    a.append(sum_)
    a.append(n)
    for i in range(n):
        num /= -2
        sum_ = num
        a.append(i)
    print(sys.getsizeof(a))


second(n)  # Python 3.8.5, разрядность ОС 64,  результат 120


def third(n):
    i = 0
    num = 1
    sum_ = None
    a = []
    a.append(num)
    a.append(sum_)
    a.append(n)
    a.append(i)
    while i < n:
        num /= -2
        sum_ = num
        i += 1
    print(sys.getsizeof(a))


third(n)  # Python 3.8.5, разрядность ОС 64,  результат 88

# Коды под номерами 1 и 3 используют меньшее количество памяти, поэтому для ее экономии лучше использовать их.