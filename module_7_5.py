import os
import time

directory = "."

for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = os.path.join(root, file)  # Объединяет корневую директорию root и имя файла file в один полный путь.
    filetime = os.path.getmtime(filepath)  # возвращает время последнего изменения файла
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(filepath)  # Используйте os.path.getsize для получения размера файла.
    parent_dir = os.path.dirname(filepath)  # Используйте os.path.dirname для получения родительской директории файла.
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
