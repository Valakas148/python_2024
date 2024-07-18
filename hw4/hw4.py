

"""
1) Є ось такий файл... ваша задача записати в новий файл тільки email'ли з доменом gmail.com (Хеш то що з ліва записувати не потрібно)
"""
import json

try:
    with open('emails.txt', 'rb') as file, open('new_emails.txt', 'wb') as new_file:

        for line in file:

            line = line.decode('utf-8').strip()
            test = line.split('\t')
            # print(test)
            for i in test:
                if '@' in i:
                    email = i.strip()
                    # print(email)
                    if email.endswith('@gmail.com'):
                        new_file.write((email + '\n').encode('utf-8'))
except Exception as e:
    print(e)

"""
2) Створити записну книжку покупок:
- у покупки повинна бути id, назва і ціна
- всі покупки зберігаємо в файлі
з функціоналу:
 * вивід всіх покупок
 * має бути змога додавати покупку в книгу
* має бути змога шукати по будь якому полю покупку
* має бути змога показати найдорожчу покупку
* має бути можливість видаляти покупку по id
(ну і меню на це все)
"""
import uuid
import json
class Book:
    def __init__(self, name, price):
        self.id = str(uuid.uuid4())
        self.name = name
        self.price = price

    def get_info(self):
        return {'id': self.id, 'name': self.name, 'price': self.price}


class AddProduct:
    def __init__(self, file='products.json'):
        self.file = file
        self.products = self.load_products()

    def load_products(self):
        try:
            with open(self.file, 'r') as f:
                data = f.read()
                if data:
                    return json.loads(data)
                else:
                    return []
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def add_product(self, product):
        self.products.append(product.get_info())
        self.save_products()

    def save_products(self):
        with open(self.file, 'w') as f:
            json.dump(self.products, f)

    def search_product(self, field, value):
        try:
            with open(self.file, 'r') as f:
                data = json.load(f)
                if data:
                    found_products = [product for product in data if str(product.get(field, '')).lower() == value.lower()]
                    if found_products:
                        for product in found_products:
                            print(product)
                    else:
                        print('No products found.')
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def search_most_expensive(self):
        expensive = max(self.products, key=lambda product: product['price'])
        return expensive


    def show_all(self):
        try:
            with open(self.file, 'r') as f:
                data = json.load(f)
                if data:
                    for product in data:
                        print(product)
                else:
                    return []
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def delete(self, product_id):
        self.products =  [product for product in self.products if product['id'] != product_id]
        self.save_products()

product1 = Book('apple', 10)
product2 = Book('mango', 20)
print(product1.get_info())

def menu():
    purchase = AddProduct()

    while True:
        print('Menu:\n')
        print('1. Add product')
        print('2. Show all')
        print('3. Search product')
        print('4. Search most expensive product')
        print('5. Delete a product')
        choice = input('Enter your choice: ')
        match choice:
            case '1':
                name = input('Enter product name: ')
                price = input('Enter product price: ')
                product = Book(name, price)
                purchase.add_product(product)
            case '2':
                purchase.show_all()
            case '3':
                field = input('Enter product field: ')
                value = input(f'Enter product value in {field}: ')
                purchase.search_product(field, value)

            case '4':
                purchase.search_most_expensive()
            case '5':
                id = input('Enter product id: ')
                purchase.delete(id)
            case '6':
                break
            case _:
                print('Invalid input')

menu()