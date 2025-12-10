# Задача 1: Генератор field

def field(items, *args):
    """
    Генератор для извлечения значений из словарей
    
    Args:
        items: список словарей
        *args: названия полей для извлечения
    
    Yields:
        Если передан один аргумент - значения поля
        Если передано несколько аргументов - словари с указанными полями
    """
    assert len(args) > 0, "Должен быть передан хотя бы один аргумент"
    
    # Если передан один аргумент
    if len(args) == 1:
        key = args[0]
        for item in items:
            if key in item and item[key] is not None:
                yield item[key]
    # Если передано несколько аргументов
    else:
        for item in items:
            result = {}
            has_values = False
            for key in args:
                if key in item and item[key] is not None:
                    result[key] = item[key]
                    has_values = True
            
            if has_values:
                yield result


# Тестовые данные и проверка
if __name__ == "__main__":
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'},
        {'title': None, 'price': 1500, 'color': 'blue'},
        {'price': None, 'color': 'red'},
        {'title': 'Стол', 'price': 3000, 'color': None}
    ]
    
    print("Тест 1 - одно поле 'title':")
    for item in field(goods, 'title'):
        print(item)
    
    print("\nТест 2 - два поля 'title', 'price':")
    for item in field(goods, 'title', 'price'):
        print(item)
    
    print("\nТест 3 - три поля 'title', 'price', 'color':")
    for item in field(goods, 'title', 'price', 'color'):
        print(item)