""" comrehensions (генераторы) """

# list_ = [] # [1, 2, 3, 4, 5]
# for i in range(1, 6):
#     list_.append(1)
# print(list_)

"длинная строка"

# list_ = [i for i in range(1, 6)]
# print(list_)

"короткая строка"

"comprehensions - которткий способ записи циклов для создания коллекции"

# синтаксис_генератора = [выражение for выражение in итерируемый объект 

# 1) добавить список 10 чисел от 1 до 10


# nums = []
# for num in range(1, 10):
#     nums.append(num)
# print(nums)

# nums = [num for num in range(1, 10)]
# print(nums)

# 2) заисать в список числа в диапазоне до 6 , при этом каждому числу добавить +10

# nums = []
# for num in range(1, 6):
#     nums.append(num + 10)
# print(nums)

# nums_10 = [num + 10 for num in range(1, 6)]
# print(nums_10)

# 3) записать с список числа в диапазоне от 1 до 10, при этом только те, которые являются четными

# even_num = []
# for num in range(1, 10):
#     if num %2 == 0:
#         even_num.append
# print(even_num)

# even_num = [num for num in range(1, 10) if num %2 == 0]
# print(even_num)

"""синтаксис генератора с условием - выражение for выражение in итерируемый """

# 4) записать в список числа в диапазоне от 1 до 10, при этом к четным прибавлять по 10 , к нечетным по 200

# nums_200 = []
# for num in range(1, 10):
#     if num % 2 == 0:
#         nums_200.append(num + 10)
#     else:
#         nums_200.append(num + 200)

# print(nums_200)

# num_200 = []
# for num in range(1, 10):
#     num_200.append(num + 10) if num % 2 == 0 else num_200.append(num + 200)
# print(num_200)


# generator_num_200 = [num + 10 if num % 2 == 0 else num + 200 for num in range(1, 10)]
# print(generator_num_200)

# синтаксис генератора с двумя условиями = [тернарный оператор for выражение ]

# 4) записать в список в числа в случайном диапазоне, к четным прибавить только с теми числами, которые больше 5
import random
random_num = random.randrange(5, 20)
# baby = []
# for num in range(1, random_num):
#     if num > 5:
#         if num % 2 == 0:
#             baby.append(num + 10)
#         else:
#             baby.append(num + 200)
# print(baby)

# baby = [num + 10 if num % 2 == 0 else num + 200 for num in range(1, random_num) if num > 5]
# print(baby)

# nums = []
# for num in range(1, 10):
#     for a_num in range(10, 20):
#         nums.append(num + a_num)
# print(nums)

# nums = [num + a_num for num in range(1, 10) for a_num in range(10, 20)]
# print(nums)

""" dict comprehensions """
names = {
    'aktan': 22,
    'koka': 32,
    'baka': 31,
}
aged_names = {}
for key, value in names.items():
    aged_names.update({key: value + 1})
print(aged_names)


# aged_names = {key: value + 1 for key, value in names.items()}
# print(aged_names)

# range(1, 10) - итератор 

# generator = [*(num for num in range(1, 10))]
# # print(generator)
# for num in generator:
#     print(num)


# r = range(1, 6)
# for i in r:
#     print(i)
# for i in r:
#     print(i)
# for i in r:
#     print(i)


# генераторы - спец тип данных, которые одновременно создают значение и исчезают из памяти, когда эти значения заканчиваются 

# итераторы - те типы данных, по которым можно пройтись 


names = {
    'temir': 71,
    'semetei': 90,
    'gig': 45,
}

print(dict('temir'))