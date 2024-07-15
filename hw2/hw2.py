from typing import Callable, List, Tuple
from unittest import result

"""
1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
- перший записує в список нову справу
- другий повертає всі записи
"""
print('TASK1')
def notebook():
    todo_list = []

    def add_todo(todo):
        todo_list.append(todo)
        pass

    def get_all():
        print(todo_list)

    return add_todo, get_all


add, get = notebook()
add('todo hw')
get()
add('todo hw2')
get()


"""
2) протипізувати перше завдання
"""
print('TASK2')
def notebook()-> Tuple[Callable[[str], None], Callable[[],List[str]]]:
    todo_list:List[str] = []

    def add_todo(todo:str)-> None:
        todo_list.append(todo)
        pass

    def get_all()->List[str]:
        print(todo_list)

    return add_todo, get_all


add, get = notebook()
add('todo hw')
get()
add('todo hw2')
get()

"""
3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
expanded_form(12) # return '10 + 2'
expanded_form(42) # return '40 + 2'
expanded_form(70304) # return '70000 + 300 + 4'
"""

print('TASK3')

def expanded_form(number:int)-> str:
    result = []

    num = 1
    for i in range(number):
        digit = number % 10
        if digit != 0:
            result.append(str(digit*num))
        number //= 10
        num *= 10

    return '+'.join(result[::-1])

print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(70304))

"""
4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором, 
та буде виводити це значення після виконання функцій
"""

print('TASK4')


def decorator_task4(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'Викликів{count}')
        func(*args, **kwargs)

    return wrapper


@decorator_task4
def test():
    print('hello')


test()
test()