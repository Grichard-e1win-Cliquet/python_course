#task1

# import math
# n = int(input("Enter n: "))

# m = int(input("Enter m: "))

# T = float(m/n)  # (m + n - 1) // n

# print("We neen", math.ceil(T), "days.") 

# task2

# Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# num = int(input('Enter three digit number: '))
# if num // 100 != 0:
#     sum = num % 10 + num // 10 % 10 + num // 100
#     print("The sum of digits of number ", num , 'equals ', sum)
# else:
#     print('Enter three digits number!!!')

#task3
# import math
# a = int(input("How many children in \"A\" class? "))
# b = int(input("How many children in \"B\" class? "))
# c = int(input("How many children in \"C\" class? "))

# # table = print("We need minimum", math.ceil((a+b+c)/2), "tables")
# table = print("We need minimum", ((a+1)//2 + (b+1)//2 + (c+1)//2), "tables")

# task4

# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

# sum = int(input('Enter a total number of paper cranes: '))
# a = b = sum // 6
# c = 4 * a
# print('Peter and Serge makes ',a, 'cranes each, and Kate makes ', c, 'cranes.')

# task5

# a = int(input("In which carriage from the head Michael sat? "))
# b = int(input("Which number has his carriage? "))

# if a == b:
#     print(0)
# else:
#     print("The train has", a+b-1, "carriages")

# task6
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

# ticket = int(input('Enter a number of ticket: '))
# if ticket // 100000 != 0:
#     a = ticket % 1000
#     b = ticket // 1000
#     sumA = a % 10 + a // 10 % 10 + a // 100
#     sumB = b % 10 + b // 10 % 10 + b // 100
#     if sumA == sumB:
#         print('Ticket ',ticket,' is happied.')
#     else:
#         print('Ticket ',ticket,' isn\'t happied.')
# else:
#     print('Enter a number of ticket!')
    
#task7

# year = int(input("Enter the year: "))

# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(f'{year} year is VISKIKUSNIIII!!!!')
# else:
#     print(f'{year} year isnt viskiKOSNII')

# task8

# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

# a = int(input('Enter length of chocolate: '))
# b = int(input('Enter width of chocolate: '))
# c = int(input('Enter how many pieces you want: '))

# if c < a * b and (c % a == 0 or c % b == 0):
#     print('Yes, you can to break off from chocolate ',c, 'pieces with one move.')
# else:
#     print('No, you cannot to break off from chocolate ',c, 'pieces with one move.')

# task9

# решить задачу факториал циклом while 

# n = int(input('Enter a number: '))
# i = 1
# F = 1
# while i < n:
#     i+=1
#     F *=  i
# print(f'Fuctorial from {n} equals {F}.')

# task10

# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

# N = int(input('Enter quantity of coins: '))
# eagle = 0
# face = 0
# for i in range(N):
#     coin = int(input("Enter a side of coin: "))
#     if coin > 0:
#         eagle += 1
#     else:
#         face += 1
# if eagle > face:
#     print(f'Minimum coins to reverse equals {face}')
# else:
#     print(f'Minimum coins to reverse equals {eagle}')

# task11

# Дано А > 1. Определить, каким по счету числом фибоначи является А. Если А не явл-ся числом Фибоначи, выведите -1.

# A = int(input('Enter a number more than 1: '))
# if A > 1:
#     i = 1
#     iP = 0
#     iN = 0
#     n = 2

#     while iN < A:
#         iN = iP + i
#         n += 1
#         iP = i
#         i = iN
#     if iN == A:
#         print(f'The number {A} is {n} number in Fibonacci list.')
#     else:
#         print('-1')
# else:
#     print('More than 1 idiot!')

# task12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3
# import math
# sum = int(input('The sum of two numbers equals: '))
# mp = int(input('The multiplicate of two numbers equals: '))
# D = sum * sum - (4 * mp)
# if D == 0:
#     x1 = sum // 2
#     x2 = x1
#     print(f'Peter think of {x1} and {x2}.')
# elif D > 0:
#     x1 = (sum + math.sqrt(D)) // 2
#     x2 = (sum - math.sqrt(D)) // 2
#     print(f'Peter think of {x1} and {x2}.')
# elif D < 0:
#     print('There is no solution with entered sum and mp.')

# task13

# N = int(input('Enter quantity of days: '))
# count = 0
# max_count = 0
# for i in range(N):
#     temp = int(input("Enter temperature: "))
#     if temp > 0:
#         count += 1
#     else:
#         if max_count < count:
#             max_count = count
#         count = 0
# print(f'Ottepel ebashila maximum {max_count} days.')

