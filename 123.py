temp_str = 'Все счастливые семьи похожи друг на друга, каждая несчастливая семья несчастлива по-своему. Все счастливые семьи'
print('1) методами строк очистить текст от знаков препинания;')
for i in [',','.','!',':','?']:
    temp_str = temp_str.replace(i,'')
print(temp_str)
print()

print('2) сформировать list со словами (split);')
temp_str = list(temp_str.split())   # приведем к типу list и применим метод split
print(type(temp_str), temp_str)
print()

print('3) привести все слова к нижнему регистру (map);')
new_temp_str = list(map(lambda x:x.lower(),temp_str))
print(type(new_temp_str), new_temp_str)
print()

print('4) получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;')

