while True:
    first = int(input("Введите первое число: "))
    second = int(input("Введите второе число: "))
    symbol = input("Введите знак операции (* / + -) 0-для выхода из калькулятора: ")
    if symbol == "0":
        print("Выход из калькулятора")
        break
    if symbol != "0" and symbol != "-" and symbol != "+" and symbol != "*" and symbol != "/":
        print("Ошибка ввода знака операции!")
    if symbol == "+":
        print(f"Операция {first} {symbol} {second} = {first + second}")
    if symbol == "-":
        print(f"Операция {first} {symbol} {second} = {first - second}")
    if symbol == "*":
        print(f"Операция {first} {symbol} {second} = {first * second}")
    if symbol == "/":
        try:
            print(f"Операция {first} {symbol} {second} = {first / second}")
        except ZeroDivisionError:
            print("Ошибка! На 0 делить нельзя!")