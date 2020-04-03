    # Инициализация словарей
# dict - тип словарь
# Словари инициализируются фигурными скобками {}
dict_temp = {}
print(dict_temp, type(dict_temp))
# Создадим словарь. 'Ключ':значение
dict_temp = {'dict1':1, 'dict2':2.1, 'dict3':'name', 'dict4' : [1,2,3]}
print(dict_temp, type(dict_temp))
# Словарь можно инициализировать с помощью метода fromkeys
dict_temp = dict.fromkeys(['a', 'b'])
print(dict_temp, type(dict_temp)) # будет создан словарь с ключами a и b, а значения будут пустыми
# чтобы наполнить словарь, нужно в dict.fromkeys подать еще одно значение
dict_temp = dict.fromkeys(['a', 'b'], [12, '2020'])
print(dict_temp, type(dict_temp))
# метод dict
dict_temp = dict(brend = 'volvo', engine_volume = 1.5) # вводим ключ=значение, ключ=значение
print(dict_temp, type(dict_temp))
# можно инициализировать словарь с помощью генератора
dict_temp = {a: a**2 for a in range(10)}
print(dict_temp)

    # Обращения к содержимому словаря
# Обращение к содержимому происходит по ключу.
print(dict_temp[8])

    # Функции со словарями
# Часто бывает необходимо знать ключи словаря и их содержимое
# Получим все ключи словаря
print(dict_temp.keys())
# как правило не работают с этим типом. Его приводят к list.
print(list(dict_temp.keys()))
# также можно получить значения (values)
print(list(dict_temp.values()))
# все методы, которые есть в листах (list) также можно использовать при работе с ключами и со значениями
# также можно работать с парами ключ=значение с помощью функции items. Функция возвращает кортежи.
# кортеж - это тот же самый лист, только не изменяемый
print(list(dict_temp.items()))

    #Работа с элементами словаря
# необходимо получать значения, изменять и добавлять новые значения
# например нулевому ключу присвоим новое значение 100
dict_temp[0] = 100
print(dict_temp)
# также можно добавлять пары ключ:значение. Т.е. несуществующему ключу присваиваем какое-то любое значение
dict_temp['name'] = 'Dima'  # ключу name присваиваем значение Dima
print(dict_temp)            # при этом пара появится в конце словаря

    # Методы
# keys, values, items см. выше
# pop - удаление значения по ключу
dict_temp.pop('name')
print(dict_temp)
# итерирование (прохождение) по словарю
for pair in dict_temp.items():
    print(pair)     # при этом в цикле вывелись все пары
for key, value in dict_temp.items():
    print(key, value)
for keys in dict_temp.keys():
    print(keys)     # при этом в цикле вывелись все ключи
for values in dict_temp.values():
    print(values)   # при этом в цикле вывелись все значения


