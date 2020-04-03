    # Инициализация (генераторы)
list_temp = []      # пустой список
print(type(list_temp))
list_temp = [1.2, 123, 'Volvo', [1,2,3]]
print(list_temp)
# пройдем по элементам списка (функция el)
for el in list_temp:
    print(el, type(el))

# list - строка разбивается на элементы, где каждый элемент представляет собой элемент списка
list_str = list('Volvo')
print(list_str)

    # Обращение к элементам списка, подсписки
for i in range(len(list_temp)):
    print(i,':', list_temp[i])
# Срезы
for i in range(len(list_temp)):
    print(i,':', list_temp[i:])     # будет сначала весь список, потом отрезается первый, второй, третий (до i-1)
for i in range(len(list_temp)):
    print(i,':', list_temp[:i])     # будет сначала пустой список, потом добавится первый, второй... (до i-1)

    # Функции со списками
print(len(list_temp))

    # Операции со списками
print(list_temp + list_str)
print(list_temp*2)

    # Методы
# append - метод для добавления в конец
integer_list = []
for i in range(5):
    integer_list.append(i)
print(integer_list)
integer_list.append(0)
print(integer_list)

# remove - метод удаления элемента из списка (удаляет певый элемент по вхождению в список. Например, если 2 нуля, то удалит первый 0)
integer_list.remove(0)
print(integer_list)
# удаление элемента по индексу
del integer_list[4]
print(integer_list)

# reverse - элементы списка в обратном порядке
integer_list.reverse()
print(integer_list)

# sort - сортировка
integer_list = [2,9,4,1,3,7]
integer_list.sort()
print(integer_list)

# insert - вставка элемента в список
integer_list.insert(2,'Volvo')
print(integer_list)

    # Обработка списков (map, filter, reduce)
# map - это функция, которая применяется к каждому элементу списка
integer_list = [2,9,4,1,3,7]
new_integer_list = list(map(lambda x: x**2, integer_list))
'''
Есть некоторый список (integer_list). Создаем новый список (new_integer_list), присваиваем ему тип список (list), потом
применяем к нему функцию map. У функции map два параметра: функция и к чему эта функция применяется.
Функция lambda : к каждому элементу (х) списка integer_list применяем возведение (х) в квадрат (х**2).
'''
print(new_integer_list)

# filter - это функция фильтрации списка по некоторому условию
new_integer_list = list(filter(lambda x: x<5, integer_list))
print(new_integer_list)

# reduce - применяется ко всем элементам списка и возвращает какой-то один элемент (например: сумма списка, произведение списка)
from functools import reduce    # добавляем функцию reduce (подробности про импорт модулей позже)
integer_list = [1,2,3,4]
sum = reduce(lambda x,y: x+y, integer_list)
'''
lambda от двух переменных (х и у). Х - это то, что было. Потом прибавляем следующий элемент (у). Т.е. 1+2=3. 
Далее 3 становится х-ом. Далее 3+3 и т.д.
'''
print(sum)

proizv = reduce(lambda x,y: x*y, integer_list)
print(proizv)
