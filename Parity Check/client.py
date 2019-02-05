import socket
s=socket.socket()
host=socket.gethostname()
port=12345
s.connect((host,port))
dataword=int(input('Enter the Dataword:'))
dataword1=dataword
codeword=0
e1=[]
while dataword1>0:
 x=int(dataword1)%10
 e1.append(x)
 codeword=x^codeword
 dataword1=int(dataword1/10)
completeword=dataword*10+codeword
print(completeword)
e1.reverse()
print('Enter 1 if you want to send without error and 0 if with error')
actual_dataword=int(input())
if(actual_dataword==1):
 s.send('Error not found'.encode())
 s.send(str((completeword)).encode());
 s.close
if(actual_dataword==0):
 n=int(input('Enter the no of error bits:'))
 print('Enter the position of error bits:')
 for i in range(n):
     position=int(input())
     if(e1[position-1]==0):
         e1[position-1]=1
     elif(e1[position-1]==1):
         e1[position-1]=0
 s.send('Error found'.encode())
 s.send(str(e1).encode())
 s.close
