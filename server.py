import random
import socket
import _thread
import string
import json

client_list = dict()
priority_queue = []
for i in range(20000):
    client_list[i] = None


# value = [conn, addr]
def createSocket(host="127.0.0.1", port=9001):
    print("host is : ", host)
    print("port is : ", port)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(20)
    return server

def serverListener(conn_id):
    while 1:
        value = client_list[conn_id]
        if value is None:
            return
        try:
            message = value[0].recv(2048)
            client_list[conn_id][0].send(bytes("ACK", 'utf-8'))
            if message:
                print("<" + value[2] + "> " + str(message))
                message_to_send = json.loads(message)['msg']
                msg = {
                    'from': value[2],
                    'msg': message_to_send
                }
                broadcast(json.dumps(msg), value[0])
            else:
                client_list[conn_id][0].send(bytes("NOACK", 'utf-8'))
                remove(value[0])
        except KeyboardInterrupt:
            return



# value is the connection
def broadcast(message, connection):
    for client in client_list.keys():
        if client_list[client] is not None and client_list[client][3] != 'DEACTIVE':
            try:
                client_list[client][0].send(bytes(message, 'utf-8'))
            except:
                client_list[client][0].close()
                remove(client)

def remove(client):
    client_list[client][3] = 'DEACTIVE'


def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for _ in range(y))


def new_clients(server):
    while 1:
        connection, address = server.accept()
        i = 0
        while i < 20000:
            if client_list[i] is None:
                break
            i += 1
        client_list[i] = [connection, address, random_char(5), 'ACTIVE']
        _thread.start_new_thread(serverListener, (i,))


if __name__ == "__main__":
    print("starting server")
    server_ = createSocket()
    print("server started")
    new_clients(server_)
    server_.close()

