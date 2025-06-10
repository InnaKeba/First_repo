#Modul 2
#Умовні оператори, цикли

# приклад значення для num
# num = 15  
# if num > 10:
#     print("num більше за 10")
# else:
#     print("num не більше за 10")

# умова чило х є парним? x % 2 == 0
# x = int(input('Введіть число: '))
# if x % 2 == 0:
#     print("Число x є парним.")
# else:
#     print("Число x є непарним.")

# Команда if ... elif ... else
# a = input('Введіть число: ')
# a = int(a)
# if a == 1:
#     print('Число дорівнює 1')
# elif a > 0:
#     print('Число додатне')
# else:
#     print("a <= 0")

# money = int(input("Введіть число >>> "))
# if money > 0:
#     print(f"You have {money} on your bank account")
# else:
#     print("You have no money and no debts")

# user_name = input("Enter your name: ")
# if user_name:
#     print(f"Hello {user_name}")
# else:
#     print("Hi Anonym!")

#Оператор is у Python використовується для перевірки ідентичності об'єктів
# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]
# print(a is b)  # True
# print(a is c)  # False

#Булева алгебра — це галузь математики, яка займається вивченням істинності виразів та їх обробкою. AND OR NOT 
# name = "Taras"
# age = 22
# has_driver_licence = True
# if name and age >= 18 and has_driver_licence:
#     print(f"User {name} can rent a car")
# num = int(input("Введіть число: "))

###
# num = 8
# length = len(str(num)) # len() обчислює довжину, str() перетворює число на рядок
# if length == 2 and num % 2 == 0:
#     print("Парне двозначне число")
# else:
#     print("Ні")

#Задача "FizzBuzz" 
# Задаємо конкретне число
# num = int(input("Введіть число: "))
# # Перевіряємо кратність
# if num % 3 == 0 and num % 5 == 0:
#     print("FizzBuzz")
# elif num % 3 == 0:
#     print("Fizz")
# elif num % 5 == 0:
#     print("Buzz")
# else:
#     print(num)

#блоки інструкцій. 
# x = 2
# y = - 5
# if x >= 0:
#     if y >= 0:  # x > 0, y > 0
#         print("Перша чверть")
#     else:  # x > 0, y < 0
#         print("Четверта чверть")
# else:
#     if y >= 0:  # x < 0, y > 0
#         print("Друга чверть")
#     else:  # x < 0, y < 0
#         print("Третя чверть")

#Оператор match
# fruit = "apple"
# match fruit:
#     case "apple":
#         print("This is an apple.")
#     case "banana":
#         print("This is a banana.")
#     case "orange":
#         print("This is an orange.")
#     case _:
#         print("Unknown fruit.")

#Цикли: for та while.:
#for-використовується для ітерації по елементах будь-якої послідовності (наприклад, списку, кортежу, рядка)
#Цикл while виконує блок коду, поки задана умова є істинною (True). Як тільки умова стає неправдивою (False), цикл закінчується
# fruit = 'apple'
# for char in fruit:
#     print(char)
#
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# for char in alphabet:
#     print(char, end=" ")

# some_iterable = ["a", "b", "c"]
# for i in some_iterable: #В цьому циклі i є змінною, яка на кожній ітерації приймає значення поточного елемента з some_iterable
#     print(i)

# #Цикл while
# k = 0
# while k < 10: #Цикл повтрється поки К менше 10, кожна наступна ітераціє буде збільшуватися на 1
#     k = k + 1
#     print(k)

#ФУНКЦІЇ
# Приклад

# def say_hello():
# 		# тіло функції
#     print('Привіт, Світ!')

# # виклик функції
# say_hello()

# # ще один виклик функції

# say_hello()
# 
# def print_max(a, b):
#     if a > b:
#         print(a, 'максимально')
#     elif a == b:
#         print(a, 'дорівнює', b)
#     else:
#         print(b, 'максимально')

# print_max(3, 4)  # пряма передача значень
# x = 5
# y = 7
# print_max(x, y)  # передача змінних у якості аргументів

# *****

# def add_numbers(num1: int, num2: int) -> int:
#     sum = num1 + num2
#     return sum

# result = add_numbers(5, 10)
# print(result)  # Виведе: 15

