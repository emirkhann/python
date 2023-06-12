""" try except - ошибки """


# ислючение - проблема в логике работы кода 
# ошибка - проблема с написанием кода/синтаксисе кода

# исключение можно выловить и обработать.
# ошибки нельзя


# a = 10
# b = 20
# print(c) 
NameError # исключение отсутствие имени

# 10 / 0
ZeroDivisionError # исключение при делении на ноль

# names = {'misha': 20, 'nur': 30}
# names = ['azamat']
KeyError # исключение ключа 

# list_ = [1, 2, 3]
# list_[5]
IndexError # индекс не входит в диапазон списка

# num = 10
# num + 'string'
TypeError # ошибка типов данных, когда тип объекта не подходит для операции 

# int(10) # ok
# int(10.10) # ok
# int('10') # ok
# int('string') 
# from math import sqrt
# sqrt(25)
# sqrt(-20)
ValueError # ошибка значения, когда тип объекта подходит под условие, но его значение - нет


# string = 'world'
# string.append('b')
AttributeError # отсутствие атрибута или метода у объекта 

# import mazh_module
ModuleNotFoundError
# from math import wrong_func
ImportError

# # ошибки 
# for i in range(10)
#     print(i)
SyntaxError # синтакическая ошибка 

# for i in range(10):
# print(10)
IndentationError # ошибка отступа 

# for i in range(10):
#       print(i)
TabError # ошибка табуляции(смешивание табов и пробелов)

# names = {
#     'viva': 40584029430580,
#     'beka': 23434930320494,
# }
# names['ring']
# print('hello')
# print(1 + 1)


# try except - конструкция для обработки исключений
# try:
#     names = {
#      'viva': 40584029430580,
#      'beka': 23434930320494,
#     }
#     names['chan']
# except:
#     print('нет такого имени')
# print('hello')
# print(1 + 1)

try:
    print('hello')
    10 / 0
    print('world')
except:
    print('что то пошло не так')
else:
    print('try работал без ошибок')
finally:
    print('я отработал в любом случае')

# nums = [1, 2, 3, 4]
# try:
#     a = nums[-1]
#     nums[10]
# except IndexError:
#     print('возникла ошибка')

# try:
#     print(c)
#     10 / 0
#     'string'.
# except (NameError, ZeroDivisionError):
#     print('нет такого имени или деление на ноль')
# except AttributeError:
#     print('нет такого атрибута')


# Exception
# try:
#     print(m)
# except Exception as error:
#     print(error)

# try:
#     код, который потенциально может вызвать исключение
# except:
#     блок кода, который сработает, если в try было вызвано исключение  
# else: 
#     выполняется если в try не было исключений 
# finally: 
#     выполняется в любом случае


# raise - ключевое слово для поднятия/вызова ошибок
# money = 0
# if money == 0:
#     raise ValueError('недостатчно средств на карте')

try:
    raise Exception('моя ошибка')
except Exception:
    print('ошибка обработана')
finally:
    print('программа завершена')

# try:
#     for i in range(10):
#         print(i)
# except SyntaxError:
#     print('неправильно написан код')

# contacts = {' Alfa': 3232, 'Biba': 4343, 'Gigant': 6565}
# try:
#     name = input('введите имя').title()
#     contacts[name]
# except KeyError:
#     print('нет такого имени')

# contacts = {' Alfa': 3232, 'Biba': 4343, 'Gigant': 6565}
# name = input("введите имя").title()
# if name not in contacts:
#     print('нет такого имени')
# else:
#     contacts[name]

# contacts = {' Alfa': 3232, 'Biba': 4343, 'Gigant': 6565}
# print(contacts.get('Nur', 'нет такого имени'))

# while True:
#     try:
#         num = int(input('введите число'))
#         print(num + 10)
#         if num == 0:
#             break
#     except ValueError:
#         print('введите число!')

# try - попытаться
#  except - исключение 


    

