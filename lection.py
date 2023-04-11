""" n = int(input("Введите число элементов:"))
list_1 = [int(input()) for item in range(n)]
list = set(list_1)
print(len(list))
# print(item for item in list_1, sep = '*') """
""" 
def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)


list_1 = []
for i in range(1, 10):
    list_1.append(fib(i))
print(list_1) # [1, 1, 2, 3, 5, 8, 13, 21, 34] """

""" def quicksort(array):
 if len(array) < 2:
 return array
 else:
 pivot = array[0]
 less = [i for i in array[1:] if i <= pivot]
 greater = [i for i in array[1:] if i > pivot]
 return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([10, 5, 2, 3]) """


""" def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
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


list_1 = [1, 5,22,55,12,1]
merge_sort(list_1)
print(list_1) """

#  list  = [1, 2, 3, 5, 8, 15, 23, 38]
# def f(l):
#     out = []
#     for i in list:
#         if i%2 == 0:
#             out.append([i, i*i])
#     return print(out)

# f(list)

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data  = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int,data)
# print(res)
# res = where(lambda x: x%2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)

# list_1 = [x for x in range (1,20)]
# list_1 = list(map(lambda x: x + 10, list_1 ))
# print(list_1)

# data = '1 2 3 5 8 15 23 38'
# data1 = data.split()
# print(data1) # ['1', '2', '3', '5', '8', '15', '23', '38']

# data = list(map(int,data.split()))
# print(data)

# data = [x for x in range(10)]
# res = list(filter(lambda x: x % 2 == 0, data))
# print(res) 

""" #lambda, filter, map, zip, enumerate, list comprehension """

#list comprehension
# a = [i if i%2==0 else 0 for i in range(1,10)]
# print(a)

#enumerate
# a = [0, 2, 0, 4, 0, 6, 0, 8, 0]
# for indx,val in enumerate(a):
#     print(indx,val)

#zip
# a = (1,2,4,5,6)
# b = "abcd"
# f = {45:"b",54:"c",87:"fr"}
# for i in zip(a,b,f.values()):
#     print(i)

#lambda

# def summa(x,y):
#     return x+y

# summa = lambda x,y: x+y if x%2==0 else 0
#
# print(summa(8,6))

#map
# def pow(x):
#     if x%2==0:
#         return 1
#     else:
#         return x
# a = [1,2,3,4,5,6]
# a = list(map(pow, a))
# print(a)

#filter
# a = [1, 2, 3, 4, 5, 6]
# a = list(filter(lambda x: x % 2, a))
# print(a)


#сортировка по ключу

# a = [(1,0,5),(3,0,4),(-5,-1,3),(5,-2,2)]
# maxx = max(a,key=lambda x:x[2])
# print(maxx)

	
print("\tPython")


import pandas as pd








