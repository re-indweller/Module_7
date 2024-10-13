# Домашнее задание по теме "Режимы открытия файлов"
# Задача "Учёт товаров":

from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def _read_products(self):
        with open(self.__file_name, 'r') as file:
            lines = file.readlines()
        products = []
        for line in lines:
            product = line[:-1].split(', ')
            products.append((product[0], float(product[1]), product[2]))
        return products

    def get_products(self):
        current_products = self._read_products()
        result = ''
        for product in current_products:
            result += ', '.join([product[0], str(product[1]), product[2]]) + '\n'
        return result[:-1]

    def add(self, *products):
        if not products:
            return
        existing_products = self._read_products()
        for product in products:
            if product.name in map(lambda x: x[0], existing_products):
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                with open(self.__file_name, 'a+') as file:
                    file.write(f"{product.name}, {product.weight}, {product.category}\n")


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
