# Задача 3: Итератор Unique для удаления дубликатов

class Unique(object):
    """
    Итератор для удаления дубликатов из последовательности
    
    Args:
        items: последовательность (список, генератор и т.д.)
        ignore_case: игнорировать регистр для строк (по умолчанию False)
    """
    
    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            item = next(self.items)
            
            # Обработка с учетом ignore_case
            if isinstance(item, str) and self.ignore_case:
                key = item.lower()
            else:
                key = item
            
            if key not in self.seen:
                self.seen.add(key)
                return item


# Тестовые данные и проверка
if __name__ == "__main__":
    print("Тест 1 - числа с дубликатами:")
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    for item in Unique(data1):
        print(item, end=' ')
    print()
    
    print("\nТест 2 - строки без учета регистра:")
    data2 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    for item in Unique(data2, ignore_case=True):
        print(item, end=' ')
    print()
    
    print("\nТест 3 - строки с учетом регистра:")
    data3 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    for item in Unique(data3):
        print(item, end=' ')
    print()
    
    print("\nТест 4 - с генератором:")
    from gen_random import gen_random
    data4 = gen_random(10, 1, 3)
    for item in Unique(data4):
        print(item, end=' ')
    print()