# task14
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

# N = int(input('Enter a number: '))
# count = 0
# res = 2 ** count
# print(f'{N} -> ')

# while res <= N:
#     print(res, end=' ')
#     count += 1
#     res = 2 ** count
# print('.')

# task15

# N = int(input('Enter quantity of watermelons: '))
# min = 0
# max = 0
# for i in range(N):
#     waterMelons = int(input("Enter a weight of watermelon: "))
#     if waterMelons > max:
#         max = waterMelons
#     if min == 0:
#         min = waterMelons
#     elif waterMelons < min:
#         min = waterMelons
# print(f'The heaviest watermelon weights {max} kilos, and lightiest weight {min}.')

# task16
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# n = 5
# 1 2 3 4 5
# x = 3

# -> 1
# import random

# A = list()
# n = int(input('Enter quantity of elements in massive: '))
# print('n = ', n)

# for i in range(n):
#     A.append(random.randint(1,10))
# print('Massive A = ', A)

# x = int(input('Enter a number which we going to find: '))
# print('x = ', x)
# count = 0

# for i in range(len(A)):
#     if A[i] == x:
#         count += 1
# print('->', count)

# task17
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# A = input().split()
# for i in range(len(A)):
#     A[i] = int(A[i])

# A = list(map(int, input().split()))
# print(A)
# print(len(set(A))) #делает из списка множество, а во множестве не может быть повторяющихся элементов
# B = list()

# #Вариант решения через создание доп списка
# # for i in A:
# #     if i not in B:
# #         B.append(i)
# # print(B)
# # print(len(B))

# print('The list has',len(set(A)),'different elements')

# task18
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# n = 5
# 1 2 3 4 5
# x = 6
# -> 5

# import random
# import math

# A = list()
# n = int(input('Enter quantity of elements in massive: '))
# print('n = ', n)

# for i in range(n):
#     A.append(random.randint(-10,10))
# print('Massive A = ', A)

# x = int(input('Enter a number which we going to find neariest: '))
# print('x = ', x)

# closest = A[0]
# if x >= A[0]:
#     diff = x - A[0]
# else:
#     diff = A[0] - x

# for i in range(1, len(A)):
#     if x >= A[i]:
#         if x - A[i] <= diff:
#             diff = x - A[i]
#             closest = A[i]
#     else:
#         if A[i] - x <= diff:
#             diff = A[i] - x
#             closest = A[i]
# print('->', closest)

# task19
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –1
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# A = list(map(int, input().split()))
# K = int(input('Enter how many first elements need to move to the end: '))
# print(A)
# # for i in range(K):
# #     A.append(A[0])
# #     A.pop(0)

# K = K % len(A)
# B = list()

# for i in range(K):
#     B.append(A[len(A) - K + i])

# for i in range(len(A) - K):
#     B.append(A[i])
# print(B)

# for i in range(K):
#     A.insert(0, A.pop(-1))

# print(A)

# task20
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# Ввод:
# ноутбук
# Вывод:
# 12

# scrumble = {'A' : '1', 'E' : '1', 'I' : '1', 'O' : '1', 'U' : '1', 'L' : '1', 'N' : '1', 'S' : '1', 'T' : '1', 'R' : '1', 'a' : '1', 'e' : '1', 'i' : '1', 'o' : '1', 'u' : '1', 'l' : '1', 'n' : '1', 's' : '1', 't' : '1', 'r' : '1', 'D' : '2', 'd' : '2', 'G' : '2', 'g' : '2', 
# 'B' : '3', 'b' : '3', 'C' : '3', 'c' : '3', 'M' : '3', 'm' : '3', 'P' : '3', 'p' : '3', 'F' : '4', 'f' : '4', 'H' : '4', 'h' : '4', 'V' : '4', 'v' : '4', 'W' : '4', 'w' : '4', 'Y' : '4', 'y' : '4', 
# 'K' : '5', 'k' : '5', 'J' : '8', 'j' : '8', 'X' : '8', 'x' : '8', 'Q' : '10', 'q' : '10', 'Z' : '10', 'z' : '10', 'А' : '1', 'а' : '1', 'В' : '1', 'в' : '1', 'Е' : '1', 'е' : '1', 'И' : '1','и' : '1', 'Н' : '1', 'н' : '1', 'О' : '1', 'о' : '1', 'Р' : '1', 'р' : '1', 'С' : '1', 'с' : '1', 'Т' : '1', 'т' : '1',
# 'Д' : '2', 'д' : '2', 'К' : '2', 'к' : '2', 'Л' : '2', 'л' : '2', 'М' : '2', 'м' : '2', 'П' : '2', 'п' : '2', 'У' : '2', 'у' : '2', 'Б' : '3', 'б' : '3', 'Г' : '3', 'г' : '3', 'Ё' : '3', 'ё' : '3', 'Ь' : '3', 'ь' : '3', 'Я' : '3', 'я' : '3',
# 'Й' : '4', 'й' : '4', 'Ы' : '4', 'ы' : '4', 'Ж' : '5', 'ж' : '5', 'З' : '5', 'з' : '5', 'Х' : '5', 'х' : '5', 'Ц' : '5', 'ц' : '5', 'Ч' : '5', 'ч' : '5', 'Ш' : '8','ш' : '8', 'Э' : '8', 'э' : '8', 'Ю' : '8', 'ю' : '8', 
# 'Ф' : '10', 'ф' : '10', 'Щ' : '10', 'щ' : '10', 'Ъ' : '10', 'ъ' : '10', ' ' : '0', ' ' : '0'}

