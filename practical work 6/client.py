# Файл client.py
import socket
import time
print("start process")
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as cli:
	cli.connect(('127.0.0.1', 8080))
	print(f"-- Клиент подключен к серверу")
	for i in range(1, 6):
		expression = f"2**{i}"
		cli.send(expression.encode('utf-8'))
		result, _ = cli.recvfrom(1024)
		print(f" результат: {result.decode('utf-8')}")
		time.sleep(1)

