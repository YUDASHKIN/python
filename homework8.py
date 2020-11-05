"""
8.1 Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'Всё верно!!!'
                else:
                    return f'Значение "год" не совпадает'
            else:
                return f'Значение "месяц" не совпадает'
        else:
            return f'Значение "день" не совпадает'

    def __str__(self):
        return f'Текущая дата: {Data.extract(self.day_month_year)}'


today = Data('11 - 10 - 2001')
print(today)
print(Data.valid(11, 11, 2022))
print(today.valid(11, 13, 2011))
print(today.valid(32, 10, 2001))
print(Data.extract('10 - 10 - 2011'))
print(today.extract('10 - 10 - 2020'))
print(Data.valid(1, 11, 2000))

'''
8.2 Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. 
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем 
нуля в качестве делителя программа должна корректно обработать эту ситуацию и 
не завершиться с ошибкой.
'''


# noinspection PyBroadException
class DivisionByNull:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def divide_by_null(numerator, denominator):
        try:
            return numerator / denominator
        except Exception:
            return f"Делить на ноль нельзя!!!"


div = DivisionByNull(10, 100)
print(div.divide_by_null(100, 0))
print(div.divide_by_null(100, 4))
print(div.divide_by_null(10, 22))

'''
8.3 Создайте собственный класс-исключение, который должен проверять содержимое списка 
на отсутствие элементов типа строка и булево. Проверить работу исключения на реальном примере. 
Необходимо запрашивать у пользователя данные и заполнять список. 
Класс-исключение должен контролировать типы данных элементов списка.
'''


class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - строка или булево")
                y_or_n = input(f'Попробовать еще раз? Да/Нет ')

                if y_or_n == 'ДА' or y_or_n == 'да' or y_or_n == 'lf':
                    print(try_except.my_input())
                elif y_or_n == 'НЕТ' or y_or_n == 'нет':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'


try_except = Error(1)
print(try_except.my_input())

'''
8.7 Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», 
реализуйте перегрузку методов сложения и умножения комплексных чисел. 
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и 
выполнив сложение и умножение созданных экземпляров. 
Проверьте корректность полученного результата.
'''


class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна:')
        return f' {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно:')
        return f' {self.a * other.a - self.b * other.b} + {self.b * other.b} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z_1 = ComplexNumber(2, -3)
z_2 = ComplexNumber(4, 5)
print(f'1-ое значение {z_1}')
print(f'2-ое значение {z_2}')
print(z_1 + z_2)
print(z_1 * z_2)

'''
8.4 Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
А также класс «Оргтехника», который будет базовым для классов-наследников. 
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
В базовом классе определить параметры, общие для приведенных типов. 
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники. 
'''

'''
8.5 Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники 
на склад и передачу в определенное подразделение компании. Для хранения данных 
о наименовании и количестве единиц оргтехники, а также других данных, можно использовать 
любую подходящую структуру, например словарь.
'''

'''
8.6 Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых 
пользователем данных. Например, для указания количества принтеров, отправленных 
на склад, нельзя использовать строковый тип данных. 
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» 
максимум возможностей, изученных на уроках по ООП.
'''
import collections


# склады: основной склад и склады подразделений
class Warehouse:
    def __init__(self, name):
        self.name = name
        self.items = []

    def __str__(self):
        strres = f'Состояние склада "{self.name}":\n'
        if self.items:
            for i, item in enumerate(self.items):
                strres += f"{i}: {item}\n"
        else:
            strres += 'пусто!\n'
        return strres

    # оприходовать оборудование на склад warehouse
    def debit(self, equipment):
        self.items.append(equipment)

    # "списать" оборудование со склада
    def _credit(self, equipment):
        if not equipment in self.items:
            raise KeyError(equipment)
        self.items.remove(equipment)
        # # найдём нужное нам оборудование: того же производителя и модели и спишем
        # for item in self.items:
        #     if item.shortname() == equipment.shortname():

    # оприходовать оборудование на склад warehouse
    def moveto(self, equipment, another_warehouse):
        self._credit(equipment)
        another_warehouse.debit(equipment)


# --> я буду только контролировать цену и вес оборудования при создании объекта Equipment
class Equipment():
    def __init__(self, brandname, model, price, weight):
        if not ((type(price) is int or type(price) is float) and price > 0):
            raise ValueError('price should be positive number')
        if not ((type(weight) is int or type(weight) is float) and weight > 0):
            raise ValueError('weight should be positive number')

        self.brandname = brandname
        self.model = model
        self.price = price
        self.weight = weight

    def __str__(self):
        return f'{self.itemname} {self.model} ценою {str(self.price)} ₽ и весом {str(self.weight)} кг.'

    # краткое наименование
    def shortname(self):
        return f'{self.itemname} {self.model}'


class Printer(Equipment):
    itemname = 'Принтер'


class Scanner(Equipment):
    itemname = 'Сканер'


class Xerox(Equipment):
    itemname = 'Ксерокс'


e1 = Printer('Xerox Phaser', '3020Bl', 7390, 4.1)
print(e1)

e2 = Scanner('HP Laser', '107w (4ZB78A)', 7690, 4.16)
print(e2)

e3 = Xerox('Струйный принтер Epson', 'L132', 11990, 2.7)
print(e3)

warehouse_main = Warehouse('main')
warehouse_moscow = Warehouse('MoscowCityOffice')
warehouse_city = Warehouse('CityOffice')

warehouse_main.debit(e1)
warehouse_main.debit(e2)
warehouse_main.debit(e3)

print(warehouse_main)

warehouse_main.moveto(e1, warehouse_moscow)

print(warehouse_main)

warehouse_main.moveto(e2, warehouse_moscow)

print(warehouse_main)

warehouse_main.moveto(e3, warehouse_city)

print(warehouse_main)

try:
    warehouse_main.moveto(e1, warehouse_city)
except KeyError as e:
    print('оборудование не найдено и не может быть списано')

print(warehouse_main)

try:
    e4 = Xerox('Xerox', 'SXD55', -123456, -12.34)
    print(e4)
except ValueError as e:
    print(e)
