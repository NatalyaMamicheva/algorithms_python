import timeit
import cProfile

# С использованием «Решета Эратосфена»

b = []
n = int(input("Вывод простых чисел до числа ... "))


def eratosfen(n):
    a = [0] * n
    for i in range(n):
        a[i] = i

    a[1] = 0

    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    del a
    return b


print(eratosfen(n))

for i in b:
    index_ = b[(int(input("Введите месторасположение числа в `Решете Эратосфена`:  "))) - 1]
    print(f"Это число {index_}")
    break

print(timeit.timeit('eratosfen(24)', number=100, globals=globals()))  # 0.001624300000000467
print(timeit.timeit('eratosfen(35)', number=100, globals=globals()))  # 0.0022869000000005357
print(timeit.timeit('eratosfen(44)', number=100, globals=globals()))  # 0.001496800000000853

cProfile.run('eratosfen(24)')

"""
        13 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 main.py:8(eratosfen)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        9    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""

cProfile.run('eratosfen(35)')

"""

         15 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 main.py:8(eratosfen)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       11    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


"""

cProfile.run('eratosfen(44)')

"""
        18 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 main.py:8(eratosfen)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       14    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""

# Без использования «Решета Эратосфена»

n = int(input("Вывод простых чисел до числа ... "))
lst = []


def my_func(n):
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst


print(my_func(n))

for i in lst:
    index_ = lst[(int(input("Введите месторасположение числа:  "))) - 1]
    print(f"Это число {index_}")
    break

print(timeit.timeit('my_func(24)', number=100, globals=globals()))  # 0.0011603999999998393
print(timeit.timeit('my_func(35)', number=100, globals=globals()))  # 0.0017457000000007383
print(timeit.timeit('my_func(44)', number=100, globals=globals()))  # 0.0025192000000000547

cProfile.run('my_func(24)')

"""
13 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 main.py:5(my_func)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        9    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


"""

cProfile.run('my_func(35)')

"""
         15 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 main.py:5(my_func)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       11    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""

cProfile.run('my_func(44)')

"""
         18 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 main.py:5(my_func)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       14    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""