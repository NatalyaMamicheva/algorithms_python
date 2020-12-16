import timeit
import cProfile

# Урок 2 задание 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

# 1 вариант кода

def first(num, n):
    if (n == 0):
        return 1
    else:
        return (num * first(num, n - 1))


print(timeit.timeit('first(-0.5, 2)', number=100, globals=globals()))  # 4.059999999999481e-05
print(timeit.timeit('first(-0.5, 4)', number=100, globals=globals()))  # 5.779999999999674e-05
print(timeit.timeit('first(-0.5, 8)', number=100, globals=globals()))  # 0.00010170000000000318

cProfile.run('first(-0.5, 2)')
"""
         6 function calls (4 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
      3/1    0.000    0.000    0.000    0.000 main.py:5(first)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""

cProfile.run('first(-0.5, 4)')
"""
    8 function calls (4 primitive calls) in 0.000 seconds

    Ordered by: standard name

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
      5/1    0.000    0.000    0.000    0.000 main.py:5(first)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""

cProfile.run('first(-0.5, 8)')
"""
         12 function calls (4 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
      9/1    0.000    0.000    0.000    0.000 main.py:5(first)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


# 2 вариант кода
def second(n):
    num = 1
    sum_ = 1
    for i in range(n):
        num /= -2
        sum_ = num
    return sum_


print(timeit.timeit('second(2)', number=100, globals=globals()))  # 6.260000000000293e-05
print(timeit.timeit('second(4)', number=100, globals=globals()))  # 0.00010420000000000568
print(timeit.timeit('second(8)', number=100, globals=globals()))  # 0.00012419999999999792

cProfile.run('second(2)')
"""          4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 main.py:3(second)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

cProfile.run('second(4)')
"""         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 main.py:3(second)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""

cProfile.run('second(8)')
"""        4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 main.py:3(second)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


# 3 вариант кода
def third(n):
    i = 0
    num = 1
    sum_ = 1
    while i < n:
        num /= -2
        sum_ = num
        i += 1
        return sum_


print(timeit.timeit('third(2)', number=100, globals=globals()))  # 3.650000000000181e-05
print(timeit.timeit('third(4)', number=100, globals=globals()))  # 5.8500000000002994e-05
print(timeit.timeit('third(8)', number=100, globals=globals()))  # 0.00010249999999999843

cProfile.run('third(2)')
"""       4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 main.py:4(third)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

cProfile.run('third(4)')
"""         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 main.py:4(third)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

cProfile.run('third(8)')
"""         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 main.py:4(third)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# ВЫВОД: Сложность и время работы алгоритмов приблизительно одинаковые.