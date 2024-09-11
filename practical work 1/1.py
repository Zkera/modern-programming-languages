import os

path = str(input())
print("Файл", os.path.split(path)[1], "имеет следующие права доступа:", end=" ")
if os.access(path, os.F_OK):
    if os.access(path, os.R_OK):
        print("чтение", end=" ")
    if os.access(path, os.W_OK):
        print("запись", end=" ")
    if os.access(path, os.X_OK):
        print("выполнение", end=" ")
else:
    print("Файл не найден")