# word = input('Enter a word for scrumbling: ')
# score = 0

# for i in word:
#     score += int(scrumble[i])

# print('You earned ',score, 'points.')

# word = input("Enter a world : ").upper()
# dictionary_ENG = {1: "AEIOULNSTR",
#                   2: "DG",
#                   3: "BCMP",
#                   4: "FHVWY",
#                   5: "K",
#                   8: "JZ",
#                  10: "QZ"}
# dictionary_RU = {1: 'АВЕИНОРСТ',
#                  2: 'ДКЛМПУ',
#                  3: 'БГЬЯ',
#                  4: 'ЙЫ',
#                  5: 'ЖЗХЦЧ',
#                  8: 'ШЭЮ',
#                 10: 'ФЩЪ'}
# points = 0
# for key, value in dictionary_ENG.items():
#     for el in value:
#         for i in range(len(word)):
#             if word[i] == el:
#                 points += key
# for key, value in dictionary_RU.items():
#     for el in value:
#         for i in range(len(word)):
#             if word[i] == el:
#                 points += key
# print(points)

# task21
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# dictionary = [ {"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII":"S007"}] 
# print('Original list: ', dictionary)

# newdict = set(val for dic in dictionary for val in dic.values())
# print('Unique values: ', newdict)

# nD = set ()
# for i in dictionary:
#     # print('i = ', i)
#     for j in i:
#         # print('j = ', j)
#         # print('i[j] = ',i[j])
#         nD.add(i[j])
# print(nD)

# # вариант со списками

# dict2 = list()
# for i in dictionary:
#     for j in i:
#         dict2.append(i[j])

# result = list()
# for i in dict2:
#     if i not in result:
#         result.append(i)
# print(result)

# task22
# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
# import random

# n , m = map(int, input('Enter a qunatity of two lists: ').split())
# print('n =',n, 'm =',m)

# a = list()
# b = list()

# for i in range(n):
#     a.append(random.randint(-10,11))
# for i in range(m):
#     b.append(random.randint(-10,11))
# # for i in range(n):
# #     a.append(input('enter a number for first list: '))
# # for i in range(m):
# #     b.append(input('enter a number for second list: '))

# c = set(a).intersection(set(b))
# print(a, b)
# print(c)




# task23
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

# array = [0, -1, 5, 2, 3, 4, 5, 1, 2, -1, 0]
# count = 0
# for i in range(1, len(array)):
# # for i in range(len(array) - 1):
# #     if array[i] < array[i+1]:
#     if array[i] > array[i-1]:
#         count += 1
# print('quantity of numbers more than previous equals: ', count)

# task24

# : В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9

# import random

# n = random.randint(4, 11)
# print('We have',n,'spots with berries.')
# spots = list()

# for i in range(n):
#     spots.append(random.randint(1, 15))
# print(spots)

# max = spots[-2] + spots[-1] + spots[0]

# for i in range(len(spots)-1):
#     if spots[i] + spots[-1] + spots[+1] > max:
#         max = spots[i] + spots[-1] + spots[+1]

# print('Max we could pick from the spots is',max,'kilos')

# task25
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# stroka = 'a b a b a c c a'
# list_1 = list(stroka.split())
# print(list_1)
# print(len(list_1))

# for i in range(len(list_1)):
#     count = 0
#     for j in range(len(list_1)):
#         if list_1[i] == list_1[j]:
#             count += 1
#             if count > 1:
#                 list_1[j] = list_1[j] + '_' + str(count - 1)
#             else:
#                 list_1[j] = list_1[j]

