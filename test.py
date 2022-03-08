
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
# try:
#    num = int(input("Введите любое целое число"))
#
# except:
#        print("Вы ввели неправильное число")
# else:
#    print(f"Вы ввели {num} ")
# finally:
#    print('Выход из программы')

# try:
#     age = int(input("How old are you?"))
#     if age > 100 or age <= 0:
#         raise ValueError("Тебе не может быть столько лет")
# except ValueError as error:
#     print(error)
#     print("Неправильный возраст")
# else:
#     print(f"You are {age} years old!")

# A = int(input("Введите любое целое число \n"))
# B = int(input("Введите любое целое число \n"))
# # def are_both_odd(A, B):
# if not (not (A % 2 != 0) and not (B % 2 != 0)):
#    print("Числа А и B нечетные")
# else:
#    print('Числа А и B четные')
# Что то не выводит результат(((


# if 6 <= 7 < 12:
#     print("Утро!!!")
# a = int(input("Введите число"))
# if a == 10:
#     print('a равно 10')
# elif a < 10:
#     print('a меньше 10')
# else:
#     print('a больше 10')

spees = 20
# def get_wind_class(speed):
#     if 0 < spees < 5:
#         return"weak [1]"
#     elif 4 < spees <= 10:
#         return"moderate [2]"
#     elif 10 < spees <= 18:
#         return "strong [3]"
#     elif 18 < spees:
#         return "hurricane [4]"
# print(get_wind_class(3))
# Не работает, выдает при любой цифре только первую
# переменную speed на x все пошло. Почему? а поменял на
# spees то же работает. Может зарезервированное

# user_database = {
#     'user': 'password',
#     'iseedeadpeople': 'greedisgood',
#     'hesoyam': 'tgm'
# }
# def check_user(username, password):
#     if username in user_database:
#         if password == user_database[username]:
#             return True
#         else:
#             return False
#     else:
#         return False
#
# a = 42
# b = 41
# result = a if a > b else b
# print(result)
#
# x = input("Ввод числа")
# print("Результат " + str(x))

# x = int(x)
# if x == 0:
#     print('if')
# elif x > 0:
#     print('elif')
# else:
#     print('else')
#
# if x== 0:
#     x += 1
#     print(x)
# else:
#     x -= 1
#     print(x)


# x = input("Ввод числа")
#
# if x == 0:
#     x = 1
#     print('x = zerro')
# elif type(x) == type(5) or type(x) == type(5.5):
#     print('OK')
# else:
#     print('No numer')
#     x = 1
#
# print(100/x)
# A = int(input('Введите первое число\n'))
# B = int(input('Введите второе число\n'))
# C = int(input('Введите третье число\n'))

# print(list(range(1, 5)))
# [1, 2, 3, 4]
# print(list(range(1, 10, 2)))
# [1, 3, 5, 7, 9]

# S = 1  # заводим переменную-счетчик, в которой мы будем считать сумму
# N = 5
#
# # заводим цикл for, в котором мы будем проходить по всем числам от одного до N
# for i in range(1, N+1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
#     print("Значение суммы на предыдущем шаге: ", S)
#     print("Текущее число: ", i)
#     S *= i  # cуммируем текущее число i и перезаписываем значение суммы
#     print("Значение суммы после сложения: ", S)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: сумма равна = ", S)

# P = 1  # заводим переменную-счетчик, в которой мы будем считать произведение
# N = 5
#
# # запишите цикл for для подсчета произведения
# for i in range(1, N+1):
#     P *= i
#
# print(P)

# N = 5
#
# for i in range(1, N + 1):
#    print("*" * i)

# S = 2  # заводим переменную-счетчик, в которой мы будем считать сумму
# n = 1  # текущее натуральное число

# заводим цикл while, который будет работать, пока сумма не превысит 500
# while n ** 2 < 1000:  # делай пока ...
#     # S *= n # увеличиваем сумму, равносильно S = S + n
#     n += 1  # так как сумма ещё не достигла нужного значения, то увеличиваем переменную-счетчик
#     print("Ещё считаю ...", n)
#
# # print("Сумма равна: ", S)
# print("Количество чисел: ", n)

