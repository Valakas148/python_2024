import abc
"""
Створити клас Rectangle:
-він має приймати дві сторони x,y
-описати поведінку на арифметични методи:
  + сумма площин двох екземплярів ксласу
  - різниця площин двох екземплярів ксласу
  == площин на рівність
  != площин на не рівність
  >, < меньше більше
  при виклику метода len() підраховувати сумму сторін


"""
print("TASK1")
class Rectangle:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return (self.x*self.y)+(other.x * other.y)

    def __sub__(self, other):
        return (self.x * self.y) - (other.x * other.y)

    def __eq__(self, other):
        return (self.x * self.y) == (other.x * other.y)

    def __ne__(self, other):
        return (self.x * self.y) != (other.x * other.y)

    def __lt__(self, other):
        return (self.x * self.y) < (other.x * other.y)

    def __gt__(self, other):
        return (self.x * self.y) > (other.x * other.y)

    def __len__(self):
        return self.x + self.y


r1 = Rectangle(2,2)
r2 = Rectangle(3,3)
print(r1+r2)
print(r1-r2)
print(r1==r2)
print(r1!=r2)
print(r1<r2)
print(r1>r2)
print(len(r1))



"""
створити класс Human (name, age)
створити два класси Prince и Cinderella які наслідуються від Human:
у попелюшки мае бути ім'я, вік, розмір нонги
у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму

в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
також має бути метод классу який буде виводити це значення

"""
print("TASK2")
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cinderella(Human):

    count = 0

    def __init__(self, name,age, foot_size):
        super().__init__(name, age)
        self.foot_size = foot_size
        self.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


class Prince(Human):
    def __init__(self, name,age, size_found):
        super().__init__(name, age)
        self.size_found = size_found

    def found_list(self, list_popels):
        for item in list_popels:
            if item.foot_size == self.size_found:
                return f"found {item.name}"



popel1 = Cinderella('Anna', 20, 20)
popel2 = Cinderella('Yana', 21, 24)
popel3 = Cinderella('Nastya', 24, 33)
popel4 = Cinderella('Vika', 19, 25)
popel5 = Cinderella('Sasha', 20, 27)

prince = Prince('Petya', 20, 24)

popel_list = [popel1, popel2, popel3,popel4,popel5]

print(prince.found_list(popel_list))


"""
1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
"""
print("TASK3.1")

class Printable(abc.ABC):
    @abc.abstractmethod
    def print(self):
        pass


"""
2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
"""
print("TASK3.2")

class Book(Printable):
    def __init__(self,name):
        super().__init__()
        self.name = name

class Magazine(Printable):
    def __init__(self,name):
        super().__init__()
        self.name = name

"""
3) Створити клас Main в якому буде:
- змінна класу printable_list яка буде зберігати книжки та журнали
- метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
- метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
- метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
"""

class Main():
    def __init__(self, printable_list):
        self.printable_list = printable_list

    def add(self,name):
        if isinstance(name,(Book,Magazine)):
            self.printable_list.append(name)


    def show_all_magazines(self):