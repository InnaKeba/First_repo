"""Написати схожий додаток на diff, який показує різницю між двома файлами diff.py a.txt b.txt."""
import sys
def compare_files(file1_path:str, file2_path:str):
    """1. Відкрити файл 2. Прочитати усі рядки у список 
       3. Порівняти списки 4. Вивести різницю"""
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        file1_lines = file1.readlines()
        file2_lines = file2.readlines()
    # Порівняння рядків через i індекс
    for i in range(max(len(file1_lines), len(file2_lines))):
        file1_lines = file1_lines[i].rstrip()
        file2_lines = file2_lines[i].rstrip()
        if file1_lines != file2_lines:
            print(f"Line {i + 1}:")
            print(f"File 1: {file1_lines}")
            print(f"File 2: {file2_lines}")


def main():
    if len(sys.argv) != 3: # != 3 не дорівнює 3
        print("Please provide file one path and file two path")
        sys.exit()  # або просто exit()
    # file1_path = sys.argv[1]
    # file2_path = sys.argv[2]
    _, file1_path, file2_path = sys.argv  # розпаковка змінних
    compare_files(file1_path, file2_path)


    # в терміналі спочатку перевірити чи ти знаходишся в необхідній директорії. Команда cd All_practices перевела мене в папку All_practices
    # потім запустити команду python diff.py a.txt b.txt