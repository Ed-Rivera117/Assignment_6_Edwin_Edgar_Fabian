import socket

def Main():

    host = '192.168.0.12' #Server ip
    port = 4000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = socket.gethostbyname('0.0.0.0')
    s.bind((host, port))

    print("Server Started")
    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode()
        print("Message from: " + str(addr))
        print("From connected user: " + data)
        print("Sending: " + data)
        s.sendto(data.encode(), addr)
    c.close()

if __name__=='__main__':
    Main()