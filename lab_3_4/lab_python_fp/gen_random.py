# Задача 2: Генератор случайных чисел

import random

def gen_random(num_count, begin, end):
    """
    Генератор случайных чисел в заданном диапазоне
    
    Args:
        num_count: количество случайных чисел
        begin: начало диапазона (включительно)
        end: конец диапазона (включительно)
    
    Yields:
        Случайные числа в заданном диапазоне
    """
    for _ in range(num_count):
        yield random.randint(begin, end)


# Тестовые данные и проверка
if __name__ == "__main__":
    print("Тест 1 - 5 чисел от 1 до 3:")
    for num in gen_random(5, 1, 3):
        print(num, end=' ')
    print()
    
    print("\nТест 2 - 10 чисел от 10 до 20:")
    for num in gen_random(10, 10, 20):
        print(num, end=' ')
    print()
    
    print("\nТест 3 - 3 числа от -5 до 5:")
    for num in gen_random(3, -5, 5):
        print(num, end=' ')
    print()