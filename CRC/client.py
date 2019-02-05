import socket
s=socket.socket()
host=socket.gethostname()
port=12343
s.connect((host,port))
dataword=int(input('Enter the Dataword:'))
divisor=int(input('Enter the divisor:'))
divident=int(dataword*1000)
main_divident=[]
main_divisor=[]
divident1=int(divident)
divisor1=int(divisor)
l=0

while divident1>0:
    x=int(divident1%10)
    main_divident.append(x)
    divident1=int(divident1/10)
    l=l+1;


while divisor1>0:
    x=int(divisor1%10)
    main_divisor.append(x)
    divisor1=int(divisor1/10)
    
main_divident.reverse()
main_divident1=main_divident
main_divisor.reverse()
print(main_divident)
print(main_divisor)
lm=len(main_divisor)
l=l-3
for i in range(l):
    if(main_divident[i]==1):
        k=i
        for j in range(lm):
            main_divident[k+j]=main_divident[k+j]^main_divisor[j]

for i in range (3):
    dataword=dataword*10 + main_divident[l+i]


print('Dataword to be Sent is:'+ str(dataword))

s.send(str(dataword).encode())
s.send(str(divisor).encode())


