# coding=utf-8
from socket import *

# 创建socket
tcpSerSocket = socket(AF_INET, SOCK_STREAM)
# 绑定本地信息
address = ('127.0.0.1', 1288)
tcpSerSocket.bind(address)
# 使⽤socket创建的套接字默认的属性是主动的，使⽤listen将其变为被动的，这样就可以接收别⼈的链接了 数字表示最多接受多少个链接请求
tcpSerSocket.listen(5)
# 如果有新的客户端来链接服务器，那么就产⽣⼀个新的套接字专⻔为这个客户端服务器
# newSocket⽤来为这个客户端服务
# tcpSerSocket就可以省下来专⻔等待其他新客户端的链接
newSocket, clientAddr = tcpSerSocket.accept()
# 接收对⽅发送过来的数据，最⼤接收1024个字节
recvData = newSocket.recv(1024)
print('接收到的数据为:', str(recvData, encoding="utf-8"))
# 发送⼀些数据到客户端
newSocket.send(bytes("thank you !", encoding='utf-8'))
# 关闭为这个客户端服务的套接字，只要关闭了，就意味着为不能再为这个客户端服务了，如果还需要服务，只能再次重新连接
newSocket.close()
# 关闭监听套接字，只要这个套接字关闭了，就意味着整个程序不能再接收任何新的客户端的连接
tcpSerSocket.close()
