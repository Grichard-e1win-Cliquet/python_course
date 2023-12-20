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

# if c % a == 0 or c % b == 0:
#     print('Yes, you can to break off from chocolate ',c, 'pieces with one move.')
# else:
#     print('No, you cannot to break off from chocolate ',c, 'pieces with one move.')