import matplotlib.pyplot as plt
import pandas as pd
import pymysql.cursors #для соединения с БД
# Параметры подключения к MySQL
mydb = pymysql.connect(host = "localhost",
    user="root",    password="sharty_beem",
    database="лесной_участок")
mycursor = mydb.cursor() #для выполнения SQL-запросов и извлечения результатов из базы данных
mycursor.execute("""        CREATE TABLE IF NOT EXISTS trees1 ( 
    id INT AUTO_INCREMENT PRIMARY KEY,     наименование VARCHAR(255), 
    количество_деревьев INT,     диаметр FLOAT, 
    высота INT,     характеристика VARCHAR(255) 
)""") 
trees1 = [
    ('Рябина', 12, 0.25, 12, 'сухостой'),    ('Ива', 5, 0.30, 3, 'сухостой'),
    ('Береза', 22, 0.40, 9, 'сухостой'),    ('Липа', 8, 0.28, 17, 'сухостой'),
    ('Дуб', 15, 0.52, 20, 'аварийное'),    ('Клен', 19, 0.32, 4, 'аварийное')
] 
sql = "INSERT INTO trees1 (наименование, количество_деревьев, диаметр, высота, характеристика) VALUES (%s, %s, %s, %s, %s)"# для вставки данных в таблицу
mycursor.executemany(sql, trees1)
mydb.commit() # фиксирует изменения, внесенные в базу данныхprint("Таблица 'trees1' создана и заполнена.")
sql_select = "SELECT * FROM trees1" # Извлечение данных из таблицы в DataFrame
mycursor.execute(sql_select)
rows = mycursor.fetchall() # Получение всех строк
columns = [desc[0] for desc in mycursor.description]
df = pd.DataFrame(rows, columns=columns)
mycursor.close()
mydb.close()
print(df)
# Подсчет суммарного количества всех деревьев
total_trees = df['количество_деревьев'].sum()
print(f"Суммарное количество всех деревьев: {total_trees}")
# Подсчет средней высоты деревьев
average_height = df['высота'].mean()
print(f"Средняя высота деревьев: {average_height:.2f}")
# Создание гистограммы высоты деревьев по видам
plt.figure(figsize=(6, 6))
plt.bar(df['наименование'], df['высота'], color='orange')
plt.xlabel('Виды деревьев')
plt.ylabel('Высота')
plt.title('Гистограмма высоты деревьев по видам')
plt.xticks(rotation=90)
plt.tight_layout() #чтобы графики не накладывались друг на друга
plt.show()
