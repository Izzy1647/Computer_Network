# 模拟qq发消息 server

from socket import *
import tkinter as tk
import threading
import tkinter.scrolledtext as ts

class mainService(tk.Frame):
    def __init__(self,master):  #构造函数建立窗口
        tk.Frame.__init__(self,master)
        self.grid()
        self.creatNewWindow()

    def creatNewWindow(self):
        self.textArea = ts.ScrolledText(self,width=60,height=30)  # 显示信息的地方
        self.textArea.grid(row=0, column=0, rowspan=1, columnspan=4)
        self.inputMsg = tk.Text(self,width=50,height=5)  # 输入消息的地方
        self.inputMsg.grid(row=1,column=0,columnspan=1)
        self.sendButton =tk.Button(self,text='发送!',command=self.sendText) # function not defined yet  发送按钮
        self.sendButton.grid(row=1,column=3)


        # 不同用户使用不同颜色
        self.textArea.tag_config('user1', foreground='green')
        self.textArea.tag_config('user2', foreground='red')

        # 监听消息的新线程
        newThread = threading.Thread(target=self.getMsg) # function not defined yet -- getMsg()
        newThread.start()





    def sendText(self):   # 获取发送消息的内容
        msg = self.inputMsg.get('1.0','end-1c')   # 从inputMsg组件中获得内容
        self.textArea.config(state='normal')
        self.textArea.insert(tk.END,msg+'\n')
        # self.textArea.insert(tk.INSERT, 'user2')  # 署名
        self.textArea.see(tk.END)    # 页面拉到最底部
        self.textArea.config(state='disabled')
        self.inputMsg.delete(0.0,tk.END)  # 清空输入框

        msg_send = bytes(msg,encoding='utf-8')
        conn.send(msg_send)   # socket发送信息  conn 尚未初始化 main里初始化 line69


        # pass


    def getMsg(self):
        while True:
            msg_recv = conn.recv(1024).decode('utf-8')+'\n'
            self.textArea.config(state='normal')
            # self.textArea.insert(tk.END,'user1')
            self.textArea.insert(tk.END, msg_recv)
            self.textArea.see(tk.END)
            self.textArea.config(state='disabled')

        # pass

    def textSendReturn(self, event):
        if event.keysym == "Return":
            self.sendText()

# mainService 类结束

root = tk.Tk()
root.title('Server')

# Initialize socket
serverPort = 12000
server=socket(AF_INET,SOCK_STREAM)  # new socket
server.bind(('',serverPort))
server.listen(1)
print('Server started!!')


conn,addr = server.accept()
print('client connected!')


app = mainService(master=root)
app.mainloop()







