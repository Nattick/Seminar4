# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

a = int(input('Enter first range numbers: '))
b = int(input('enter second range numbers: '))
list_1 = set(map(int, input(f'Enter {a} numbers divided by space: ').split()))
list_2 = set(map(int, input(f'Enter {b} numbers divided by space: ').split()))
a = len(list_1)
b = len(list_2)
list_3 = list_1.intersection(list_2)
print(f'List of unique numbers {sorted(list_3)}')