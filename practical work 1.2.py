import os
import shutil

path = str(input())
if not os.access(path, os.F_OK):
    print("Файл не найден")
    exit()
if not (os.access(path, os.R_OK) and os.access(path, os.W_OK)):
    print("Не возможно прочитать/изменить файл")
    exit()

with open(path, "r") as file:
    data = file.read()
    print(data)
with open(path, "w") as file:
    data = data.replace(str(input()), str(input()))
    file.write(data)
print("Успешно")
print(data)
