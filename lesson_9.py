# Вариант 1.  
# 1. 
# Вычислить сумму и число положительных элементов матрицы A[N, 
# N], находящихся над главной диагональю.  

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

sum_positive = 0
count_positive = 0

# над - j > i

for i in range(N):
    for j in range(i + 1, N):
        if matrix[i][j] > 0:
            sum_positive += matrix[i][j]
            count_positive += 1

print(count_positive, sum_positive)

# 2. 
# Дана матрица B[N, М]. Найти в каждой строке матрицы 
# максимальный и минимальный элементы и поменять их с первым и 
# последним элементами строки соответственно. 

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    row = matrix[i]
    min_idx = 0
    max_idx = 0
    for j in range(1, M):
        if row[j] < row[min_idx]:
            min_idx = j
        if row[j] > row[max_idx]:
            max_idx = j

    row[0], row[max_idx] = row[max_idx], row[0]

    if min_idx == 0:
        min_idx = max_idx

    row[M - 1], row[min_idx] = row[min_idx], row[M - 1]

for row in matrix:
    print(*row)

# Вариант 2.  
# 1. 
# Дана целая квадратная матрица n-го порядка. Определить, 
# является ли она магическим квадратом, т. е. такой матрицей, в которой 
# суммы элементов во всех строках и столбцах одинаковы.  

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

target = sum(matrix[0])
is_magic = True

for i in range(n):
    if sum(matrix[i]) != target:
        is_magic = False
        break
    
if is_magic:
    for j in range(n):
        col_sum = sum(matrix[i][j] for i in range(n))
        if col_sum != target:
            is_magic = False
            break
        
print('DA' if is_magic else 'NET')

# 2. 
# Дана прямоугольная матрица A[N, N]. Переставить первый и 
# последний столбцы местами и вывести на экран. 

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    matrix[i][0], matrix[i][-1] = matrix[i][-1], matrix[i][0]
    
for row in matrix:
    print(*row)
 
# Вариант 3.  
# 1. 
# Определить, является ли заданная целая квадратная матрица n-го 
# порядка симметричной (относительно главной диагонали).  

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

symmetric = True
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            symmetric = False
            break
    if not symmetric:
        break

print("DA" if symmetric else "NET")

# 2. 
# Дана вещественная матрица размером n х m. Переставляя ее 
# строки и столбцы, добиться того, чтобы наибольший элемент (или один 
# из них) оказался в верхнем левом углу.  

# это на потом

n, m = map(int, input().split())
matrix = [list(map(float, input().split())) for _ in range(n)]

max_val = matrix[0][0]
max_i, max_j = 0, 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] > max_val:
            max_val = matrix[i][j]
            max_i, max_j = i, j

# max_i -> 0
matrix[0], matrix[max_i] = matrix[max_i], matrix[0]

# max_j -> 0
for i in range(n):
    matrix[i][0], matrix[i][max_j] = matrix[i][max_j], matrix[i][0]

for row in matrix:
    print(*row)

# Вариант 4.  
# 1. 
# Дана прямоугольная матрица. Найти строку с наибольшей и строку 
# с наименьшей суммой элементов. Вывести на печать найденные строки и 
# суммы их элементов.  

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

sums = [sum(row) for row in a]
min_sum = min(sums)
max_sum = max(sums)
min_idx = sums.index(min_sum)
max_idx = sums.index(max_sum)

print("Строка с наименьшей суммой:", *a[min_idx], "\nСумма:", min_sum)
print("\nСтрока с наибольшей суммой:", *a[max_idx], "\nСумма:", max_sum)

# 2. 
# Дана квадратная матрица A[N, N], Записать на место 
# отрицательных элементов матрицы нули, а на место положительных — 
# единицы.  
# Вывести на печать нижнюю треугольную матрицу в общепринятом виде. 

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if a[i][j] > 0:
            a[i][j] = 1
        elif a[i][j] < 0:
            a[i][j] = 0

for i in range(n):
    for j in range(n):
        if j <= i:
            print(a[i][j], end=' ')
        else:
            print(' ', end=' ')
    print()
 
# Вариант 5.  
# 1. 
# Упорядочить по возрастанию элементы каждой строки матрицы 
# размером n х m.  

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

for row in matrix:
    row.sort()

for row in matrix:
    print(*row)

# 2. 
# Дана действительная матрица размером n х m, все элементы 
# которой различны. В каждой строке выбирается элемент с наименьшим 
# значением. Если число четное, то заменяется нулем, нечетное - 
# единицей. Вывести на экран новую матрицу.  

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    min_value = min(a[i])
    for j in range(n):
        if A[i][j] == min_value:
            A[i][j] = 0 if min_value % 2 == 0 else 1
            break
        
for row in a:
    print(*row)
# Вариант 6.  
# 1. 
# Дана целочисленная квадратная матрица. Найти в каждой строке 
# наибольший элемент и в каждом столбце наименьший. Вывести на 
# экран.  

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

row_max = [max(row) for row in a]
col_min = [min(a[i][j] for i in range(n)) for j in range(n)]

print(*row_max)
print(*col_min)

# 2. 
# Дана действительная квадратная матрица порядка N (N — 
# нечетное), все элементы которой различны. Найти наибольший элемент 
# среди стоящих на главной и побочной диагоналях и поменять его 
# местами с элементом, стоящим на пересечении этих диагоналей.  

# N — нечётное -> центр: (N//2, N//2) 

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

diag_elements = []

for i in range(n):
    diag_elements.append((a[i][i], i, i))
    if i != n - 1 - 1:
        diag_elements.append((a[i][n-1-i], i, n-1-i))
        
max_value, max_i, max_j = max(diag_elements, key=lambda x: x[0])
center = n // 2

a[max_i][max_j], a[center][center] = a[center][center], a[max_i][max_j]
for row in a:
    print(*row)

# Вариант 8.  
# 1. 
# Задана матрица порядка n и число к. Разделить элементы k-й 
# строки на диагональный элемент, расположенный в этой строке.

n = int(input())
k = int(input('Введите число с 1 (1я строка, 2я строка и т.д.): ')) - 1
a = [list(map(int, input().split())) for _ in range(n)]

diag_elem = a[k][k]
if diag_elem != 0:
    for j in range(n):
        a[k][j] /= diag_elem
        
for row in a:
    print(*row)

# 2. 
# Задана квадратная матрица. Получить транспонированную 
# матрицу (перевернутую относительно главной диагонали) и вывести на 
# экран.  

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

translated = [[a[j][i] for j in range(n)] for i in range(n)]

for row in translated:
    print(*row)
