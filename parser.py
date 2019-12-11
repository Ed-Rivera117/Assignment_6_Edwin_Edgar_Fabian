import ply.yacc as yacc
from pip._vendor.distlib.compat import raw_input
from lex import tokens
import socket
import sys

def p_local_sock_create(p):  # sock
    'CREATESOCKET : ID'
    # 'socket : SOCK'
    # p[0] = p[1]
    p[1] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def p_local_server_sock_bind(p):  # serveradress host port sock
    'BINDSOCKET : ID ID NUMBER CREATESOCKET'
    p[1] = (p[2], p[3])
    print(sys.stderr, 'starting up on %s port %s' % p[1])
    p[4].bind(p[1])
    p[4].listen(1)


def p_local_server_receive_repeated_messages(p):  # socket
    'RECEIVEREPEATED : ID'
    while True:
        # Wait for a connection
        print(sys.stderr, 'waiting for a connection')
        connection, client_address = p[1].accept()
        try:
            print(sys.stderr, 'connection from', client_address)

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(16)
                print(sys.stderr, 'received "%s"' % data)
                if data:
                    print(sys.stderr, 'sending data back to the client')
                    connection.sendall(data)
                else:
                    print(sys.stderr, 'no more data from', client_address)
                    break

        finally:
            # Clean up the connection
            connection.close()


########################
def p__local_client_connect(p):  # serveradress host port sock
    'CONNECTLOCALCLIENT : ID ID NUMBER CREATESOCKET'
    p[1] = (p[2], p[3])
    print(sys.stderr, 'connecting to %s port %s' % p[1])
    p[4].connect(p[1])


def p_local_client_repeated_messages(p):  # socket
    'REPEATEDMESSAGES : CREATESOCKET'
    try:

        # Send data
        message = 'This is the message.  It will be repeated.'
        print(sys.stderr, 'sending "%s"' % message)
        p[1].sendall(message.encode())

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = p[1].recv(16)
            amount_received += len(data)
            print(sys.stderr, 'received "%s"' % data)
    finally:
        print(sys.stderr, 'closing socket')
        p[1].close()


def p_local_client_finish(p):  # sock

    'FINISHLOCALCLIENT : CREATESOCKET'
    print(sys.stderr, 'closing socket')
    p[1].close()


#########
def p_external_sock_create(p):  # sock
    'CREATESOCKET : ID'
    p[1] = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def p_external_server_sock_bind(p):  # host port socket
    'BINDEXTERNALSERVERSOCKET : ID NUMBER CREATESOCKET'
    p[1] = socket.gethostbyname('0.0.0.0')
    p[3].bind(p[1], p[2])
    print("Server Started")


def p_external_server_receive_multi_messages(p):
    'MULTTIMESSAGESRECEIVE : CREATESOCKET'
    while True:
        data, addr = p[1].recvfrom(1024)
        data = data.decode()
        print("Message from: " + str(addr))
        print("From connected user: " + data)
        print("Sending: " + data)
        p[1].sendto(data.encode(), addr)


def p_external_server_close(p):
    'CLOSEEXTERNALSERVER : CREATESOCKE'
    p[1].close


##########
def p_external_client_bind(p):  # serveraddress host port sock
    'BINDEXTERNALCLIENTSOCKET : ID ID NUMBER CREATESOCKET'
    p[2] = socket.gethostbyname('0.0.0.0')
    p[1] = ('10.31.3.129', p[3])
    p[4].bind(p[2], p[3])


def p_external_client_sent_multi_messages(p):  # serveraddress socket
    'MULTTIMESSAGESSENT : ID CREATESOCKET'
    message = input("-> ")
    while message != 'stop':
        p[2].sendto(message.encode(), p[1])
        data, addr = p[2].recvfrom(1024)
        data = data.decode()
        print("Received from server: " + data)
        message = input("-> ")


def p_external_client_close(p):
    'CLOSEEXTERNALCLIENT : CREATESOCKET'
    p[1].close
