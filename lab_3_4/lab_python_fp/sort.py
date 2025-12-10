# Задача 4: Сортировка по модулю

def sort_by_abs(data):
    """
    Сортировка списка по модулю в порядке убывания
    
    Args:
        data: список чисел
        
    Returns:
        Отсортированный список
    """
    # Сортировка без использования lambda
    return sorted(data, key=abs, reverse=True)


# Тестовые данные и проверка
if __name__ == '__main__':
    data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]
    
    # Без lambda (с использованием встроенной функции)
    result_without_lambda = sort_by_abs(data)
    
    # С lambda
    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    
    print("Исходный массив:", data)
    print("Без lambda:", result_without_lambda)
    print("С lambda:", result_with_lambda)
    
    # Проверка корректности
    assert result_without_lambda == [123, 100, -100, -30, 30, 4, -4, 1, -1, 0], \
        "Некорректная сортировка без lambda"
    assert result_with_lambda == [123, 100, -100, -30, 30, 4, -4, 1, -1, 0], \
        "Некорректная сортировка с lambda"
    print("\nОба метода работают корректно!")