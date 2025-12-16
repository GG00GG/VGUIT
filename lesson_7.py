# Вариант 1   
# Дан одномерный массив, состоящий из N целочисленных элементов. 
# 1.
# Ввести массив с клавиатуры. Найти максимальный элемент. Вывести массив на 
# экран в обратном порядке.   

lst = [int(n) for n in input().split(',')]
print(max(lst), lst.reverse())

# 2. 
# В массиве действительных чисел все нулевые элементы заменить на 
# среднее арифметическое всех элементов массива.   

lst = [int(n) for n in input().split(',')]
average = sum(lst) / len(lst)
lst = [average if n == 0 else n for n in lst]

# Вариант 2   
# 1. 
# Дан одномерный массив, состоящий из N целочисленных элементов. 
# Ввести массив с клавиатуры. Найти минимальный элемент. Вывести индекс 
# минимального элемента на экран.   

lst = [int(n) for n in input().split(',')]
print(min(lst), lst.index(min(lst)))

# 2. 
# Дан массив целых чисел. Переписать все положительные элементы во 
# второй массив, а остальные - в третий.   

lst = [int(n) for n in input().split(',')]
positive = []
negative = []

for n in lst:
    if n > 0: positive.append(n)
    else: negative.append(n)

# Вариант 3   
# 1. 
# В одномерном числовом массиве D длиной n вычислить сумму элементов 
# с нечетными индексами. Вывести на экран массив D, полученную сумму.   

lst = [int(n) for n in input().split(',')]
total = 0

for n in lst:
    if lst.index(n) % 2 == 1:
        total += n
        
print(lst, total)

# 2. 
# Дан одномерный массив из 8 элементов. Заменить все элементы массива 
# меньшие 15 их удвоенными значениями. Вывести на экран монитора 
# преобразованный массив.   

lst = [1, 2, 6, 8, 134, 15132, -143, 15]
lst = [n * 2 if n < 15 else n for n in lst]
print(lst)

# Вариант 4   
# 1. 
# Дан массив целых чисел. Найти максимальный элемент массива и его 
# порядковый номер.   

lst = [int(n) for n in input().split(',')]
print(max(lst), lst.index(max(lst)))

# 2. 
# Дан одномерный массив целого типа. Получить другой массив, состоящий 
# только из нечетных чисел исходного массива или сообщить, что таких чисел нет. 
# Полученный массив вывести в порядке убывания элементов.   

lst = [int(n) for n in input().split(',')]
new = []

for n in lst:
    if n % 2 == 1:
        new.append(n)

if len(n) == 0:
    print('Таких чисел нет')
else:
    new.sort()
    new.reverse()
    print(new)

# Вариант 5   
# 1. 
# Дан одномерный массив из 10 целых чисел. Вывести пары отрицательных 
# чисел, стоящих рядом.   

lst = [-1, -2, 3, 5, -4, 7, -8, 10, -20, -21]
count = 0

while count < len(lst)-1:
    if lst[count] < 0 and lst[count+1] < 0:
        print(lst[count], lst[count+1])
    count += 1

# 2. 
# Дан целочисленный массив размера 10. Создать новый массив, удалив 
# все одинаковые элементы, оставив их 1 раз. 

lst = [-1, -2, 3, 5, -4, 7, -8, 10, -20, -21]
for n in lst:
    count = lst.count(n)
    if count > 1: lst.remove(n)
    
print(lst)


# Вариант 6   
# 1. 
# Дан одномерный массив из 10 целых чисел. Найти среднеарефметическое 
# и сравнить с ним остальные элементы. Вывести количество меньших 
# максимального и больших среднеарефметического.   

lst = [-1, -2, 3, 5, -4, 7, -8, 10, -20, -21]
average = sum(lst) / len(lst)
sta = 0
bta = 0

for n in lst:
    if n < average: sta += 1
    elif n > average: bta += 1
    
print(sta, bta)

# 2. 
# Одномерный массив из 10-и целых чисел заполнить с клавиатуры, 
# определить сумму тех чисел, которые >5.   

lst = [int(input()) for _ in range(10)]
total = 0

for n in lst:
    if n > 5: total += n
    
print(total)

# Вариант 7   
# 1. Дан массив целых чисел. Найти сумму элементов с четными номерами и 
# произведение элементов с нечетными номерами. Вывести сумму и 
# произведение.   

lst = [int(n) for n in input().split(',')]
total = 0
mult = 0

for n in lst:
    if lst.index(n) % 2 == 0: total += n
    else:
        if mult == 0:
            mult = n
        else: mult *= n
        
print(mult, total)

# 2. Переставить в одномерном массиве минимальный элемент и максимальный.   
lst = [int(n) for n in input().split(',')]
index_min = lst.index(min(lst))
index_max = lst.index(max(lst))

min_n, max_n = min(lst), max(lst)

lst[index_min] = max_n
lst[index_max] = min_n
