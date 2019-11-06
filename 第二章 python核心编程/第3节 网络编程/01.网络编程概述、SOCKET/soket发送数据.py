import socket

client = socket.socket()  # 申明socket类型，同时生成socket连接对象

client.connect(("192.168.199.100", 6969))

client.send(b"hello world")
data = client.recv(1024)

print("recv", data)

client.close()
