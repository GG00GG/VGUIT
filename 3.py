# Самое простое решение
def simple_solution():
    print("Введите три целых числа:")
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    
    print("\nЧисла из интервала [1,3]:")
    if 1 <= a <= 3:
        print(a, end=" ")
    if 1 <= b <= 3:
        print(b, end=" ")
    if 1 <= c <= 3:
        print(c, end=" ")
    
    if not (1 <= a <= 3 or 1 <= b <= 3 or 1 <= c <= 3):
        print("нет чисел в интервале [1,3]")

# Запуск простого решения
if __name__ == "__main__":
    simple_solution()
    