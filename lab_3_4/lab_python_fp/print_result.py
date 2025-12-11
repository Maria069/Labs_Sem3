def print_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        # имя функции
        print(func.__name__)
        
        # в зависимости от типа
        if isinstance(result, list):
            for item in result:
                print(item)
        elif isinstance(result, dict):
            for key, value in result.items():
                print(f"{key} = {value}")
        else:
            print(result)
        
        return result
    
    return wrapper
