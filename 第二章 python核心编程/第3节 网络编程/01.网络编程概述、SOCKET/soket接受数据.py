import socket

server = socket.socket()
# 绑定要监听的端口
server.bind(("127.0.0.1", 6969))

server.listen()  # 监听

print("我要开始监听了")

conn, addr = server.accept()  # 等电话来,conn就是客户端连接过来，而在服务器端为其生成的一个链接实例

print(conn, addr)

print("电话来了")

data = conn.recv(1024)

print("recv", data)

conn.send(data.upper())

server.close()