# def string_to_codes(string: str) -> dict:
#     # Ініціалізація словника для зберігання кодів
#     codes = {}  
#     # Перебір кожного символу в рядку
#     for ch in string:  
#         # Перевірка, чи символ вже є в словнику
#         if ch not in codes:
#             # Додавання пари символ-код в словник  
#             codes[ch] = ord(ch)  
#             # ord() - Ця функція приймає один символ і повертає його код ASCII. 
#     return codes
# result = string_to_codes("Hello world!")
# print(result)

# def real_cost(base: int, discount: float = 0) -> float:
#     return base * (1 - discount)
# # Функція використовує формулу base * (1 - discount) для обрахунку остаточної вартості. Якщо знижка відсутня, то використовується лише базова ціна
# price_bread = 15
# price_butter = 50
# price_sugar = 60

# current_price_bread = real_cost(price_bread)
# current_price_butter = real_cost(price_butter, 0.05)
# current_price_sugar = real_cost(price_sugar, 0.07)
# print(f'Нова вартість хліба: {current_price_bread}')
# print(f'Нова вартість масла: {current_price_butter}')
# print(f'Нова вартість цукру: {current_price_sugar}')

# Home Work:
# 1
# is_next = None
# num = int(input("Enter the number of points: "))
# if num >= 83:
#      is_next = True
# else:
#      is_next = False
# print(f"Кандидат проходить в наступний тур: {is_next}")

# 2
# work_experience = int(input("Enter your full work experience in years: "))
# if 1 < work_experience <= 5: 
#     developer_type = "Middle"
# elif work_experience <= 1:  
#     developer_type = "Junior"
# else:  
#     developer_type = "Senior"
# print(f"Ваш рівень розробника: {developer_type}")

# 3
# num = int(input("Enter a number: "))
# if num > 0:
#     if num % 2 == 1:
#         result = "Positive odd number"
#     else:
#         result = "Positive even number"
# elif num < 0:
#     result = "Negative number"
# else:
#     result = "It is zero"

# 4
# num = int(input("Enter the integer (0 to 100): "))
# sum = 0
# while num > 0:
#       sum += num
#       num -= 1
#       print(f"Сума всіх чисел від 1 до введеного: {sum}")

# 5
# message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
# search = "r"
# result = 0
# for char in message:
#     if char == search:
#      result += 1
# print(f"Символ '{search}' зустрічається {result} раз у рядку.")

# 6
# pool = 1000
# quantity = int(input("Enter the number of mailings: "))
# try:
#     chunk = int(pool / quantity)
# except ZeroDivisionError:
#     print('Divide by zero completed!')

# 7
# def greeting ():
#     print("Hello world!")
# greeting()

# 8
# def invite_to_event(username):
#     return f"Dear {username}, we have the honour to invite you to our event"
# print(invite_to_event("Inna"))

# 9
# def discount_price(price, discount):
#     def apply_discount():
#         nonlocal price 
#         price = price * (1 - discount)
#         return price # Повертаємо оновлену ціну
# # викликаємо функцію
#     return apply_discount()  

# 10
# def get_fullname(first_name, last_name, middle_name=""): #Позначаємо middle_name="" як може мати пусте значення
#     if middle_name: # Перевірка заповнення middle_name
#        return f"{first_name} {middle_name} {last_name}"
#     return f"{first_name} {last_name}"
# print(get_fullname("Inna", "Keba"))
  
# 11
# def format_string(string, length):
#     if len(string) >= length:#Якщо довжина string більша або дорівнює length, поверніть рядок без змін.
#         return string
#     spaces = (length - len(string)) // 2
#     return " " * spaces + string  

# 12
 def first(size, *args):
     return size + len(args) #len(args) підраховує кількість додаткових аргументів
 def second(size,**kwargs):
     return size + len(kwargs) #len(kwargs) підраховує кількість ключових аргументів
 print(first(5, 10, "Inna")) 
 print(second(3, name="Inna", age=35))

# 13
# def factorial(n):
#     if n < 2:
#         return 1
#     else:
#         return n * factorial(n - 1)

 # def number_of_groups(n, k): #n - загальна кількість людей та k - кількість переможців.
 #     if k > n or k < 0:
 #       return "Некоректні значення: k не може бути більшим за n або меншим за 0"
 #     return factorial(n) // (factorial(n - k) * factorial(k))      