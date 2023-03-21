""" # Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.

my_str = input()
dict = {}
my_list = my_str.split()
print(my_list)

for i in my_list:
    if i in dict:
        dict[i] += 1
        print(f'{i}_{dict[i]}',end = ' ')
    else: 
        dict[i] = 0
        print(i,end=" ")
print()


# Этот вариант, если нужно split применить обязательно

print('Этот вариант, если нужно split применить обязательно')

my_list = my_str.split()
print(my_list)
for i in range(len(my_list)):
  if my_list.count(my_list[(i + 1) * -1]) > 1:
    my_list[(i + 1) * -1] += f'_{str(my_list.count(my_list[(i + 1) * -1]) - 1)}'

print(my_list)


# Этот вариант больше похож на пример в задании
print('Этот вариант больше похож на пример в задании')

print(my_str)
new_str = ''

for i in range(len(my_str)):
  if my_str[i] != ' ' and my_str.count(my_str[i], 0, i) > 0:
    new_str += f'{my_str[i]}_{my_str.count(my_str[i], 0, i)}'
  else: 
    new_str += my_str[i]

print(new_str) """

# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов. 
# Определите, сколько различных слов содержится в этом тексте.
""" str = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells".lower()
str_2 = str.replace('.', ' ').split()
set_text = set(str_2)
print(set_text)
print(f'{len(set_text)}') """


""" a =  "She sells sea shells on the sea shore;The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore,I'm sure that the shells are sea shore shells."

# for znak in [".", "!", "?", ";", ":", ","]:
#     a = a.replace(znak, " ")
# print(a)  

res = set()
cur_wrd = ""
for letter in a:
    if letter not in ".,? !:;":
        cur_wrd += letter
    else:
        res.add(cur_wrd)
        cur_wrd = ""
print(res)
print(len(res)) """

# “Задана последовательность неотрицательных целых чисел. Требуется определить значение наибольшего элемента
# последовательности, которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”.

""" number_ = int(input())
max_ = number_

while number_ != 0:
    if number_ > max_:
        max_ = number_
    number_ = int(input())
    
print(f'{max_ = }') """



