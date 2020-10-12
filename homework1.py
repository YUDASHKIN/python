"""
1.1 Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя
несколько чисел и строк и сохраните
в переменные, выведите на экран.
"""

numb = 5
text = "яблок"
print(f'{numb} {text}')

print("Анкета: ")
name = input("Как Вас зовут? ")
age = int(input("Сколько Вам полных лет? "))
country = input("В какой стране Вы родились? ")
print(f"Имя: {name}; Возраст: {age}; Страна: {country}.")  # изменил формат

'''
1.2 Пользователь вводит время в секундах. 
Переведите время в часы, минуты и секунды 
и выведите в формате чч:мм:сс. 
Используйте форматирование строк. 
'''

timeSec = int(input("Введите время в секундах: "))
hours = timeSec // 3600
minutes = (timeSec - hours * 3600) // 60
seconds = timeSec - (hours * 3600 + minutes * 60)
print(f"Точное время: {hours:02}:{minutes:02}:{seconds:02}")  # показ "0"

'''
1.3 Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369
'''

n = int(input("Введите целое число, для вычисления суммы чисел n + nn + nnn: "))
result = (n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))
print(f"Сумма чисел равна: %d" % result)

'''
1.4 Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''

n = int(input("Введите целое положительное число: "))
maxNumber = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > maxNumber:
        maxNumber = n % 10
    if n > 9:
        continue
    else:
        print("Максимальное цифра введенного числа равна: %d" % maxNumber)
        break

'''
1.5 Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или
убыток — издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы
и определите прибыль фирмы в расчете на одного сотрудника.
'''

proceeds = float(input("Введите значение выручки фирмы: "))  # int заменил float
costs = float(input("Введите значение издержек фирмы: "))  # int заменил float
profit: float = proceeds - costs
lesion: float = costs - proceeds
if proceeds > costs:
    print(f'Фирма в прибыли: {profit:.2f} RU, рентабельность составит: {profit / proceeds:.2f} RU')
    staff = int(input("Укажите число сотрудников фирмы: "))
    print(f"Прибыль фирмы на одного сотрудника составит {profit / staff:.2f} RU")
elif profit == 0:
    print("Фирма работает в нулевую прибыль")
else:
    print(f'Фирма в убытке: {lesion:.2f} RU')

'''
1.6 Спортсмен занимается ежедневными пробежками. 
В первый день его результат составил 'a' километров. 
Каждый день спортсмен увеличивал результат на 10 % 
относительно предыдущего. 
Требуется определить номер дня, на который общий 
результат спортсмена составить не менее 'b' километров. 
Программа должна принимать значения параметров 'a' и 'b' и  
выводить одно натуральное число — номер дня.
'''

a = float(input("Введите результаты пробежки первого дня в (км): "))  # int заменил float
b = float(input("Введите результат по нормативу в (км): "))  # int заменил float
numbDay = 1
while a < b:
    a = a + 0.1 * a  # a += a * 0.1
    numbDay += 1
print(f"на {numbDay}" "-й день спортсмен достиг результата — не менее 3 км.")
