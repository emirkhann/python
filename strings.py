"""strings (строка) """

#str()

#string - неизменяемый, упорядоченный, индексируемый, итерируемый тип данных

string = "hello"

string = 'hello'

doc_string = """ Строка документации - используется для описание кода в нескольких строк """
doc_string = ''' строка документации '''

# string3 = 'hello, I'm student Error

string4 = "hello, I'm student"
string5 = 'hello I\'m student' # экранирование 

str1 = 'hello'
str2 = 'world'
# (print(str1 + str2) # helloworld
# конкатинация - склеивание / сложение строк 

frog = 'quak'
# print(frog * 3) # quakquakquak

"""функция и методы строк """

greeting = 'Hello everyone'

# print(len(greeting)) # 14
# len(x) - подсчитывает кол-во строк

# print(dir(greeting))
# dir(x) - возвращает список методов переданного обьекта 


# метод - функция, принадлежащая определенному типу данных и может быть вызвана только через объект

# my_str = 'Hello world'

# print(my_str.lower())
# print(my_str.upper())
# print(my_str.split()) # str.split() --> возвращает список из строк по делителю, 
# если не передать делитель - по порбелу


# my_str2 = '                     Hello world                         '

# my_str2.title() #Hello world
# my_str2.capitalize() # Hello world 
# my_str2.count('l') # 3
# my_str2.replace('o', 'm') #hellm wrmld 
# print(my_str2.strip()) # удалает пробелы с двух сторон
# my_str2.lstrip() # слева 
# my_str2.rstrip() # справа 


# string = 'Some sring with 5 words'
# string.isalpha() # False
# string.isdigit() # False
# string.isalnum() # False
# string.startswith('S') # true
# string.endswith('ds') # true

# #in
# 'with' in string # true

""" Форматирование/интрпритация строк """


# name = input('name;')
# party = input('party;')


# inv1 = 'Дорогой %s, приглашаем тебя на свадьбу' % name
# print(inv1)
# inv2 = 'Дорогой {a1} , пригалаем тебя на {b2}'. format(a1=name, b2=party)
# inv3 = f'Дорогой {name} , пригалаем тебя на {party}'. format(a1=name, b2=party)
# print(inv3)



""" индексы и срезы  """

# str10 = 'makers'
# str10 [0] # 'm'
# индексы - порядковый номер элемента в строке/списке/ кортеже. В программирование индексация начинаеся с нуля 
# 'hello'
# 01234
# -5-4-3-2-1

# string2 = 'house'
# print(string2[-1]) # 'e'

# string3 = 'hello world'
# start =  0 
# stop = 5
# step = 1
# print(string3[start:stop:step]) 
# print(string3[::-1])
# print(string3[::])

# """ экраниерование строк """
# print('hello\nworld')
# """
# hello
# world
# """

# print('hello\n\tworld')
# """
# hello
#    world
# """

# path = "C;\\users\\new\\tanks"
# print(path)

# print(('hello world' + '\n') * 3)
# print(('hello world' + '\n') * 3)

# string = 'hello world'
# reversed(string)
# print(string)

# str = "hello"
# stringlength=len(str) 
# slicedString=str[stringlength::-1] 
# print (slicedString)

# str = "pythonist" 
# reversedstring=''.join(reversed(str))
# print(reversedstring)

# string1 = "hello"
# string2 = "world"
# print(string1 + ' ' + string2)

string = 'hey'
# print(string + string + string + string)

# string = 'hello'
# reversed(string)
# print(string)

# str = "baby"
# reversedstring=''.join(reversed(str))
# print(reversedstring)

# string = 'The quick brown fox jumps over the lazy dog'
# string1 = string.replace("o", "*")
# print(string1)

" создание новой переменной и его сохранение "

string = input()
wordLength = len(string)
print(string[wordLength-1]+string[1:wordLength-1]+string[wordLength-wordLength])










