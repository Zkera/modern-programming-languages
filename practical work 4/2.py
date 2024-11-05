import matplotlib.pyplot as plt
import pandas as pd
import pymysql.cursors
# Параметры подключения к MySQL
mydb = pymysql.connect( 
    host = "localhost",    user="root",
    password="sharty_beem",    database="лесной_участок"  
)
mycursor = mydb.cursor()
try:
    update_query = "UPDATE trees1 SET rating= %s WHERE product_id = %s"
    new_rating = 123.456 #значение для обновления
    product_id_to_update = 1
    mycursor.execute(update_query, (new_rating, product_id_to_update))
    mydb.commit()
    print("Транзакция успешно завершена.")
except Exception as e:
    mydb.rollback()
    print(f"Произошла ошибка: {str(e)} Транзакция откатывается.")
finally:
    mydb.close()