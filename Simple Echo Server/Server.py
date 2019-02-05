import socket
s=socket.socket()
host=socket.gethostname()
port=12345
s.bind((host,port))
s.listen(5)
while True:
    c,addr=s.accept()
    print("Connection Established with "+str(addr));
    c.send('Thank you for your connection'.encode())
c.close
