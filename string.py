    # Инициализация
temp_str = 'Марка авто Volvo'
temp_str_1 = 'Марка авто "Volvo"'
temp_str_2 = 'Марка авто \'Volvo\'' # Экранирование \
print(temp_str)
print(temp_str_1)
print(temp_str_2)

    # Обращение к символам, подстрокам
# Вывод строки посимвольно
for i in range(len(temp_str)):      # len - это функция, определяющая длину строки
    print(temp_str[i])              # печатаются все символы строки в столбик

# Срезы
print(temp_str[1:4])
# Обратная нумерация
print(temp_str[0:-1])               # выведутся все символы до -1 с конца (т.е. кроме последнего)
print(temp_str[0:-3])

# Функции со строками: print и len() - длина строки
print(temp_str, len(temp_str))

# Операции со строками
temp_str_3 = 'Mercedes'
temp_str_4 = 'Audi'
print(temp_str_3 + temp_str_4)      # Операцию + лучше не использовать, т.к. занимает слишком много памяти
print(temp_str_3*2)

    # Форматирование строк
brend = 'Volvo'
price = 1.5
car = f'Марка {brend} цена {price}'
print(car)

    # Методы

# Метод split - разбивает строку на подстроки. Если в скобках ничего не указано, то разбивается по пробелам!

print(temp_str.split())
cars = 'Volvo,Audi,Lada'
print(cars.split(','))              # если в скобках указана запятая, то split разобъет строку по запятой

# upper - делает все буквы большими
print(cars.upper())

# title - первую букву делает Заглавной
print(cars.title())

# lower - делает все буквы маленькими
print(cars.lower())

# Замена подстроки в строке replace
email_adress = 'email: _mail_'
email = 'name@yandex.ru'
print(email_adress.replace('_mail_',email))     # _mail_ заменяется на переменную email

