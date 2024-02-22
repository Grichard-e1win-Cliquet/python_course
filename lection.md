# list_1 = []
# list_2 = list()
# list_3 = [1, 2, 3, 4, 5]
# print(*list_3)

# for i in list_3:
#     print(i)

# print(len(list_3))

# list_1 = [1, 5]
# print(list_1)
# list_1.append(8)
# print(list_1)
# list_1.append(85)
# print(list_1)
# list_1.pop()
# print(list_1)
# list_1.pop(0)
# print(list_1)
# list_1.insert(0, 11)
# print(list_1)

# list = []
# print(list)
# for i in range(5):
#     list.append(i)
#     print(list)

# Срез списка
# Помните в конце первой лекции Вы прошли срезы строк? Также существует срез списка,
# давайте научимся изменять наш список
# ● Отрицательное число в индексе — счёт с конца списка
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0]) # 1
# print(list_1[1]) # 2
# print(list_1[len(list_1)-1]) # 10
# print(list_1[-5]) # 6
# print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2]) # [1, 2]
# print(list_1[len(list_1)-2:]) #[9, 10]

# print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
# print(list_1[6:-18]) # []
# print(list_1[0:len(list_1):6]) # [1, 7] c шагом 6
# print(list_1[::6]) # [1, 7] то же самое

# Кортеж — это неизменяемый список.
# Тогда для чего нужны кортежи, если их нельзя изменить? В случае защиты каких-либо
# данных от изменений (намеренных или случайных). Кортеж занимает меньше места в
# памяти и работают быстрее, по сравнению со списками
# t = () # создание пустого кортежа
# print(type(t)) # class <'tuple'>
# t = (1,)
# print(type(t))
# t = (1)
# print(type(t))
# t = (28, 9, 1990)
# print(type(t))

# Можно распаковать кортеж в независимые переменные:
# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))# r:red g:green b:blue

# t = (1, 2, 3, 5,)
# print(t[1])
# for i in range(len(t)):
#     print(t[i])

# Словари
# Словари — неупорядоченные коллекции произвольных объектов с доступом по ключу.
# В списках в качестве ключа используется индекс элемента. В словаре для определения
# элемента используется значение ключа (строка, число).
# d = {}
# d = dict()

# d['q'] = 'qwerty'
# print(d)

# d['w'] = 'werty'
# print(d)

# d.update({'four': 4, 'five': 5})
# print(d.get('four'))

# dictionary = {}
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ← типы ключей могут отличаться
# print(dictionary['up']) # ↑ типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# dictionary.pop['left'] # удаление элемента
# print(d.keys())
# print(d.values())

# for i in dictionary:
#     # print(i)
#     print('{}: {}'.format(i, dictionary[i]))

# for (k,v) in dictionary.items():
#     print(k, v)

# dict1 = {'Tom': {'English': 5, 'Math': 5}, 'Red': {'English': 4, 'Math': 4}}

# print(dict1)
# for i in dict1['Tom'].items():
#    print(*i)

# print(dict1['Red']['Math'])

# d.update({'Wer': {'English': 3, 'Math': 4})
# dict1['Tom'].update({'Work': 6})
# dict1['Red']['Math'] = 5


# Множества
# Множества содержат в себе уникальные элементы, не обязательно упорядоченные.
# Одно множество может содержать значения любых типов. Если у Вас есть два множества,
# Вы можете совершать над ними любые стандартные операции, например, объединение,
# пересечение и разность. Давайте разберем их.
# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# colors.clear()
# print(colors)

# q = set()

# Операции со множествами в Python:
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a.union(b).difference(a.intersection(b))# {1, 21, 3, 13}

# a = {1, 8 ,6 }
# b = frozenset(a)

# List Comprehension
# У каждого языка программирования есть свои особенности и преимущества. Одна из
# культовых фишек Python — list comprehension (редко переводится на русский, но можно
# использовать определение «генератора списка»). Comprehension легко читать, и их
# используют как начинающие, так и опытные разработчики. List comprehension — это
# упрощенный подход к созданию списка, который задействует цикл for, а также инструкции
# if-else для определения того, что в итоге окажется в финальном списке.
# 1. Простая ситуация — список:
# list_1 = [exp for item in iterable]
# 1. Выборка по заданному условию:
# list_1 = [exp for item in iterable (if conditional)]

# Создать список, состоящий из четных чисел в диапазоне от 1 до 100.
# Решение:
# 1. Создать список чисел от 1 до 100
# list_1 = []
# for i in range(1, 101):
#     list_1.append(i)
# print(list_1) # [1, 2, 3,..., 100]
# Эту же функцию можно записать так:
# list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]
# print(list_1) # [1, 2, 3,..., 100]

# Добавить условие (только чётные числа)
# list_1 = [i for i in range(1, 101) if i % 2 == 0]# [2, 4, 6,..., 100]
# Допустим, вы решили создать пары каждому из чисел (кортежи)
# list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]# [(2, 2), (4, 4),..., (100, 100)]
# Также можно умножать, делить, прибавлять, вычитать. Например, умножить значение на 2.
# list_1 = [i * 2 for i in range(10) if i % 2 == 0]
# print(list_1) # [0, 4, 8, 12, 16]

#   Функции, рекурсия, алгоритмы.

def sum_numbers(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print (sum)
    return sum
a = sum_numbers(5)
print(a)

def sum_str(*args):
    res = ''
    for i in args:
        res += i
    return res
print(sum_str('q', 'e', 'r'))

import module1 as m1
from modul1 import max1

def fib(n):
    if n in [1,2]:
        return 1
    return fib(n-1) + fib(n-2)

list_1 = []
for i in range (1, 10):
    list_1.append(fib(i))
print(list_1)

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    more = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot]+ quick_sort(more)
print (quick_sort([14,5,9,6,3,58,7,5,2,7]))

def merge_sort(nums):
    if len(nums) > 1:
        mid len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
list1 = [1,5,6,9,8,7,2,1,55,2,4]
merge_sort(list1)
print(list1)

def f(x):
    return x*x
a = f
print(f(5))

def calk1(a):
    return a+a
# calk1 = lambda a,b: a + b

def calk2(a):
    return a*a

def math(op, x):
    print(op(x))

math(calk1, 5)

colors = ['red', 'green', 'blue']
data = open('file.txt', 'a') # указываем режим работы
data.writelines(colors) # разделителей не будет
data.close()

with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')

path = 'file.txt'
data = open('file.txt', 'r')
for line in data:
    print(line)
data.close()
