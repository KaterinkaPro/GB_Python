n = int(input("Введите число элементов:"))
list_1 = [int(input()) for item in range(n)]
list = set(list_1)
print(len(list))
# print(item for item in list_1, sep = '*')