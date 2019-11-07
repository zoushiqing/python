from socket import *

# 创建socket
tcpClientSocket = socket(AF_INET, SOCK_STREAM)
# 链接服务器
serAddr = ('127.0.0.1', 1288)
tcpClientSocket.connect(serAddr)
# 提示⽤户输⼊数据
tcpClientSocket.send(bytes("我是客户端的数据", encoding='utf-8'))
# 接收对⽅发送过来的数据，最⼤接收1024个字节
recvData = tcpClientSocket.recv(1024)
print('接收到的数据为:', recvData)
# 关闭套接字
tcpClientSocket.close()
