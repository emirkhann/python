
""" методы set """

# class_js = {'aktan', 'beka', 'tima', 'nikita'}
# class_py = {'malik', 'aigul', 'tima', 'aktan'}

# inter = class_js.intersection(class_py)  
# print(class_js & class_py)
# print(inter)

# diff = class_js.difference(class_py) 
# print(diff)

# print(class_js.union(class_py))
# print(class_js | class_py)

# fruits = {'banana', 'kiwi', 'apple', 'tangerin'}
# vegetabels = {'carrot', 'patoto', 'tomato'}

# fruits.intersection_update(vegetabels)
# print(fruits)

# a = {1, 2, ['a', 'b']} # TypeError

# my_unique_set = {1, 0, 'string', True, False, (1, 2)}
# print(my_unique_set)


""" Кортеж """

# Tuple()

# кортеж - неизменяемый, итерируемый, индексируемый, упорядоченный тип данных 

# литералы - ()

# tuple = (1, 2, 3, 4, [1, 2])
# tuple2 = 1, 2, 3, 4, [1, 2]
# print(type(tuple))
# print(type(tuple2))


# t1 = ('1 element', )
# print(type(t1))
# t2 = '1 element',
# print(type(t2))

# a, b, c = (1, 2, 3) # распаковка 

# звездочный синтаксис
# tuple_of_nums = tuple(range(5))
# print(tuple_of_nums)
# print(*tuple_of_nums)
# print(0, 1, 2, 3, 4)

# tuple_of_nums = (0, 1, 2, 3)
# v1, *v2, v3 = tuple_of_nums
# print(v1)
# print(v3)
# print(v2)

# human = ['heart', 'hands', 'eyes']
# human[1] = 'wheels'
# print(human)


# l1 = [1, 2, 3]
# l2 = (1, 2, 3)
# print(l1.__sizeof__())
# print(l2.__sizeof__())

# s1 = {'string', 'string2', {1, 2, 3}}
# print(hash('string'))
# {-830021360973310514: 'string'}


# t1 = (1, 2, 3, 3, 3)
# print(t1.count(3))
# print(t1.index(2))

tuple = (1, 2, 3)
tuple2 = [4, 5, 6]
new_tuple = tuple + tuple2







