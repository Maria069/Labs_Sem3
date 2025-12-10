# Задача 6: Контекстные менеджеры для измерения времени

import time
from contextlib import contextmanager


# Способ 1: На основе класса
class cm_timer_1:
    """
    Контекстный менеджер для измерения времени выполнения (реализация на классе)
    """
    
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = time.time() - self.start_time
        print(f"time: {elapsed_time:.1f}")


# Способ 2: С использованием contextlib
@contextmanager
def cm_timer_2():
    """
    Контекстный менеджер для измерения времени выполнения (реализация с contextlib)
    """
    start_time = time.time()
    yield
    elapsed_time = time.time() - start_time
    print(f"time: {elapsed_time:.1f}")


# Тестирование
if __name__ == "__main__":
    print("Тестирование cm_timer_1 (на основе класса):")
    with cm_timer_1():
        time.sleep(1.5)
    
    print("\nТестирование cm_timer_2 (с contextlib):")
    with cm_timer_2():
        time.sleep(0.5)