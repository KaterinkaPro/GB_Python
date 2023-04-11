""" class Human:
    def __init__(self, name, age,color) -> None:
        self.name = name
        self.age = age
        self.color = color

    def say_hello(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age} лет.")

    def __eq__(self, other: object) -> bool:
        if type(other) == Human:
            if self.age == other.age:
                return "Они одногодки"
            else:
                return "у них разный возраст"


    def __add__(self, other):
        return self.age + other.age    

ivan = Human("Иван", 37, "brown")
max_ = Human("Макс", 22, "green")
# print(ivan.color, ivan.age, ivan.name)

ivan.say_hello()

# print(type(ivan))
# print(ivan == max) """

# a = 5
# b = a
# a = "trtr"
# print(a)
# print(b)
# # Динамическая типизация

# изменяемое, неизменяемое
# set, list, dict - изменяемые
# import time

# a = "1"
# start = time.perf_counter()
# for i in range(10_000_000):
#     a += "1"
# end = time.perf_counter()
# print(end - start)

# 1.Создать класс, описывающий человека. Должны быть поля для имени, фамилии и возраста.
# Создать экземпляр и вывести информацию о человеке.
#2.Доработать предыдущий класс, чтобы вся информация о человеке была доступна при вызове str над экземпляром.
# 3.Добавить метод greet, вызов которого будет выводить в консоль информацию о человеке в формате 
# "Привет! Меня зовут Петров Василий, мне 12 лет".
# 4.Добавить атрибут grades, в котором будет храниться список оценок. 
# Создать список учеников, заполняя оценки случайными числами. 
# и вывести информацию о них в порядке убывания среднего балла. 
# Заполнение оценок и подсчёт среднего балла вынести в отдельные методы.
#


""" 
class Human:
    def __init__(self, name, famil, age):
        self.name = name
        self.famil = famil
        self.age = age
        self.grades = []
    
    
    def greet(self):
        print(f'Привет! Меня зовут {self.famil} {self.name}, мне {self.age} лет.')


    def add_grades(self):
        import random
        for i in range(6):
            self.grades.append(random.randint(2,5))

    def mean_grades(self):
        return sum(self.grades)/len(self.grades)
        
            
    def __str__(self): # вывод содержимого имени
        return f'{self.name}, {self.famil}, {self.age}, {self.grades}'

    def __repr__(self): # вывод список оценок
        return f'{self.name} {self.mean_grades()}'


ivan = Human('Иван', 'Илонов', 24)
sergey = Human('Сергей', 'Петров', 22)
anya = Human('Анна', 'Максимова', 23)
kolya = Human('Коля', 'Семенов', 20)

students=[ivan, sergey, anya, kolya]
for i in students:
    i.add_grades()
    print(f'{i}')

students.sort(key=lambda x: x.mean_grades(), reverse=True)
print(students) """

# 5. Создайте класс прямоугольник — Rectangle. 
# Метод __init__ принимает две точки — левый верхний и правый нижний угол. 
# Каждая точка представлена экземпляром класса Point. 
# Реализуйте методы вычисления площади и периметра прямоугольника.
#
# 6.Добавьте в класс Rectangle метод has_point. 
# Метод принимает точку на плоскости и возвращает True, 
# если точка находится внутри прямоугольника и False в противном случае.

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, point1, point2) -> None:
        self.left_up = point1
        self.right_down = point2


    def sqrt(self):
        sqrt = abs(self.left_up.x - self.right_down.x)*abs(self.left_up.y - self.right_down.y)
        print(sqrt)

    def per(self):
        p = 2*(abs(self.left_up.x - self.right_down.x)+abs(self.left_up.y - self.right_down.y))
        print(p)

    def has_point(self, point_x, point_y):
        return (self.left_up.x <= point_x <= self.right_down.x and self.left_up.y <= point_y <= self.right_down.y)


point1 = Point(5,6)
point2 = Point(2,3)
rect1 = Rectangle(point1, point2)

rect1.sqrt()
rect1.per()
print(rect1.has_point())

