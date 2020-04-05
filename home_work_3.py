text = open('C:/Users/Светлана/Desktop/123/text_3.txt','r',encoding='UTF-8')
text = text.read()
print('1) методами строк очистить текст от знаков препинания;')

for i in [',','.','!',':','?','—',';','«','»','(',')']:
    text = text.replace(i,'')
print(text)
print()

print('2) сформировать list со словами (split);')
text = list(text.split())   # приведем к типу list и применим метод split
print(type(text), text)
print()

print('3) привести все слова к нижнему регистру (map);')
new_text = list(map(lambda x:x.lower(),text))
print(type(new_text), new_text)
print()

print('4) получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;')
# инициализируем словарь с помощью генератора
temp_dict = {i: new_text.count(i) for i in new_text}
print(type(temp_dict),temp_dict)
print()

print('5) вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).')
a = list(temp_dict.items())
a.sort(key=lambda i: i[1],reverse=True)
for i in a[0:5]:
    print(i[0], ':', i[1])

temp_set = set(new_text)
print('Количество разных слов в тексте',':',len(temp_set))

