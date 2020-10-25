"""
6.1 Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
 и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.  Переключение между режимами должно осуществляться
только в указанном порядке (красный, желтый, зеленый). Проверить работу примера,
создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
выводить соответствующее сообщение и завершать скрипт.
"""
from time import sleep
from colorama import init
from colorama import Fore, Back, Style

init()


# Методы класса
class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зелёный', 'Желтый']

    def running(self):
        i = 0
        while i < 4:
            print(Style.RESET_ALL + f'Переключение светофора')
            if i == 0:
                sleep(2)
                print(Fore.BLACK + Back.RED + f'{TrafficLight.__color[i]}')
            elif i == 1:
                sleep(7)
                print(Fore.BLACK + Back.YELLOW + f'{TrafficLight.__color[i]}')
            elif i == 2:
                sleep(2)
                print(Fore.BLACK + Back.GREEN + f'{TrafficLight.__color[i]}')
            elif i == 3:
                sleep(5)
                print(Fore.BLACK + Back.YELLOW + f'{TrafficLight.__color[i]}')
                print(Style.RESET_ALL)

            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()

'''
6.2 Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. 
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, 
необходимого для покрытия всего дорожного полотна. Использовать формулу: 
длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, 
толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
'''


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        total = self._length * self._width * 25 * 5 / 1000

        print('Программа расчёта массы асфальта по исходным данным:\n'
              f'Длина: 10000 м.\nШирина: 30 м.\n'
              f'Масса асфальта на 1 кв метр: 25кг * 1см\n'
              f'Необходимо {total} тонн для строительства')


Road_1 = Road(30, 10000)
Road_1.mass()

'''
6.3 Реализовать базовый класс Worker (работник), в котором определить атрибуты: 
name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным 
и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. 
Создать класс Position (должность) на базе класса Worker. 
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных 
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


a = Position('\nMatvey ', 'Safonov ', 'Goalkeeper', 1500000, 500000)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())


'''
6.4 Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: 
speed, color, name, is_police (булево).  А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''


class Car:
    # атрибуты
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # методы
    def go(self):
        return f'{self.name} начал движение'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_left(self):
        return f'{self.name} повернул на лево.'

    def turn_right(self):
        return f'{self.name} повернул на право'

    def show_speed(self):
        return f'Текущая скорость {self.name} составляет - {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городского автомобиля {self.name} составляет - {self.speed}')

        if self.speed > 40:
            return f'Скорость автомобиля {self.name} выше, чем разрешенная для городского автомобиля'
        else:
            return f'Скорость автомобиля {self.name} разрешённая для городской машины'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость рабочего автомобиля {self.name} равна - {self.speed}')

        if self.speed > 60:
            return f'Скорость автомобиля {self.name} выше допустимой для рабочей машины'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} принадлежит полиции.'
        else:
            return f'{self.name} не принадлежит полиции'


AudiS8 = SportCar(100, 'Желтый', 'Audi', False)
KiaRio = TownCar(30, 'Красный', 'KiaRio', False)
Gaz2705 = WorkCar(70, 'Зелёный', 'Gaz', False)
Mustang = PoliceCar(110, 'Синий',  'Mustang', True)
print(f'\n{Gaz2705.color} автомобиль {Gaz2705.go()}')
print(f'{Gaz2705.show_speed()}')
print(f'{KiaRio.color} автомобиль {KiaRio.go()}')
print(f'{KiaRio.show_speed()}')
print(f'{AudiS8.name} покрашен в {AudiS8.color}')
print(AudiS8.show_speed())
print(f'Когда {AudiS8.stop()}, то {Mustang.turn_right()}, '
      f'затем автомобиль {Mustang.turn_left()}')
print(Mustang.show_speed())
print(Mustang.police() + f' Цвет - {Mustang.color}')
print(f'Автомобиль {AudiS8.name} принадлежит к полиции? {AudiS8.is_police}')


'''
6.5 Реализовать класс Stationery (канцелярская принадлежность). 
Определить в нем атрибут title (название) и метод draw (отрисовка). 
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение. 
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''


class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'\nВы взяли {self.title}. Запуск отрисовки ручкой'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки карандашом'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки маркером'


pen = Pen('"Ручку"')
pencil = Pencil('"Карандаш"')
handle = Handle('"Маркер"')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
