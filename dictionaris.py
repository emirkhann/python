# word - слова 

# dict
# словарь - изменяемый, итерируемый тип данных. Вместо индекса имеет ключи. Состоит из пар - ключ: значение 

# Ключи могут только неизменяемыми типами данных и должны быть уникальными 

# значениями могут быть любые типы данных

# литералы - (1)

passport = {'name': 'Lohh', 'last_name': 'baby', 'age': 25, 'gender': 'f'}

# print(passport['name'])
# passport['last_name']
# passport['age']
# passport['gender']
# passport['license'] # KeyError

# passport['licence'] = 'Can drive B'
# # passport['licence'] = # Can drive B
# print(passport)


""" созданеие словаря """
# dict_ - {1: 10}

# dict_2 = dict(name='baby', age=23)
# print(dict_2)

# dict_3 = dict((('name', 'baby'), ('age')))

# dict_4 = dict.fromkeys(['a', 'b'], 10)
# print(dict_4)


# human = {
#     'name'; 'bakai', 
#     'age': '21',
#     'friends': ['david', 'archi'],
#     'name': 'bakyt'
# }
# print(human)


# dict_5 = {
#     'name': 'archi',
#     [1, 2, 3]: 'ERROR'
# }



""" продолжение """

""" получеие значений из словаря """
car = {
    'marka': 'lexus', 
    'model': 'lx', 
    'color': 'black',
    'volume': 5.0,
    'year': 2021,
    
}
# print(car['marka']) # lexus
# print(car['kuzov']) # KeyError

# print(car.get('marka',)) # lexus
# print(car.get('kuzov')) # None
# print(car.get('kuzov', 'Такого ключа нет!')) # Такого ключа нет!

# print(car.setdefault('year')) 
# print(car.setdefault('kuzov')) 
# print(car)

""" добавлене данных в словарь """
house = {
    'color': 'white',
    'category': 'elit',
    'rooms': 4,
    'warmnes': True
}
# house =['area'] = '30x40'
# # print(house)

# house.update({'floor':} 3)
# print(house)

# house.update([['square', '12-mkr']])
# print(house)


# house.setdefault('pool', False)
# print(house)

# house['color'] = 'black'
# print(house)

""" удалееие данных из словаря """

# movie = {
#     'title': 'вторая жизнь Уве',
#     'country': 'USA',
#     'year': 2015,
#     'genre': ['comedy', 'dream']
# }
# deleted_key = movie.pop('country')
# print(movie)
# print(deleted_key)


# deleted_pair = movie.popitem()
# print(deleted_pair)
# print(movie)


# del movie['title']
# print(movie)

# movie.clear()
# print(movie)

""" итерация по словарям """


# """ перебор словаря """
# game = {
#     'title': 'fifa',
#     'year': 2015,
#     'author': 'ckala',
#     'category': 'RPG'
# }
# del key in game:
# print(key) 

# for key in game:
#     print(game[key])

# print(game.values()) # - .values() возвращает список значений словаря в виде dict_keys
# for value in game.values():
#     print(value)

# list(game.values())[1] 

# print(game.keys()) # .keys() возвращает список ключей в виде dict_keys

# print(game.items()) # - .items возвращает пару ключ-значений в виде списка из кортежей с типом dict_items

# a = 5
# b = 10

# a, b = 5, 10 

# key, value = ('titel', 'GTA')

# for key, value in game.items():
#     print(f'ключ{key},значение {value}')

# human = {
#     'name': 'asyla',
#     'age': '21',
#     'gender': 'f',
#     'friends': ['melis', 'khan']

# }
# human2 = human.copy()
# print(human)
# print(human2)

# human2['friends'].append('bema')
# human['gender'] = 'm'
# print(human2['friends'] is human['friends'])
# print(human2)
# print(human['friends']) 


# from copy import deepcopy
# human3 = deepcopy(human)
# print(human3)


# person = {
#     'name': 'nurlan',
#     'age': 39,
#     'passport': {
#         'id': 123456789,
#         'natyonaly': 'kyrgyz'
#     },
#     'drive_licence': {
#         'category': 'a',
#         'year': 2011
#     }
# }

# print(person['passport']['natyonaly'])



# human = {
#     'name': 'bakai', 
#     'age': 21,
#     'friends': ['david', 'archi'],
# }
# print('age')

# car = {
#     'marka': 'lexus', 
#     'model': 'lx', 
#     'color': 'black',
#     'volume': 5.0,
#     'year': 2021,
    
# }
# print(car['marka']) # lexus

# hashtags = ('#makers#bootcamp#программирование#it#курсы')
# print(hashtags)

a = range(10, 1, -1)
for i in a:
    print(i)