# random_matrix = [
#     [9, 2, 1],
#     [2, 5, 3],
#     [4, 8, 5]
# ]
#
# mean_value_rows = []  # здесь будут храниться средние значения для каждой строки
# min_value_rows = []  # здесь будут храниться минимальные значения для каждой строки
# min_index_rows = []  # здесь будут храниться индексы минимальных значений для каждой строки
# max_value_rows = []  # здесь будут храниться максимальные значения для каждой строки
# max_index_rows = []  # здесь будут храниться индексы максимальных значений для каждой строки
#
# for row in random_matrix:  # здесь мы целиком берем каждую сроку
#     min_index = 0  # в качестве минимального значения возьмем первый элемент строки
#     max_index = 0
#     min_value = row[min_index]  # начальное минимальное значение для каждой строки будет новое
#     max_value = row[max_index]  # для максимального значения тоже самое
#     for index_col in range(len(row)):
#         if row[index_col] < min_value:
#             min_value = row[index_col]
#             min_index = index_col
#         if row[index_col] > max_value:
#             max_value = row[index_col]
#             max_index = index_col
#     min_value_rows.append(min_value)
#     min_index_rows.append(min_index)
#     max_value_rows.append(max_value)
#     max_index_rows.append(max_index)
#
# print(min_value_rows)
# print(min_index_rows)
# print(max_value_rows)
# print(max_index_rows)

# list_ = [-5, 2, 4, 8, 12, -7, 5]
#
# for i in range(len(list_)):  # равносильно выражению for i in [0, 1, 2, 3, 4, 5, 6]:
#     print("Индекс элемента: ", i)
#     print("Значение элемента: ", list_[i])  # с помощью индекса получаем значение элемента
#     print("---")
# print("Конец цикла")

# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Функция enumerate возвращает данные в виде кортежей,
# # где на первом месте стоит индекс, а затем значение
# # [(0, -5), (1, 2), (2, 4), ...]
# for i, value in enumerate(list_):
#     print("Индекс элемента: ", i)
#     print("Значение элемента: ", value)  # с помощью индекса получаем значение элемента
#     print("---")
# print("Конец цикла")

# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Объявим переменную, в которой будем хранить индекс отрицательного элемента
# index_negative = None
#
# for i, value in enumerate(list_):
#     if list_[i] < 0:
#         print("Отрицательное число: ", list_[i])
#         index_negative = i  # перезаписываем значение индекса
#         print("Новый индекс отрицательного числа: ", index_negative)
#     else:
#         print("Положительное число: ", list_[i])
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: индекс последнего отрицательного элемента = ", index_negative)

# text = """
# У лукоморья дуб зелёный;
# Златая цепь на дубе том:
# """
#
# text = text.lower()
# text = text.replace(" ", "")
# text = text.replace("\n", "")
# print(text)
# count = {}  # для подсчета символов и их количества
# for char in text:
#    if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
#        count[char] += 1
#    else:
#        count[char] = 1
# for char, cnt in count.items():
#    print(f"Символ {char} встречается {cnt} раз")

# n = int(input("Введите число\n"))

# while True:
#     if n % 2 != 0:
#         n = (n * 3 + 1) // 2
#     else:
#         n = n // 2
#     print(n)
#
#     if n == 1:
#         print("Done")
#         break

# heads = 35  # количество голов
# legs = 94  # количество ног

# for r in range(heads + 1):  # количество кроликов
#     for ph in range(heads + 1):  # количество фазанов
#         #  если суммарное количество голов превышено или ног превышено, то переходим на следующий шаг цикла
#         if (r + ph) > heads or \
#             (r * 4 + ph * 2) > legs:
#             continue
#         if (r + ph) == heads and (r * 4 + ph * 2) == legs:
#             print("Количество кроликов", r)
#             print("Количество фазанов", ph)
#             print("---")
# some_var = (2,)
# if some_var is None:
#     print("NoneType")
# else:
#     print(type(some_var))

# squares = [(i, i**2) for i in range(1,11) if i % 2 == 1]
# print(squares)
#
# M = [[i+j for j in range(5)] for i in range(5)]
# print(M)
#
# T = [[i*j for j in range(1,11)] for i in range(1,11)]
# print(T)

# L = [int(input()) % 2 == 0 for i in range(5)]
# print(any(L))

N = int(input("ведите необходимое колличество билетов = "))
# #
result = 0  # и результирующую строку
# #
# #
# if N > 0: # если количество посетителей еще больше нуля,
for i in range(1, N+1):
    age = int(input("ведите возраст посетителя номер " + str(i) + "- "))
    if 18 <= age < 25:
      result += 990
    elif age >= 25:
      result += 1390
# N -= 1  # то уменьшаем  счетчик
print("сумма к оплате - ", result)
# else:
#     N == 0   # иначе - записываем в результат



# age = int(input())

# if 18 <= age < 25:
#     result += 990
# elif age >= 25:
#     result += 1390
# print(result)

# print("setvberbte = " + str(N))
