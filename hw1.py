# Было: ( Задача с суммой цифр числа )
def sum_num(num):
    sum_numbers = 0
    for i in str(num):
        if i != '.':
            sum_numbers += int(i)
    return sum_numbers


n = input("Введите число: ")
print(sum_num(n))

# Стало:( Задача с суммой цифр числа )
b = input("Введите число: ")
sum_lst = list(filter(lambda x: x.isdigit(), b))
res_lst = list(map(int, sum_lst))
print(sum(res_lst))

# Задача с "ликвидацией" слов с "абв" ( изначально использовал лямбду и фильтр )

unmodified_string = 'абв абвгде аваыджолп фываждлыв абвг ввв ааа'.split()
modified_lst = list(filter(lambda e: 'абв' not in e, unmodified_string))
modified_string = ""
for i in range(len(modified_lst)):
    modified_string += modified_lst[i] + " "
print(modified_string)

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции


number = [1, 2, 3, 4, 5, 6, 7, 9]
sum_n = 0
for i in enumerate(number):
    if i[0] % 2 != 0:
        sum_n += i[1]
print(sum_n)

# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.

user_n = int(input())
result_lst = [x for x in range(-user_n, user_n + 1)]
print(result_lst)
a = int(input("Введите а: "))
b = int(input("Введите b: "))
user_mult = result_lst[a] * result_lst[b]
print(user_mult)
