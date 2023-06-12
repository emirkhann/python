""" functions - функции """

# num1 = 10
# print(num1 + 20 / 5)

# num2 = 20
# print(num2 + 20 / 5)

# num3 = 30
# print(num3 + 20 / 5)

def add_and_divide(x):
    print(x + 20 / 5)

# add_and_divide(10)
# add_and_divide(20)
# add_and_divide(30)

# функция - именнованный блок кода, который принимает какие-либо значения, 
# совершает над ними определенные действия и возвращает результат этих действий

# def greet():
#     print('hello world')

# greet()
# greet(10)

# def add(a, b):
#     print(a + b)

# # add(20, 40)

# def add(num, num2):
#     result = num + num2
#     return result

# print(add(50, 100))
# a = add(10, 10)
# print(a)
# b = add(20, 40)
# print(b)

# def func():
#     print('this is func')
#     return

# def имя_функции(параметры):
#     тело функции

# имя_функции(аргумент)


# параметры - локальные переменные для функции, объявляются при создании функции

# аргумент - это значение для функции при вызове. 
# аргумент может быть столько сколько параметров у функции

# return - ключевое слово, которое служит для возвращения результатов выполения функции.
# Является точкой выхода из функции 

# def big_baby(b):
#     counter = 0
#     for i in b:
#         counter += i
#     return counter
    
# print(big_baby([1, 2, 3]))

# def nitroo_race(list_of_nums: list) -> int:
#     """ складывает все числа из списка """
#     counter = 0
#     for i in list_of_nums:
#         counter += i
#     return counter

# print(nitroo_race((1, 2, 3, 4)))

# print(pow(1, 2, 3))

# параметры бывают 2 типов: 
# 1) обязательный 
# 2) необязательный 

# def sub(x, y):
#     return x - y

# sub(1) # TypeError
# sub(1, 2) # -1

# def sub(x, y=10):
#     return x - y

# sub(20) # 10
# print(sub(50, 20))

# def wrong_params(x = 5, y):
#     return x + y
# SyntaxError

# def good_params(a, b, c, d, e=10, f=20):
#     pass

# аргументы бывают 2 типов:
# 1) именнованые 
# 2) позиционные

# pow(10, 20)
# pow(exp=20, base=10)

# def amogus_1(num1, num2, num3=20):
#     return num1 + num2 + num3

# print(amogus_1(10, 20, 30))
# amogus_1(num1=80, num2=10, num3=30)
# amogus_1(num1=30, 10, 20) # Error
# amogus_1(10, 20, num3=30) # ok

# print()

""" args, kwargs - arguments, keyword arguments """
# *args - кортеж позиционных аргументов 
# **kwargs - словарь позиционных аргументов

# def func(*args, **kwargs):
#     print(args, '<- args')
#     print(kwargs, '<-kwargs') 

# func()
# func(1, 2, 3)
# func(a=1, b=2, c=3)
# func(1, 2, 3, b=4, c=5, d=6)

# def sum_nums(*nums):
#     counter = 0
#     for num in nums:
#         try:
#             counter += num
#         except TypeError:
#             print(f'{num} не является числом')

#     return counter

# print(sum_nums(1, 2, 3, 'hello', 4))


# def idi_v_as(nums: list):
#     for num in nums:
#         return num + 10

# print(idi_v_as([1, 2, 3]))

# def get_names(**contacts):
#     for key, value in contacts.items():
#         print(f'номер {value} принадлежит {key}')
# get_names(beka=647858483, baby=5748394839)

# def add(b):
#     counter = 0
#     for i in b:
#         counter += i
#     return counter
    
# print(add([2, 10]))


# my_dict = {
#     'first': {'a': 1}, 'second': {'b': 2}}
# for a, b in list(my_dict.items()):
#     for z, x in list(b.items()):
#         my_dict[a] = x
# print(my_dict)