# print(list_1)

# text = input().split()
# text1 = {}
# for i in text:
#     if i in text1:
#         text1[i] += 1
#         print(f'{i}_{text1[i]}', end=' ')
#     else:
#         print(i, end=' ')
#         text1[i] = 0
# print(type(text1))
    
# task26
# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# def step(a,b):
#     if b == 0:
#         return 1
#     else:
#         return a * step(a,b-1)

# x, y = map(int, input().split())
# print(step(x, y))

# task27
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# text = 'She sells sea shells on the sea shore The shells that she sells are sea shells I\'m sure So if she sells sea shells on the sea shore I\'m sure that the shells are sea shore shells'.split()
# count = set()
# words = 0
# for i in text:
#     if i.lower() not in count:
#         count.add(i.lower())
#         words += 1
# print(words)
# print(count)
# print(len(count))

# print(len(set(text.lower().split())))

# task28
# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

# def sum(a,b):
#     if b == 0:
#         return a
#     else:
#         return sum(a+1,b-1)

# x, y = map(int, input().split())
# print(sum(x, y))

# task29

# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих
# слайдах

# Ваня:
# n = int(input())
# max_number = 1000
# while n != 0:
#  n = int(input())
#  if max_number > n:
#  max_number = n
# print(max_number)
# Петя:
# n = int(input())
# max_number = -1
# while n < 0:
#  n = int(input())
#  if max_number < n:
#  n = max_number
# print(n)

#task30
# Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n
#  = a1
#  + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

# a1, diff, quantity = map(int, input('Enter first element, diff and quantity in progression: ').split())
# print(f'an = {a1}', '+ (n - 1) *',quantity)

# list1 = []
# list1.append(a1)

# for i in range(2, quantity + 1):
#     list1.append(a1 + (i - 1) * diff)
# print(list1)

#task 31
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

# def Fibo(n):
#     if n == 0 or n == 1:
#         return n
#     return Fibo(n - 1) + Fibo(n - 2)

# print(Fibo(int(input('Enter a number of Fibonacci: '))))

#task32
# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]


#task 33
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# A = list(map(int, input().split()))
# max = A[0]
# min = A[0]
# # max = max(A)
# # min = min(A)
# for i in range(1, len(A)):
#     if A[i] > max:
#         max = A[i]
#     elif A[i] < min:
#         min = A[i]
# print(max,min)

# for i in range(len(A)):
#     if A[i] == max:
#         A[i] = min
# print(A)

#task35
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# n = int(input('Enter a number: '))

# def prime(n):
#     i = 2
#     flag = True
#     while i < n // 2 + 1 and flag:
#         if n % i == 0:
#             flag = False
#         i += 1
#     if flag:
#         return print(n,'is a natural number.')
#     return print(n,'isnt a natural number.')
# prime(n)

# task37
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# def mass(n):
#     if n == 0:
#         return ''
#     x = int(input())
#     return mass(n - 1) + f' {x}'

# print(mass(int(input())))

#task39
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 
# 3 3 2 12 (каждое число вводится с новой строки)

# list1 = [int(input('Enter a number: ')) for i in range(int(input('Enter quantity of numbers in list: ')))]
# print(list1)
# list2 = [int(input('Enter a number: ')) for i in range(int(input('Enter quantity of numbers in list: ')))]
# print(list2)

# listCross = list()

# for i in range(len(list1)):
#     exist = False
#     if list1[i] not in list2:
#         exist = True
#     if exist:
#         listCross.append(list1[i])
# print(listCross)

#task41
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5 5
# 1 2 3 4 5 1 5 1 5 1
# Вывод: Вывод:
# 0 2
# (каждое число вводится с новой строки)

# list1 = [int(input('Enter a number: ')) for i in range(int(input('Enter a quantity of numbers in list: ')))]
# count = 0
# print(list1)
# for i in range(1, len(list1)-1):
#     if list1[i] > list1[i-1] and list1[i] > list1[i+1]:
#         count += 1
# print(count)

#task43
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: Вывод:
# 1 2 3 2 3 2

# from collections import Counter

# list1 = list(map(int, input('Enter numbers in list separated by space: ').split()))
# print(list1)
# dictionary = Counter(list1)
# count = 0
# for key, values in dictionary.items():
#     if int(values) // 2 >= 1:
#         count += int(values) // 2
# print(count)

