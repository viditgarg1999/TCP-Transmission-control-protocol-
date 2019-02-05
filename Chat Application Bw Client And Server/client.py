import socket
s=socket.socket()
host=socket.gethostname()
port=12345
s.connect((host,port))
print(s.recv(1024).decode())
message='hi'
while message!='bye':
    str1=input('Client:')
    s.send(str1.encode())
    message=s.recv(1024).decode()
    print('Server:'+str(message))
print('Session Expired')
s.close()
