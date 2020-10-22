"""
5.1 Создать программно файл в текстовом формате,
 записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

file = open("out_file.txt", "w", encoding="utf-8")
str1 = input("Введите данные: ")
str2 = input("Введите данные: ")
str3 = input("Введите данные: ")
str_list = [f"{str1}\n{str2}\n{str3}\n"]
file.writelines(str_list)
file.close()

'''
5.2 Создать текстовый файл (не программно), сохранить в нем несколько строк,
 выполнить подсчет количества строк, количества слов в каждой строке.
'''

my_file = open("out_file.txt", "r", encoding="utf-8")
content = my_file.read()
print(f'\nСодержимое файла:\n{content}')
my_file = open("out_file.txt", "r", encoding="utf-8")
content = my_file.readlines()
print(f'Колличество строк в файле - {len(content)}')
my_file = open("out_file.txt", "r", encoding="utf-8")
content = my_file.read()
content = content.split()
print(f"Общее колличество слов - {len(content)}")
my_file.close()

'''
5.3 Создать текстовый файл (не программно), построчно записать фамилии
 сотрудников и величину их окладов (не менее 10 строк). Определить,
 кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
'''

with open("text_3.txt", "r", encoding="utf-8") as my_file:
    salary = []
    staff = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
            staff.append(i[0])
        salary.append(i[1])
print(f"\nСотрудники имееющиет оклад менее 20 тыс. $ :\n {staff}\n"
      f"Средняя величина дохода сотрудников: {sum(map(float, salary)) / len(salary)} $")

'''
5.4 Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
 построчно данные. При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

trans = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('text_4.txt', 'r', encoding='utf-8') as my_file:
    for i in my_file:
        i = i.split(' ', 1)
        new_file.append(trans[i[0]] + '  ' + i[1])
    print(f'\n{new_file}')

with open('text_4new.txt', 'w', encoding='utf-8') as my_file2:
    my_file2.writelines(new_file)

'''
5.5 Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''


def result():
    try:
        with open('file_5.txt', 'w+') as file5:
            line = input('\nВведите цифры через пробел: \n')
            file5.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Ошибка ввода-вывода')


result()
