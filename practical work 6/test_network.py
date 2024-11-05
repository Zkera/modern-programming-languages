# Файл test_network.py
import subprocess
import time

from concurrent.futures import ThreadPoolExecutor
def run_server():
    # Запускаем сервер в отдельном процессе
    server_process = subprocess.Popen(["python", "server.py"])
    time.sleep(1) # Даем серверу время для запуска
    return server_process
def run_client():
    # Запускаем клиента в отдельном процессе
    client_process = subprocess.Popen(["python", "client.py"])
    return client_process
def test_network_interaction():
    # Запускаем сервер
    server_process = run_server()
    n = 3
    try:
    # Запускаем n клиентов одновременно
        with ThreadPoolExecutor(n) as executor:
            clients = [executor.submit(run_client) for _ in range(n)]
            # Даем клиентам время для взаимодействия
            for client in clients:
                client.result().wait()
            # Проверяем, что все клиенты завершились без ошибок
            for client in clients:
                assert client.result().returncode == 0
    finally:
        # Завершаем сервер после завершения теста
        server_process.terminate()
        server_process.wait()
