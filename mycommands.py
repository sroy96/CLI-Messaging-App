import socket

if __name__ == "__main__":
    sr = []
    for i in range(20):
        sr.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))

    print(sr)
