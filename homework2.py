"""
1.1 Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.
"""

my_list = [3, 9.5, True, 'жизнь_хороша', None, False]
for el in range(len(my_list)):
    print(type(my_list[el]))

'''
1.2 Для списка реализовать обмен значений соседних элементов, т.е.
значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
'''

numb = int(input("Введите количество элементов в списке: "))
my_list = []
i = 0
el = 0
while i < numb:
    my_list.append(input("Следующее значение элемента: "))
    i += 1
for elem in range(int(len(my_list) / 2)):
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
    el += 2
print(my_list)

'''
1.3 Пользователь вводит месяц в виде целого числа от 1 до 12. 
Сообщить к какому времени года относится месяц 
(зима, весна, лето, осень). Напишите решения через list и через dict.
'''

day_month = int(input('Введите "месяц" в виде целого числа от 1 до 12: '))
seasons_winter = ['Декабрь', 'Январь', 'Февраль']
seasons_Spring = ['Март', 'Апрель', 'Май']
seasons_Summer = ['Июнь', 'Июль', 'Август']
seasons_Autumn = ['Сентябрь', 'Октябрь', 'Ноябрь']
seasons_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
if day_month == 12:
    print(f'{seasons_winter[0]}')
    print(f'{seasons_dict.get(1)}')
elif day_month == 1:
    print(f'{seasons_winter[1]}')
    print(f'{seasons_dict.get(1)}')
elif day_month == 2:
    print(f'{seasons_winter[2]}')
    print(f'{seasons_dict.get(1)}')
elif day_month == 3:
    print(f'{seasons_Spring[0]}')
    print(f'{seasons_dict.get(2)}')
elif day_month == 4:
    print(f'{seasons_Spring[1]}')
    print(f'{seasons_dict.get(2)}')
elif day_month == 5:
    print(f'{seasons_Spring[2]}')
    print(f'{seasons_dict.get(2)}')
elif day_month == 6:
    print(f'{seasons_Summer[0]}')
    print(f'{seasons_dict.get(3)}')
elif day_month == 7:
    print(f'{seasons_Summer[1]}')
    print(f'{seasons_dict.get(3)}')
elif day_month == 8:
    print(f'{seasons_Summer[2]}')
    print(f'{seasons_dict.get(3)}')
elif day_month == 9:
    print(f'{seasons_Autumn[0]}')
    print(f'{seasons_dict.get(4)}')
elif day_month == 10:
    print(f'{seasons_Autumn[1]}')
    print(f'{seasons_dict.get(4)}')
elif day_month == 11:
    print(f'{seasons_Autumn[2]}')
    print(f'{seasons_dict.get(4)}')
else:
    print('Вы ввели неверный параметр, повторите снова!')

'''
1.4 Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать. 
Если слово длинное, выводить только первые 10 букв в слове.
'''

line = input('Напишите 3 своих лучших качества: ')
a = line.split(' ')
for i, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}. - {el}")

'''
1.5 Реализовать структуру «Рейтинг», представляющую собой 
не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. 
Если в рейтинге существуют элементы с одинаковыми значениями, 
то новый элемент с тем же значением должен разместиться после них.
'''

print('«Рейтинг» - [7, 5, 3, 3, 2]')
user_numb = int(input('Введите число для рейтинга: '))
my_list = [7, 5, 3, 3, 2]
b = my_list.count(user_numb)
for el in my_list:
    if b > 0:
        a = my_list.index(user_numb)
        my_list.insert(a + b, user_numb)
        break
    else:
        if user_numb > el:
            d = my_list.index(el)
            my_list.insert(d, user_numb)
            break
        elif user_numb < my_list[len(my_list) - 1]:
            my_list.append(user_numb)
print(my_list)

'''
1.6 Реализовать структуру данных «Товары». Она должна представлять
собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами 
(характеристиками товара: название, цена, количество, единица измерения). 
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором 
каждый ключ — характеристика товара, например название, а значение — 
список значений-характеристик, например список названий товаров.
'''

goods = []
features = {'Название:': '', 'Цена:': '', 'Колличество:': '', 'Ед.:': 'шт.'}
analytics = {'Название:': [], 'Цена:': [], 'Колличество:': [], 'Ед.:': []}
num = 0
feature_ = None
control = None
while True:
    control = input("Для выхода нажмите 'Q', для продолжения нажмите 'Enter', для аналитики нажмите 'A'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print('\nТекущая аналитика\n')
        for key, value in analytics.items():
            print(f'{key[:25]:>01}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature_ = input(f'Функция ввода "{f}"')
        features[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))
