"""
1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
наприклад:
st = 'as 23 fdfdg544' введена строка
2,3,5,4,4        #вивело в консолі.
"""

str1 = 'fjajf 11 a2v3'
num2 = [i for i in str1 if i.isdigit()]
print(num2)
print(','.join(num2))


"""
2)написати прогу яка вибирає зі введеної строки числа і виводить їх 
так як вони написані
наприклад:
  st = 'as 23 fdfdg544 34' #введена строка
  23, 544, 34              #вивело в консолі
  """

str2 = 'fjajf 111 a22v3'
num3 = ','.join(''.join(i if i.isdigit() else ' ' for i in str2).split())
print(num3)


"""
1)є строка:
greeting = 'Hello, world'
записати кожний символ як окремий елемент списку і зробити його заглавним:
['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
"""

greeting = 'Hello, world'
def task_list1(input):
    split1 = [i.upper() for i in input]
    return split1

print(task_list1(greeting))

"""
2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
приклад:
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
"""

arr = [i for i in range(0,50)]
def task_list2(input):
    arr_odd = []
    for i in input:
        if(i % 2 != 0):
            arr_odd.append(i**2)
    return arr_odd

print(task_list2(arr))


"""
- створити функцію яка виводить ліст
"""

def task_func1(a,b,c):
    list = [a,b,c]
    return list

print(task_func1(1,'afk','a'))


"""
- створити функцію яка приймає три числа та виводить та повертає найбільше.
"""
def task_func2(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c and b>a):
        return b
    else:
        return c

print(task_func2(20,10,3))


"""
- створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
"""
def task_func3(*args):
    min_val = min(args)
    max_val = max(args)

    return f"Min-{min_val} \nMax-{max_val}"

print(task_func3(1,2,3,4,5,6,7))


"""
- створити функцію яка повертає найбільше число з ліста
"""

def task_func4(list):
    return max(list)

print(task_func4([1,10,3,4]))

"""
- створити функцію яка повертає найменьше число з ліста
"""
def task_func5(list):
    return min(list)

print(task_func5([1,10,3,4]))

"""
- створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
"""
def task_func6(list):
    result = sum(list)
    return result

print(task_func6([1,2,3,4,5]))


"""
- створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
"""

def task_func7(list):
    result = sum(list) / len(list)
    return result

print(task_func7([1,2,3,4,5]))


"""
1)Дан list:
  list = [22, 3,5,2,8,2,-23, 8,23,5]
  - знайти мін число
  - видалити усі дублікати
  - замінити кожне 4-те значення на 'X'
"""


def find_min(input):
    return min(input)

def without_duplicates(input):
    return list(set(input))

def replace(input):
    changed_list = input[:]
    for i in range(3, len(changed_list), 4):
        changed_list[i] = 'X'
    return changed_list

list2 = [22, 3,5,2,8,2,-23, 8,23,5]
print(find_min(list2))
print(without_duplicates(list2))
print(replace(list2))


"""
2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
"""

def task_func9(input):
    for i in range(input):
        if(i==0 or i==input - 1):
            print("*" * input)
        else:
            print('*' + ' '*(input - 2) + '*')

print(task_func9(10))

"""
3) вывести табличку множення за допомогою цикла while
"""

def task_func10(input):
    i = 1
    while i <= input:
        j = 1
        while j <= input:
            print(f'{i * j:4} ', end=' ')
            j +=1
        print()
        i+=1


print(task_func10(10))


"""
переробити це завдання під меню
"""

def menu():
    print("\nМеню:")
    print("1. Знайти мінімальне число")
    print("2. Видалити усі дублікати")
    print("3. Замінити кожне 4-те значення на 'X'")
    print("4. Вихід")




def find_min(input):
    return min(input)

def without_duplicates(input):
    return list(set(input))

def replace(input):
    changed_list = input[:]
    for i in range(3, len(changed_list), 4):
        changed_list[i] = 'X'
    return changed_list

while True:
    menu()
    choice = input("Виберіть варіант: ")

    if choice == '1':
        task1 = find_min(list2)
        print(f"Мінімальне число: {task1}")
    elif choice == '2':
        task2 = without_duplicates(list2)
        print(f"Список без дублікатів: {task2}")
    elif choice == '3':
        task3 = replace(list2)
        print(f"Список з заміненими кожними 4-ми значеннями: {task3}")
    elif choice == '4':
        print("Вихід з програми.")
        break
    else:
        print("Неправильний вибір. Спробуйте ще раз.")