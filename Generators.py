# Задача 1: Фабрика Функций
# Написать функцию, которая возвращает различные математические функции (например, деление, умножение) в
# зависимости от переданных аргументов.
#
# Задача 2: Лямбда-Функции
# Использовать лямбда-функцию для реализации простой операции и написать такую же функцию с использованием def.
# Например, возведение числа в квадрат
#
# Задача 3: Вызываемые Объекты
# Создать класс с Rect c полями a, b которые задаются в __init__ и методом __call__, который возвращает площадь
# прямоугольника, то есть a*b.

#    ЗАДАЧА 1
def create_operation(operation):
    if operation == "add":
        def add(x, y):
            return x + y
        return add
    elif operation == "subtract":
        def subtract(x, y):
            return x - y
        return subtract
    elif operation == "multiplication":
        def multiplication(x, y):
            return x * y
        return multiplication
    elif operation == "divid":
        def divid(x, y):
            return x / y
        return divid

print('Задача 1. Фабрика функций.')
x = 3
y = 2
print(f'Исходные данные: x = {x}; y = {y}')
my_func_add = create_operation("add")
print(f'Результат сложения: {my_func_add(x,y)}')
my_func_subtract = create_operation("subtract")
print(f'Результат вычитания: {my_func_subtract(x,y)}')
my_func_multipl = create_operation("multiplication")
print(f'Результат умножения: {my_func_multipl(x,y)}')
my_func_div = create_operation("divid")
print(f'Результат деления: {my_func_div(x,y)}')
print('************************************************************')


# ЗАДАЧА 2
multiply = lambda x: x ** 2
print('Задача 2. Лямбда. Возведение числа в квадрат')
print(f'Исходное значение: х = {x}')
print(f'Результат через лямбда: {multiply(x)}')

def multiply_def(x):
   return x ** 2
print(f'Результат с использованием def: {multiply_def(x)}')
print('******************************************************************')

#ЗАДАЧА 3
class Rect:
   def __init__(self, a):
       self.a = a
       #self.b = b
   def __call__(self, b):
       return self.a * b

print('Задача 3. Вызываемые объекты')
a = 2
b = 4
print(f'Стороны прямоугольника: a = {a}, b = {b}')
repeat_five = Rect(a)
Sqr = repeat_five(b)
print(f'Площадь прямоугольника: {Sqr}')