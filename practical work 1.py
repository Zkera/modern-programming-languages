import os

path = str(input())
if os.access(path, os.F_OK):
    print("Файл есть")
    if os.access(path, os.R_OK):
        print("Файл читаемый")
    if os.access(path, os.W_OK):
        print("Файл изменяемый")
    if os.access(path, os.X_OK):
        print("Файл выполняемый")
else:
    print("Файл не найден")