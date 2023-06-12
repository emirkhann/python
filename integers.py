# int() - целочисленный тип данных (1, 2, 5, 7,)
int_num = 20

# float() - числа с плавающей/числа с дробной частью (5.1, ~2.3, 10.004)
float_num = 10.02

""" операторы для работы с числами / арифметическими операторами """
num_1 = 10
num_2 = 20

num_1 + num_2 # сложение (15)
num_1 - num_2 # вычитание (5)
num_1 * num_2 # умножение (50)
num_1 / num_2 # деление (2.0) -> float
num_1 // num_2 # деление (2) -> int
num_1 ** num_2 # возведение в степень (100000)
num_1 % 3 # выделение остатка от деления (1) -> int


# проблема float
# result = 0.1 + 0.1
# print(result)

# from decimal import Decimal
# decimal_1 = Decimal("0.1")
# decimal_1 = Decimal("0.1")
# decimal_1 = Decimal("0.1")

# print(decimal_1 + decimal_2 + decimal_3)

even =2
add = 5

# print(even % 2)
# print(odd % 2)

""" функция для работы """
# print(abs(5)) #5
# print(abs(-6)) #6
# print(abs(-2.5)) #2.5
# # abs(x) -  возвращает модуль переданного числа/число без учета знака


# print(pow(2, 3)) # 2 ** 3 = 8
# print(pow(2, 3, 4)) # 2 ** 3 % = 8
# # pow(x, y, [2])


# print(divmod(1, 2)) # 1 // 2, 1 % -> (0,1)

round(5.2) # 5
round(5.6) # 6
round(5.5) # 6 в этом случае лкруглит в четную сторону
round(3.1456373465, 2) # 3.15
# round(x, [y]) - округление числа "х" до целого, если указан "у", то оставит после точки "у" цифр


# num_3 = 10
# print(float(num_3))
# num_4 = 10.4
# print(int(num_4))

immutable_num = 20
immutable_num + 50
print(immutable_num) #20

immutable_num = 20
immutable_num = 50
print(immutable_num) #20

counter = 0
counter += 1 # counter = counter + 1
print(counter) # 1
# += - инкремент 
# -= - дикреент


import math

# math.sqrt(25) # 5
# math.factorial(5) # 120
# # 1 * 2 * 3 * 4 * 5
# math.pi # 3.14...

"""
Дана переменная t с целочисленным значением веса муки в 255 тонн, 
найдите сколько это будет в граммах, килограммах, центнерах, 
распечатайте результат в терминале

"""
t = 255
g = ...
kg = ...
ts = ...
print(g, kg, ts)



