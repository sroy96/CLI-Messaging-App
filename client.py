import random
import socket
import string
import sys
import select
import time
import json




if __name__ == "__main__" :
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(sys.argv)
    if len(sys.argv) < 3 :
        print("Correct usage: script, IP address, port number")
        exit()
    IP_address = str(sys.argv[1])
    Port = int(sys.argv[2])
    server.connect((IP_address, Port))

    while True :
        try :
            sockets_list = [sys.stdin, server]
            read_sockets, write_socket, error_socket = select.select(sockets_list, [], [])

            for socks in read_sockets :
                if socks == server :
                    message = socks.recv(2048)
                    try :
                        k = json.loads(message.decode("utf-8"))
                        print(k['from'], " : ", k['msg'])
                    except :
                        print(message)
                else :
                    message = sys.stdin.readline()
                    message = {
                        'msg_id' : random_char(10),
                        'msg' : message,
                        'timestamp' : time.time()
                    }
                    message = bytes(json.dumps(message), 'utf-8')
                    server.send(message)
                    sys.stdout.flush()
        except KeyboardInterrupt :
            server.close()
