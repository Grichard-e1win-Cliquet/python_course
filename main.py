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

# task19
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

A = list(map(int, input().split()))
K = int(input('Enter how many first elements need to move to the end: '))
print(A)
for i in range(K):
    A.append(A[0])
    A.pop(0)

print(A)
