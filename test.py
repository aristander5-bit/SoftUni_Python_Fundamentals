# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)

# def sum_numbers(a, b):
#     if a > 0 and b > 0:
#         return a + b
# result = sum_numbers(3, 4)
# print(result)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
# print(even_numbers)
# print(odd_numbers)

# numbers = [1,2,3,4,5]
# squares = [num ** 2 for num in numbers if num % 2 ==0]
# print(squares)

# letters = ['a', 'b', 'c', 'd']
# uppercase_letters = [letter.upper() for letter in letters]
# print(uppercase_letters)

# keys = ['name', 'age', 'city']
# values = ['John', '33', 'Sofia']
# info_dict = {k: v for (k, v) in zip(keys, values)}
# print(info_dict)

# sentence = "Hello, Python"
# unique_chars = {char for char in sentence if char.isalpha()}
# print(unique_chars)

# numbers = [1, 2, 3, 4, 5]
# result = [num ** 2 if num % 2 == 0 else num ** 3 for num in numbers]
# print(result)

# my_list = [1,2,3,4]
# my_list += [5,6,7,8]
# print(my_list)

# my_list = [1, 2, 3, 4, 5]
# my_list.extend([6, 7, 8])
# print(my_list)

# my_list = [1, 2, 3, 4, 5]
# number = my_list.pop(0)
# print(my_list)
# print(number)

# number_list = [6,2,1,4,3,5]
# sorted_numbers = sorted(number_list)
# print(sorted_numbers)

# words = ['banan', 'apple', 'cherry', 'date']
# sorted_by_length = sorted(words, key=len, reverse=True)
# print(sorted_by_length)

# numbers = [1, 2, 3, 4, 5]
# squares = list(map(lambda x: x**2, numbers))
# print(squares)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)

# numbers = [1, 2, 3, 4, 5]
# index1 = 1
# index2 = 3
# numbers[index1], numbers[index2] = numbers[index2], numbers[index1]
# print(numbers)

# lst1 = ['a', 'b']
# lst2 = ['c', 'd']
# letters = lst1 + lst2
# print(letters)

# numbers = [1, 2, 3, 4, 5, 5, 2, 3, 1]
# print(set(numbers))

# from functools import reduce
# numbers = [1, 2, 3, 4, 5]
# result = reduce(lambda x, y: x + y, numbers)
# print(result)
#
# population_string = input().split(", ")
# min_wealth = int(input())
#
# population = []
#
# for elements in population_string:
#     number = int(elements)
#     population.append(number)
#
# if sum(population) < len(population) * min_wealth:
#     print("No equal distribution possible")
#     exit()
# else:
#     for element in range(len(population)):
#         if population[element] < min_wealth:
#             diff = min_wealth - population[element]
#
#             wealth_people = max(population)
#             wealth_index = population.index(wealth_people)
#             population[wealth_index] -= diff
#             population[element] += diff
#
# print(population)
#
# voltage = int(input(f"Voltage is: "))
# current = float(input(f"Current is: "))
# power_factor = float(input(f"Power factor is: "))
# active_power = voltage * current * power_factor
# print(f"Active power is: {active_power:.2f}")
#
# from math import sqrt
# def calculator_power_impedance():
#     u = float(input("Please enter your voltage: "))
#     i = float(input("Please enter your amperage: "))
#     cos_psi = float(input("Please enter your cos_psi: "))
#     if not 0 <= cos_psi <= 1:
#         print("Please enter number between 0 and 1.")
#         return
#     if u == 0 or i == 0:
#         print("Please enter a positive number.")
#         return
#     sin_psi = sqrt(1 - cos_psi ** 2)
#     s = u * i
#     p = s * cos_psi
#     q = s * sin_psi
#     z = u / i
#     r = z * cos_psi
#     x = z * sin_psi
#     print(f"{s:.2f}")
#     print(f"{p:.2f}")
#     print(f"{q:.2f}")
#     print(f"{r:.2f}")
#     print(f"{z:.2f}")
#     print(f"{x:.2f}")
# calculator_power_impedance()

# class Car:
#     def __init__(self, brand, colour):
#         self.brand = brand
#         self.colour = colour
#     def drive(self):
#         print(f"{self.colour} {self.brand} is moves!")
# car1 = Car("BMW", "Black")
# car2 = Car("Mercedes", "White")
# car1.drive()
# car2.drive()
#
# class Engine:
#     def __init__(self, horsepower):
#         self.horsepower = horsepower
#         self.is_running = False
#     def start(self):
#         self.is_running = True
#         print(f"Engine {self.horsepower} hp is running!")
#     def stop(self):
#         self.is_running = False
#         print(f"Engine {self.horsepower} hp is stopped!")
# class Car:
#     def __init__(self, brand, engine):
#         self.brand = brand
#         self.engine = engine
#     def drive(self):
#         if  not self.engine.is_running:
#             print("Cannot drive - engine is not starting!")
#         else:
#             print(f"{self.brand} drives straight!")
#     def start_engine(self):
#         self.engine.start()
# class Person:
#     def __init__(self, name, car):
#         self.name = name
#         self.car = car
#     def go_to_work(self):
#         print(f"{self.name} is go to work!")
#         self.car.start_engine()
#         self.car.drive()
# engine = Engine(150)
# car = Car("Mercedes", engine)
# person = Person("Ivan", car)
# person.go_to_work()
#
# class Car:
#     def __init__(self, color):
#         self.color = color
#     def drive(self):
#         print(f"The {self.color} car is driving.")
# car1 = Car("black")
# car2 = Car("blue")
# car3 = Car("red")
# car4 = Car("green")
# car5 = Car("yellow")
# car1.drive()
# car2.drive()
# car3.drive()
# car4.drive()
# car5.drive()
#
# class Car:
#     def __init__(self, color, brand):
#         self.color = color
#         self.brand = brand
#     def info(self):
#         return f"This car is a {self.color} {self.brand}"
# car1 = Car("red", "BMW")
# car2 = Car("blue", "Mercedes")
# print(car1.info())
# print(car2.info())
#
# class Person:
#     def __init__(self, name, age=0):
#         self.name = name
#         self.age = age
#     def say_hello(self):
#         return f"Hello, {self.name}!"
# person1 = Person('Ivan', 25)
# person2 = Person('Gosho', 28)
# person3 = Person('Pesho', 30)
# print(person1.say_hello())
# print(person2.say_hello())
# print(person3.say_hello())
#
# class Person:
#     def __init__(self, name, age=0):
#         self.name = name
#         self.age = age
#     def say_hello(self):
#         return f"Hello, {self.name}!"
# me = Person("Peter", 25)
# print(me.age)
# me.age += 1
# print(me.age)
#
# class Car:
#     wheels = 4
#     def __init__(self, brand):
#         self.brand = brand
# car1 = Car("BMW")
# car2 = Car("Ford")
# car3 = Car("Honda")
# print(car1.wheels)
# print(car2.wheels)
# print(car3.wheels)
# Car.wheels = 6
# print(car1.wheels)
# print(car2.wheels)
# print(car3.wheels)
#
# class Car:
#     wheels = 4
#     def __init__(self, brand):
#         self.brand = brand
#     def drive(self):
#         print(f"{self.brand} is driving on {self.wheels} wheels")
# car1 = Car("BMW")
# car2 = Car("Audi")
# car1.drive()
# car2.drive()





