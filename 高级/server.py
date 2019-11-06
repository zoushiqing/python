import socket
import sys

# 创建socket对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取本地主机名
host = socket.gethostname()
print("hostname", host)
port = 9999
# 绑定端口号
serversocket.bind((host, port))
# 设置对打连接数,超过后开始排队
serversocket.listen(5)
while True:
    # 建立客户端连接
    clientsocket, addr = serversocket.accept()
    print("连接地址:", str(addr))
    msg = "欢迎访问志愿汇rencai"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()
