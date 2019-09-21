import socket
import json
from tkinter import *

sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 重用地址端口
sock_server.bind(('127.0.0.1', 8088))


sock_server.listen(5)  #5个连接排队

print('server started')

while True:
    conn, client_addr = sock_server.accept()
    print(client_addr)
    # clientLabel = Label(root,text = "连接的用户："+client_addr)
    # clientLabel.pack()

    Unlogged = True

    while Unlogged:
        try:
            ret = conn.recv(1024)
            Info = json.loads(ret)
            flag = False

            if Info['password'] == '00001':
                flag = True

            if flag:
                conn.send('Success'.encode('utf-8'))
                print("logged")
                Unlogged = False
            else:
                conn.send('Fail'.encode('utf-8'))
                print("error")

        except ConnectionResetError:
            break


    while True:
        data = conn.recv(1024)  # 接收1024个字节


        if not data:
            break

        print ('客户端的数据', data)

        conn.sendall(data.upper())  # 把收到的数据再全部返回给客户端




# root.mainloop()

conn.close()


server.close()