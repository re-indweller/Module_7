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
        pprint(file.read())
        file.close()
        return file

    # def add(self, *products):
    #     existing_products = self.get_products()
    #     for product in products:
    #         if
    #             file = open(self.__file_name, 'r')
    #             pprint(file.read())
    #             file.close()
    #         else:
    #             print(f"Продукт {product.name} уже есть в магазине")


# Пример использования
if __name__ == "__main__":
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # str

    s1.add(p1, p2, p3)

    print(s1.get_products())
