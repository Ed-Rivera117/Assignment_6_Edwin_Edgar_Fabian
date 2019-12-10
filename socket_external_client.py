import socket

def Main():

    host='192.168.0.13' #client ip
    port = 4000

    host = socket.gethostbyname('0.0.0.0')
    server = ('10.31.3.129', 4000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))

    message = input("-> ")
    while message !='q':
        s.sendto(message.encode(), server)
        data, addr = s.recvfrom(1024)
        data = data.decode()
        print("Received from server: " + data)
        message = input("-> ")
    s.close()

if __name__=='__main__':
    Main()