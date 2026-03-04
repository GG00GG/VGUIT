# Задание А.1: Вычисление x^n / n!
def task_a1(x, n):
    def power(x, n):
        if n == 0:
            return 1
        return x * power(x, n - 1)
    
    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n - 1)
    
    return power(x, n) / factorial(n)

# Задание А.2: Остаток от деления a на b
def task_a2(a, b):
    if a < b:
        return a
    return task_a2(a - b, b)

# Задание А.3: Вывести число в обратном порядке
def task_a3(n):
    def reverse_num(n, rev=0):
        if n == 0:
            return rev
        return reverse_num(n // 10, rev * 10 + n % 10)
    
    if n == 0:
        return 0
    return reverse_num(n)

# Задание А.4: Сумма цифр числа
def task_a4(n):
    if n == 0:
        return 0
    return n % 10 + task_a4(n // 10)

# Задание А.5: Вывести цифры числа в обратном порядке
def task_a5(n):
    if n < 10:
        print(n, end=" ")
        return
    print(n % 10, end=" ")
    task_a5(n // 10)

# Задание А.6: Проверка на простоту
def task_a6(n):
    def is_prime(n, divisor=2):
        if n <= 2:
            return n == 2
        if n % divisor == 0:
            return False
        if divisor * divisor > n:
            return True
        return is_prime(n, divisor + 1)
    
    return "YES" if is_prime(n) else "NO"

# Задание А.7: Вывод чисел от A до B
def task_a7(a, b):
    if a == b:
        print(a)
        return
    print(a, end=" ")
    if a < b:
        task_a7(a + 1, b)
    else:
        task_a7(a - 1, b)

# Демонстрация работы блока А
def demo_block_a():
    print("=== БЛОК А ===")
    print("А.1: 2^5 / 5! =", task_a1(2, 5))
    print("А.2: 17 % 5 =", task_a2(17, 5))
    print("А.3: 12345 в обратном порядке =", task_a3(12345))
    print("А.4: Сумма цифр 12345 =", task_a4(12345))
    print("А.5: Цифры 12345 в обратном порядке: ", end="")
    task_a5(12345)
    print("\nА.6: 17 простое? -", task_a6(17))
    print("А.7: Числа от 10 до 5: ", end="")
    task_a7(10, 5)

    # Задание Б.1: Максимум последовательности
def task_b1():
    num = int(input("Введите число (0 для окончания): "))
    if num == 0:
        return 0
    next_max = task_b1()
    if next_max == 0:
        return num
    return num if num > next_max else next_max

# Задание Б.2: Второй по величине элемент
def task_b2():
    def find_second():
        num = int(input("Введите число (0 для окончания): "))
        if num == 0:
            return 0, 0
        
        max1, max2 = find_second()
        
        if num > max1:
            return num, max1
        elif num > max2:
            return max1, num
        else:
            return max1, max2
    
    _, second = find_second()
    return second

# Задание Б.3: Вывод каждого второго элемента
def task_b3():
    def print_odd_positions(pos=1):
        num = int(input("Введите число (0 для окончания): "))
        if num == 0:
            return
        
        if pos % 2 == 1:
            print(num)
        
        print_odd_positions(pos + 1)
    
    print_odd_positions()

# Задание Б.4: Проверка на простоту со сложностью O(logn)
def task_b4(n):
    def is_prime_optimized(n, divisor):
        if n <= 2:
            return n == 2
        if n % divisor == 0:
            return False
        if divisor * divisor > n:
            return True
        # Увеличиваем шаг для оптимизации
        next_div = divisor + (2 if divisor > 2 else 1)
        return is_prime_optimized(n, next_div)
    
    return "YES" if is_prime_optimized(n, 2) else "NO"

# Демонстрация работы блока Б
def demo_block_b():
    print("\n=== БЛОК Б ===")
    print("\nБ.1: Найти максимум последовательности")
    print("Максимум:", task_b1())
    
    print("\nБ.2: Найти второй максимум")
    print("Второй максимум:", task_b2())
    
    print("\nБ.3: Вывод каждого второго числа")
    task_b3()
    
    print("\nБ.4: Проверка на простоту (оптимизированная)")
    num = int(input("Введите число для проверки: "))
    print(task_b4(num))

def main():
    # Выбор блока для демонстрации
    print("Выберите блок для демонстрации:")
    print("1 - Блок А")
    print("2 - Блок Б")

    choice = input("Ваш выбор: ")

    if choice == "1":
        demo_block_a()
    elif choice == "2":
        demo_block_b()
    else:
        print("Неверный выбор!")

if __name__ == "__main__":
    main()