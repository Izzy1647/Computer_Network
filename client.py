import socket
import json
from tkinter import *


root = Tk()
root.title('client')
root.geometry('460x240')


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print(client)

client.connect(('127.0.0.1', 8088))


def login():
    name = inp1.get()
    password = inp2.get()
    Info = json.dumps({'name': name, 'password': password}).encode('utf-8')  #组装参数
    client.send(Info)
    ret = client.recv(1024).decode('utf-8')

    # print('ret',ret)

    # print(ret)
    # retLabel = Label(root,text=ret)

    # pass

def sendText():
    data = inp3.get()
    client.send(data.encode('utf-8'))  # 发送数据

    retdata = client.recv(1024)  # 接收数据
    retLabel = Label(root,text = '发送数据:'+retdata.decode())
    # retLabel.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
    retLabel.pack()

        # print('接收数据 =', data.decode())


lb1 = Label(root, text='username')
lb1.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.1)

lb2 = Label(root,text = 'password')
lb2.place(relx=0.6, rely=0.1, relwidth=0.2, relheight=0.1)



inp1 = Entry(root)
inp1.place(relx=0.1, rely=0.2, relwidth=0.2, relheight=0.1)
inp2 = Entry(root)
inp2.place(relx=0.6, rely=0.2, relwidth=0.2, relheight=0.1)

btn1 = Button(root, text='login', command=login)    # login function
btn1.place(relx=0.3, rely=0.4, relwidth=0.3, relheight=0.1)

btn2 = Button(root, text='send',command=sendText)    # text function
# btn2 = Button(root, text='方法二', command=lambda: run2(inp1.get(), inp2.get()))
btn2.place(relx=0.3, rely=0.8, relwidth=0.3, relheight=0.1)

inp3 = Entry(root)
inp3.place(relx=0.1, rely=0.7, relwidth=0.6, relheight=0.1)


root.mainloop()


client.close()  # 关闭

