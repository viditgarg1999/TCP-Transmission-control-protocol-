import socket
s=socket.socket()
host=socket.gethostname()
port=12345
s.bind((host,port))
s.listen(5)
while True:
 c,addr=s.accept();
 print('Connection found',addr)
 a=c.recv(1024).decode()
 print(a)
 if(a=='Error not found'):
     print(c.recv(1024).decode())
 else:
     print('Actual Dataword is:')
     print(c.recv(1024).decode())
 c.close()
