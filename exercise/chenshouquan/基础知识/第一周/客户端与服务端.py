#客户端
import socket
client=socket.socket()#生成socket对象
client.connect(("localhost",6969))#和目标主机建立连接
client.send("hello world!".encode())#向对方发送数据
client.close()

'''
#服务端
import socket
server=socket.socket()#生成socket对象
server.bind(("localhost",6969))#绑定监听对象
server.listen()#监听
print("准备接电话了。。。")
con,addr=server.accept()#等待消息
print(con,addr)
data=con.recv(1024)
print("接收到消息是：",data)
server.close()
'''