# pair = 0
# i = 0
# while i < len(list1):
#     j = i + 1
#     while j < len(list1):
#         if list1[i] == list1[j]:
#             list1.pop(j)
#             list1.pop(i)
#             pair += 1
#             i = 0
#             j = 0
#         j += 1
#     i += 1

# print(pair)

# for i in range(len(list1)-1):
#     for j in range(1, len(list1)):
#         if list1[i] == list1[j]:
#             list1.remove(list1[j])
#             list1.remove(list1[i])
#             i = 0
#             j = 1
# print(list1)

#task45
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: Вывод:
# 300 220 284
# k = False
# while k == False:
#     k = int(input('Enter a number less than 100 000: '))
#     if k > 100000:
#         print('Less than 100 000, idiot!')
#         k = False

# sum1 = 0
# sum2 = 0
# list1 = []

# for i in range(2, k + 1):
#     for j in range(1, i // 2 + 1):
#         if i % j == 0 and sum1+j <= k:
#             sum1 += j
#         if j == i // 2:#- 1:
#             for n in range(1, sum1):
#                 if sum1 % n == 0 and sum2+n < k:
#                     sum2 += n
#             if sum2 == i and sum1 != i and i not in list1 and sum1 not in list1:
#                 print('answer is','i= ',i, 'sum1 = ',sum1)
#                 list1.append(i)
#                 list1.append(sum1)
#     sum1 = 0
#     sum2 = 0

# def list_n(num):
#     summa = 0
#     for i in range(1, num // 2 + 1):
#         if num % i == 0:
#             summa += i
#     return summa

# for i in range(1, k):
#     div_i = list_n(i)
#     for j in range(i + 1, k):
#         div_j = list_n(j)
#         if div_j == i and div_i == j and i != j:
#             print(i,j)

# def div_list(number: int)-> dict:
#     div_dict = {}
#     for j in range(1, number):
#         summa_div = 0
#         for i in range(1, j):
#             if j%i == 0:
#                 summa_div += i
#         div_dict[j] = summa_div
#     return div_dict

# div_dict = div_list(k)

# for i in range(1, k):
#     for j in range(i+1, k):
#         if i == div_dict.get(j) and j == div_dict.get(i): #and i != j:
#             print(i,j)

#task 1461
# import random

# n = int(input('Quantity of balls: '))
# balls = list()
# count = 1
# q = 0
# balls.append(random.randint(0, 9))

# for i in range(1, n):
#     if count < 3:
#         x = random.randint(0, 9)
#         if x == balls[i - 1]:
#             count += 1
#             q = 2
#             balls.append(x)
#         else:
#             count = 1
#             balls.append(x)
#     else:
#         x = random.randint(0, 9)
#         if x != balls[i - 1] or x != balls[i - 2]:
#             balls.append(x)
#         else:
#             i -= 1
#             n += 1
# print(balls)

# if q == 2 and count != 3:
#     while q < 3:
#         for i in range(1, len(balls)):
#             if balls[i] == balls[i - 1]:
#                 q += 1
#                 balls.insert(i, balls[i])
#                 break
# if q == 0:
#     x = random.randint(0, len(balls)-1)
#     balls.insert(x, balls[x])
#     balls.insert(x, balls[x])
# print(balls)

# removed = 0
# for i in range(len(balls) - 2):
#     if len(balls) >= i + 2:
#         if balls[i] == balls[i + 1] == balls[i + 2]:
#             if len(balls) >= i + 3 and balls[i] == balls[i + 3]:
#                 balls.pop(i)
#                 balls.pop(i)
#                 balls.pop(i)
#                 balls.pop(i)
#                 i = 0
#                 removed += 4
#             else:
#                 balls.pop(i)
#                 balls.pop(i)
#                 balls.pop(i)
#                 i = 0
#                 removed += 3
# print(balls)
# print(removed)

#task olimp
# import random

# N = int(input('Enter quantity of numbers in list less than 100: '))
# list1 = [random.randint(-100,101) for i in range(N)]
# print(list1)

# maxN = max(list1)
# minN = min(list1)
# print(maxN,minN)

# minIndex = list1.index(minN)
# maxIndex = list1.index(maxN)
# print(minIndex, maxIndex)

# if maxIndex < minIndex:
#     maxIndex = minIndex
#     minIndex = list1.index(maxN)
# print(minIndex, maxIndex)
# if (maxIndex - minIndex) <= 1:
#     print('Max and min are neibhors.')

# Pr = 1
# for i in range(minIndex + 1, maxIndex):
#     Pr *= list1[i]

# sum = sum(i for i in list1 if i > 0)

# print(sum, Pr)