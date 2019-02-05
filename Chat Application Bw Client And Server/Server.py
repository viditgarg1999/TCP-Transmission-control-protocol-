import socket
s=socket.socket()
host=socket.gethostname()
port=12345
s.bind((host,port))
s.listen(5)
while True:
    c,addr=s.accept()
    print("Connection Established with "+ str(addr))
    c.send('Thankyou for your Connection'.encode())
    while True:
        msg=c.recv(1024).decode()
        if(msg=='bye'):
            c.send('Session Expired'.encode())
            c.close()
            break
        print('Client:'+msg)
        message=input('Server:')
        c.send(message.encode())
c.close()
