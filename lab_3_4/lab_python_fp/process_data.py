import json
import sys
from field import field
from unique import Unique
from gen_random import gen_random
from print_result import print_result
from cm_timer import cm_timer_1


path = None


if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = "data_light.json"


with open(path, encoding='utf-8') as f:
    data = json.load(f)


# отсортированный список профессий без повторений
@print_result
def f1(arg):
    return sorted(Unique(field(arg, 'job-name'), ignore_case=True))


# фильтрация программистов
@print_result
def f2(arg):
    # только профессии, начинающиеся со слова "программист"
    return list(filter(lambda x: x.lower().startswith('программист'), arg))


# добавление "с опытом Python"
@print_result
def f3(arg):
    # добавляем к каждой профессии " с опытом Python"
    return list(map(lambda x: f"{x} с опытом Python", arg))


# генерация зарплат
@print_result
def f4(arg):
    # генерируем зарплаты и объединяем с профессиями
    salaries = gen_random(len(arg), 100000, 200000)
    return [f"{profession}, зарплата {salary} руб." for profession, salary in zip(arg, salaries)]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))