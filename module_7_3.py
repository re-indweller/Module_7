# Домашнее задание по теме "Оператор "with".
# Задача "Найдёт везде":

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                for



    #     return {'file1.txt': ['word1', 'word2'],
    #             'file2.txt': ['word3', 'word4'],
    #             'file3.txt': ['word5', 'word6', 'word7']}

    # def find(self, word):
    # def count(self, word):

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего