# Файл server.py
import socket
import math

print("start process")
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as svr:
	svr.bind(('127.0.0.1', 8080))
	print(f"\n-- Сервер запущен в работу:")
	while True:
		data, addr = svr.recvfrom(1024)
		x = data.decode('utf-8')
		res = eval(x)
		svr.sendto(f'{x} = {res}'.encode('utf-8'), addr)
