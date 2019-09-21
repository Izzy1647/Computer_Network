
from socket import *
import sys

'''
str1 = 'asdf'
print(type(str1))
str1 = str1.encode('utf-8')
print(type(str1))
'''
# url_b = str(url).encode('utf-8')   # byte类型
# b1 = b'GET / HTTP/1.1\r\nHost: '
# b2 = b'\r\nConnection: close\r\n\r\n'
# header = b1 + url_b + b2
#
# print(type(header))
# print(header)

def http_get(url):
    url_b = str(url).encode('utf-8')   # 转为byte类型
    # b1 = b'GET / HTTP/1.1\r\nHost: '
    # b2 = b'\r\nConnection: close\r\n\r\n'
    header = b'GET / HTTP/1.1\r\nHost: ' + url_b + b'\r\nConnection: close\r\n\r\n'

    # header = b'GET / HTTP/1.1\r\nHost: www.microsoft.com\r\nConnection: close\r\n\r\n'  # Connection:Keep-Alive

    print(type(header))   # bytes

    HOST = url
    PORT = 80
    BUFSIZ = 1024  # 1024字节接收

    # 创建socket

    for paras in getaddrinfo(HOST, PORT, AF_UNSPEC,
                           SOCK_STREAM, 0, AI_PASSIVE):
        print(paras)     # (<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_STREAM: 1>, 6, '', ('221.230.146.237', 80))
        af, socktype, proto, canonname, sockaddr = paras

        try:

            # 初始化socket
            webClient = socket(af, socktype)

        except OSError as msg:
            webClient = None
            continue

        try:
            webClient.connect(sockaddr)
        except OSError as msg:
            webClient.close()
            webClient = None
            continue
        break

    if webClient is None:
        print('could not open socket')
        sys.exit(1)


    '''
    
    url = 'www.baidu.com'
    port = 80
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((url, port))
    request_url = 'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n'
    sock.send(request_url.encode())
    
    '''



    # socket建立之后发送请求

    buffer = []  # 缓存数组保存接受信息
    with webClient:
        webClient.send(header)
        print("sended")

        while True:
            recv = webClient.recv(BUFSIZ)  # bytes
            # print(recv)
            if recv:
                buffer.append(recv.decode())
            else:
                break
        data = ''.join(buffer).encode()  # list to str
        data = data.decode()

        print(data)
        # note "encoding = 'utf-8'", or it will raise UnicodeEncodeError
        with open('recv_'+url+'.txt', 'w', encoding='utf-8') as f:
            f.write(data)




http_get('www.baidu.com')

