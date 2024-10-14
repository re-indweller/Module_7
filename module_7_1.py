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

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        existing_products = self.get_products()
        app_file = open(self.__file_name, 'a')
        for products in existing_products:
            str_item = str(products)
            if str_item not in existing_products:
                app_file.write(f'{str_item}\n')
                app_file.close()
            if str_item in existing_products:
                print(f"Продукт {product.name} уже есть в магазине")

# Пример использования
if __name__ == "__main__":
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # str

    s1.add(p1, p2, p3)

    print(s1.get_products())
