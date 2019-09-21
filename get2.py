import socket
url = 'www.baidu.com'
port = 80
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((url, port))
request_url = 'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n'
sock.send(request_url.encode())

#
# print(request_url.encode())
# print('asdfbgngdsafsgbgnbfsdad')
#


response = b''

rec = sock.recv(1024)
while rec:
    response += rec
    rec = sock.recv(1024)

print(response.decode())
