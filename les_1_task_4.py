#Определить, является ли год, который ввел пользователь, високосным или не високосным
year = int(input("Введите год (формат ГГГГ):  "))

if year % 100 == 0:
    print("Не високосный год!")
elif year % 4 != 0:
    if year % 400 == 0:
        print("Високосный год!")
    else:
        print("Не високосный год!")
else:
    print("Високосный год!")