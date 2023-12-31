""" list, loops: for, while """

# list()
# list() (списки) - коллекция элементов. Изменемый тип данных, 
# упорядоченный, индесируемый, итерируемый. используется для хранения набора элемента

# элемнтами списка могут быть любые типы данных 

# list_with_all_data_types = [1, 'string', True, False, None, [1, 2], {'a': 10}, {1, 2}, {'a' 1, 'b'}]
# print(list_with_all_data_types)

# list_of_numbers = [1, 2, 3, 4, 5, [6, 7]] 
# list_of_numbers = [0] # 1
# list_of_numbers = [1] # 2
# list_of_numbers = [2] # 3
# list_of_numbers = [3] # 4
# list_of_numbers = [4] # 5
# list_of_numbers = [5] # [6, 7]
# list_of_numbers = [5][1] # 7

# list_of_numbers[1:3:] # [2, 3]

""" методы списков """

" 1) добавление элементов в список "
# a = [1, 2, 3]
# print('до', a)
# a.append(4) # добавляет элемент в конец списка
# print('после', a)

# b = '123'
# b + '4'
# print(b)

# a.insert(0, 'baby')
# print(a)
# a.insetr(index, element) # вставляет элемент на указанный индекс

# a.insert(len(a) '4') 
# print(a)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
# list1.extend(list2)
# print(list1) # [1, 2, 3, 4, 5. 6]

# baby = list1 + list2 
# print(baby)

" замена элементов "
# letters = ['a', 'b', 'c', 'g']
# letters[3] = 'd'
# print(letters)
# print (letters)

" удаление элементов "
# letters = ['a', 'b', 'c', 'g']
# letters.pop(2)
# print(letters)

# letters = ['a', 'b', 'c', 'g']
# deleted_el = letters.pop(2)
# print(deleted_el) 


letters = ['a', 'a', 'b', 'c', 'g']
# letters.remove('a')
# print(letters)


# letters.clear()
# print(letters)

# del letters[1]
# print(letters) # ['a', 'b', 'c', 'd']


""" сортировка и копирование списка """

# nums = [1, 2, 3, 4,]
# nums_copy = nums.copy()
# nums_copy2 = nums[:] 


# nums = [1, 2, 3, 4,]
# nums2 = nums
# nums2.append(5)
# print(nums2) 
# print(nums)
# print(nums is nums2)


# nums_list = [8, 6, 10, 5]
# # nums_list.sort()
# nums_list.sort(revers=True)
# print(nums_list)


# names = ['kolya', 'mayram', 'alexande', 'ivan']
# names.sort()
# names.sort(key=len)
# print(names)

# names = ['kolya', 'mayram', 'alexande', 'ivan']
# new_names = sorted(names)
# print(new_names)

# names.reversed

""" циклы """

# цикл - многократное выполнение определенного участка кода 

# иетрация - повтороное какого-либо действия

# итерируемый объект - объект, к котороиу можно применить цикл 

# nums_list = [1, 2, 3, 4, 5]
# print(nums_list[0])
# print(nums_list[1])
# print(nums_list[2])
# print(nums_list[3])
# print(nums_list[4])

# 1) for 
# nums_list = [1, 2, 3, 4, 5]
# for num in nums_list:
    # print(num)

# for - цикл который перебирает каждый элемент в итерируемом объекте и работает до тех пор, пока эти элементы не закончатся 
# for элемент 

# string = 'hello world' 
# for letter in string:
#     print(letter) 


# nums = range(10)
# for num in nums:
#     print(num)

nums = range(1, 21)
new_nums = []
for num in nums:
    if num % 2 == 0:
        new_nums.append(num)

print(new_nums)



"""продолжеие """


# list_of_lists = [[1, 2, 3], ['big', 'gig', 'fufa'], [4, 5, 6,]]
# for list_ in list_of_lists:
#     for element in list_:
#          print(element) 

# for elemet in list_of_lists[-1]:
#     print(element) 


# data_types = [int, bool, str, list, tuple, dict, set, None]
# итерируемые : list, str, tuple, dict, set
# неитерируемые : bool, int, None

# iter_objs = []
# non_iter_objs = []
# for type_ in data_types:
#     if '__iter__' in dir(type_):
#         iter_objs.append(type_)
#     else:
#         non_iter_objs.append(type_)

# print('итерируемые', iter_objs)
# print('неитерируемые', non_iter_objs)


# while условие
# while - цикл, который работает до тех пор, пока условие возвращает True

# counter = 0
# while counter < 5:
#     print(counter)
#     print('hello')
#     counter += 1 


# while True: # бескрненчный цикл 
#     print(...)

# CTRL + c - остановка бесконечного цикла 


# msg = input('Введите сообщение или стоп ')
# while msg != 'stop':
#     print(f'ваше сообщение\n[{msg}')
#     msg = input('введите сообщение или стоп ') 


# while True:
#     msg = input('введите сообщение или стоп ')
#     if msg == 'stop':
#         print('цикл оставлен')
#         break
#     print(f'ваше сообщение\n{msg}')

# break - оператор для остановки цикла
# continue - начинает цикл заново, пропуская остальное тело цикла

# a = 'Ainininningugig'
# b = ''
# for letters in a:
#     if letters == 'i':
#         continue
#     b += letters
# print(b)

# убирает буквы

""" else в циклах """
# nums = range(0, 101, 2)
# result = 0
# for num in nums:
#     if num = 51:
#         break
#     result += num
# else:
#     print(result)

# list_of_names = ['serega', 'dimon', 'baby', 'vavo']
# guests_q = 10
# while guests_q > 0:
#     name_of_guests = input('введи имя ')
#     if name_of_guests in list_of_names:
#         print('вход закрыт ')
#         break
#     guests_q -= 1
# else:
#     print('начинаем веренку!!!!!!!')


# list_of_nums = [1, 2, 3, 4]
# for num in list_of_nums:
#     print(num)

# list_of_nums = [1, 2, 3, 4]
# conter = 0
# while conter != len(list_of_nums):
#     print(list_of_nums[conter])
#     conter += 1

# nums_list = [1, 2, 3, 4, 5]
# print(nums_list[0])
# print(nums_list[1])
# print(nums_list[2])
# print(nums_list[3])
# print(nums_list[4])

list_ = [
    'Honda', 'kawasaki'
]
for baby in list_:
    for element in list_:
        print(element)














