
# print(list(str(123456789)))
# # ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#
# print(list(map(int, ['1', '2', '3', '4', '5', '6', '7', '8', '9'])))
# # [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# list_digit = list(map(int, list(str(123456789))))
# print(5 in list_digit)
# # True
#
# print('5' in str(123456789))
# # True
#
# print('3' and '7' in str(123456789))
# # True
#
# print('3' in str(123456789) and '7' in str(123456789))
# # True

# a = [1, 2, 3]
# print(id(a))  # id возвращает идентификатор объекта
# # 140039772293512
# b = a
# print(id(b))
# # 140039772293512
# print(a is b)  # а и b являются один и тем же объектом
# # True
#
# a = [1, 2, 3]
# b = [1, 2, 3]
#
# print(a == b)  # True
# print(a is b)  # False
#
# s = 5
# a = 10
# if a > 0:
#    s = s + a
# else:
#    s = s - a
#
# print(s)

# a = 7
# b = 9 + a
# print("a = F(", b,")")

# a = 15
# if a > 5:
#    a = 5
# a = a + 2
# print(a)

# mx = 0
# s = 0
# x = int(input())
# if x < 0:
#     s = x
#
# b = 7
# b /=b
# if x > mx:
#    mx = x
# print(s)
# print(mx)
# print(b)

# is_rainy = True  # дождь будет
# heavy_rain = False  # не сильный дождь
#
# if is_rainy:
#     # в данный блок дописали ещё один условный оператор
#     if heavy_rain:
#         print("Брать зонт")
#     else:
#         print("Надеть дождевик")
# else:
#     print("Не брать зонт")

#  Задание 13.4.8
try:
   num = int(input("Введите любое целое число"))

except:
       print("Вы ввели неправильное число")
else:
   print(f"Вы ввели {num} ")
finally:
   print('Выход из программы')

# try:
#     age = int(input("How old are you?"))
#     if age > 100 or age <= 0:
#         raise ValueError("Тебе не может быть столько лет")
# except ValueError as error:
#     print(error)
#     print("Неправильный возраст")
# else:
#     print(f"You are {age} years old!") # Возраст выводится только в случае, если пользователь ввёл правильный возраст.