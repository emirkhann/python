# id(obj) - принимает объект и возвращает его уникальный номер.

# str1 = 'Hello world'
# print(id(str1))
# str2 = 'Another string'
# print(id(str2))
# str3 = str1
# print(id(str1))
# print(id(str3))


# str3 = str1.swapcase()
# print(id(str1))
# print(id(str3))

# list1 = list('hello world')
# print(id(list1))
# list2 = list('Another list')
# print(id(list2))

# list3 = [1, 2, 3]
# print(id(list3))
# list3.append(4)
# print(id(list3))

# list_of_nums = [1, 2, 3, 4]
# list_of_nums.append(1)
# list_of_nums.append(2)
# list_of_nums.append(3)
# list_of_nums.append(4) #нельзя так делать. 

# DRY - Don't Repeat Yourself

# list_of_nums = [1, 2, 3, 4]
# for num in range(4):
#     list_of_nums.append(num)
# print(list_of_nums)


# while условие == True


# from string import ascii_lowercase


# counter = 0
# alphabet = ''
# while counter < len(ascii_lowercase):
#     alphabet += ascii_lowercase(counter)
#     counter += 1
#     # counter = counter +1