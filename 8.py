# Вариант 1.  
# 1. 
# Составить программу для вычисления площади разных геометрических 
# фигур.  

from math import pi

def get_area(type):
    if type == 'круг':
        r = int(input())
        area = pi * (r ** 2)
    elif type == 'квадрат':
        a, b = int(input()), int(input())
        area = a * b
    elif type == 'прямоугольный треугольник':
        a, b = int(input()), int(input())
        area = 0.5 * a * b
    
    return area

# 2. 
# Даны 3 различных массива целых чисел (размер каждого не превышает 
# 15). В каждом массиве найти сумму элементов и среднеарифметическое 
# значение.  

def get_sum_and_average(lst):
    return sum(lst), sum(lst)/len(lst)

a = list(range(3, 14))
b = list(range(14))
c = list(range(4, 8))
print(get_sum_and_average(a))
print(get_sum_and_average(b))
print(get_sum_and_average(c))

# Вариант 2. 
# 1. 
# Вычислить площадь правильного шестиугольника со стороной а, 
# используя подпрограмму вычисления площади треугольника.  

from math import sqrt

def get_area(a):
    return (3 * sqrt(3) * (a**2)) / 2

# 2. 
# Пользователь вводит две стороны трех прямоугольников. Вывести их 
# площади.   

def get_area(a, b):
    return a * b
for _ in range(3):
    a, b = int(input()), int(input())
    get_area(a, b)

# Вариант 3.  
# 1. 
# Даны катеты двух прямоугольных треугольников. Написать функцию 
# вычисления длины гипотенузы этих треугольников. Сравнить и вывести какая из 
# гипотенуз больше, а какая меньше.  

from math import sqrt

def hypotenuse(a, b):
    return sqrt(a**2 + b**2)

# 2. 
# Преобразовать строку так, чтобы буквы каждого слова в ней были 
# отсортированы по алфавиту.   

def sort_letters_in_words(s):
    words = s.split()
    sorted_words = [''.join(sorted(word)) for word in words]
    return ' '.join(sorted_words)

text = input()
print(sort_letters_in_words(text))

# Вариант 4.  
# 1. 
# Даны две дроби A/B и C/D (А, В, С, D — натуральные числа). Составить 
# программу деления дроби на дробь. Ответ должен быть несократимой дробью. 
# Использовать подпрограмму алгоритма Евклида для определения НОД.  

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def divide_fractions(A, B, C, D):
    # (A/B) / (C/D) = (A*D) / (B*C)
    num = A * D
    den = B * C

    g = gcd(num, den)
    num //= g
    den //= g

    return num, den

# 2. 
# Задана окружность (x-a)2 + (y-b)2 = R2 и точки Р(р1, р2), F(f1, f1), L(l1,l2). 
# Выяснить и вывести на экран, сколько точек лежит внутри окружности.  
# Проверку, лежит ли точка внутри окружности, оформить в виде процедуры.  

def is_inside_circle(x, y, a, b, R):
    return (x - a)**2 + (y - b)**2 < R**2

a, b, R = map(float, input("Введите a, b, R (окружность): ").split())

p1, p2 = map(float, input("Введите координаты точки P: ").split())
f1, f2 = map(float, input("Введите координаты точки F: ").split())
l1, l2 = map(float, input("Введите координаты точки L: ").split())

count = 0
if is_inside_circle(p1, p2, a, b, R):
    count += 1
if is_inside_circle(f1, f2, a, b, R):
    count += 1
if is_inside_circle(l1, l2, a, b, R):
    count += 1

print(f"Количество точек внутри окружности: {count}")

# Вариант 5.  
# 1. 
# Даны две дроби A/B и C/D (А, В, С, D — натуральные числа). Составить 
# программу вычитания из первой дроби второй. Ответ должен быть 
# несократимой дробью. Использовать подпрограмму алгоритма Евклида для 
# определения НОД.  

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def subtract_fractions(A, B, C, D):
    # A/B - C/D = (A*D - B*C) / (B*D)
    num = A * D - B * C
    den = B * D

    if den < 0:
        num, den = -num, -den

    g = gcd(abs(num), den)
    num //= g
    den //= g

    return num, den

# 2. 
# Напишите программу, которая выводит в одну строчку все делители 
# переданного ей числа, разделяя их пробелами.  

def print_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(str(i))
    print(' '.join(divisors))

print_divisors(int(input()))

# Вариант 6.  
# 1. 
# Составить программу нахождения наибольшего общего делителя (НОД) и 
# наименьшего общего кратного (НОК) двух натуральных чисел НОК(А, В) = 
# (A*B)/НОД(A,B). Использовать подпрограмму алгоритма Евклида для 
# определения НОД.  

def gcd(a, b): # НОД
    while b:
        a, b = b, a % b
    return a

def lcm(a, b): # НОК
    return (a * b) // gcd(a, b)

# 2. 
# Cоставить программу вычисления площади выпуклого четырехугольника, 
# заданного длинами четырех сторон и диагонали.  

def triangle_area(a, b, c): # a, b - длины сторон, c - диагональ
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

# Вариант 7.  
# 1. 
# Даны числа X, Y, Z, Т — длины сторон четырехугольника. Вычислить его 
# площадь, если угол между сторонами длиной X и У — прямой. Использовать 
# две подпрограммы для вычисления площадей: прямоугольного треугольника и 
# прямоугольника.  

def area_triangle(a, b):
    return a * b / 2

def area_rectangle(a, b):
    return a * b

X, Y, Z, T = float(input()), float(input()), float(input()), float(input())

area = area_triangle(X, Y) + area_rectangle(Z, T)
print(f"Площадь четырёхугольника: {area:.2f}")

# 2. 
# Напишите программу, которая переводит переданное ей 
# неотрицательное целое число в 10-значный восьмеричный код, сохранив 
# лидирующие нули.

def to_octal_10digit(n):
    if n < 0:
        raise ValueError("Число должно быть неотрицательным")
    oct_str = oct(n)[2:]  # там 0о
    return oct_str.zfill(10) # с лидирующими нулями

n = int(input())
print(to_octal_10digit(n))
