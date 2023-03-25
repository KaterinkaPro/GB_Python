#Последовательностью Фибоначчи называется последовательность чисел a0 , a1, ..., an, ..., где a0 = 0, a1 = 1, ak= ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи 

""" def fib(n):
    if n == 1 or n == 0:
        return 1
    return fib(n-1)+fib(n-2)

n = int(input())
print(fib(n))
 """

# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на 
# # максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
Проверить встроенныее функции листа мин и макс

""" def change(arg):
    min = arg[0]
    max = arg[0]
    for i in arg:
        if i < min:
            min = i
        elif i > max:
            max = i
    for i in range(len(arg)):
        if arg[i]==max:
            arg[i] = min
    return arg

n = int(input("Введите количество элементов:"))
arg = [int(input()) for i in range(n)]
print(arg)
print(change(arg)) """

# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым # Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число) 

""" def is_simple(n):
    # count = 0
    # for i in range(1,n+1):
    #     if n % i == 0:
    #         count +=1
    # return count == 2 ##вариант2
    # return len([i for i in range(1, n+1) if n % i == 0]) == 2 
    for i in range(2,n):
        if n%i==0:
            return ("No")
    else:
        return ("Yes")

n = int(input())
print(is_simple(n)) """



# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

""" def rec(n):
    a = input()
    if n == 1:
        return a
    return(rec(n-1)) + a

N = int(input())
print(rec(N)) """