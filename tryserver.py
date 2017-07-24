from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_BROADCAST

address=('192.168.137.228',31500)
s=socket(AF_INET,SOCK_DGRAM)
s.bind(address)
#if __name__=="__main__":
while True:
    data,addr=s.recvfrom(2048)
    #if not data:
        #print ("client has exist")
        #break
    print ("received:",data,"from",addr)
s.close()