""" условные вырожения (if-elif-else)"""

# bool() - неизменяемый тип данных, который имеет всего 2 значения: true, False

# 10 > 2 # true
# > - большк
# < - меньше 
# <= - меньше или равно
                    #    -> bool()
# >= - больше или ровно
# != - неравенство 
# == - равенство

# print(25 == 23) # false
# print(0.25 == 25) # true
# print("apple > 2") # Error

# print(bool(0)) # false
# print(bool(1)) # true

# print(bool(2)) # true
# print(bool(-5)) # true


# print(bool('it')) # true
# print(bool('')) # false

" все работает как, есть тока, или нет"

# bool([]) # false
# bool({}) # false
# bool(set()) # false
# bool(None()) # false

""" if """

# num = 10
# print(num)

# num = 15
# if num > 10: 
#     print('число больше 10')

""" if else """

# num = 26
# if num > 20:
#     print("num больше 20")
# else:
#     print("num не больше 20")

# tempreture = 40
# if tempreture < 20:
#     print('холодно')
# else:
#     if tempreture > 30:
#         print('тепло')
#     else:
#             if tempreture < 35:
#                 print('жарко')

# temperature = 40 
# if temperature < 27:
#     print('холодно') 
# elif temperature < 30: 
#     print('тепло')
# elif temperature > 35:
#     print('жарко')
# else: 
#     print('Неверная цифра') 


# num2 = 35
# if num2 < 20:
#     print('num2 < 20')
# elif num2 > 10:
#     print('num2 > 10')
      
# mark = int(input('Введите оценку от 1 до 5 '))
# msg = ''
# if mark == 5:
#     msg = 'ты молодец!'
# elif mark == 4:
#     msg = 'хорошо'
# elif mark <= 3:
#     msg = 'подтяни предмет'
# print(msg)

# mark = input('Введите оценку от 1 до 5 ')

# if mark isdigit():
#     mark = int(mark)
#     msg = ''
#     if mark == 5:
#     msg = 'ты молодец!'
#      elif mark == 4:
#     msg = 'хорошо'
#      elif mark <= 3:
#     msg = 'подтяни предмет'
# print(msg) 


""" and or not """
# age = 25
# if age > 10 and age < 20:
#     print('входите')
# else:
#     print('входа нет')

False # false
True # true
False and False # false
True and True # true
True and False # false

False or False # false
True or True # true
False or True # True
True or False # true

not True # false
not False # true

(False or True) and (False and False) # false

""" is, ==, in """
# a = 10
# print(a is 10)

# a = 300
# b = 300
# print(id(a))
# print(id(b))
# print(a is b) # false
# print(a == b) # true

# string = 'hello world'
# print('world' in string) # True

# """ тернарый оператор """
# msg = input('введите сообзение')
# if len(msg) > 10:
#     print('собщение длиннее 10')
# else:
#     print('сообение короче 10')

# msg = input('введите сообщение ')
# res = 'сообщение длиннее 10' if len(msg) > 10 else 'сообщение короче 10'
# print(res)

# if условие:
#     действие 1
# else:
#     действие 2

# действие 1 if условие else действие 2

""" elif """
# if условие1:
#     действие1
# elif условие2:
#     действие2
# else:
#     действие3

#------------------------
# name = "John"
# age = 23
# if name == "John" and age == 23:
#     print("Your name is John, and you are also 23 years old.")

# x = 2
# if x == 2:
#     print("x equals two!")
# else:
#     print("x does not equal to two.")



num = 15
if num > 10: 
    print('число больше 10')

""" синтаксис """

# if <условие 1>: 
#     <выражение 1> 
# elif <условие 2>: 
#     <выражение 2> 

# … 

# elif <условие n>: 
#     <выражение n> 
# else: 
#     <выражение n + 1> 



