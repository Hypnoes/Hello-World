import socket
import random

def genetator():
    l = []
    for i in range(0, 8):
        l.append(random.randint(0, 255).to_bytes(1, "little"))
    return l

def main():
    with socket.socket() as target:
        target.bind(("", 5000))
        target.listen(1)
        conn, addr = target.accept()
        with conn:
            print("Connected by", addr)
            conn.send(b'Hypnoes')

if __name__ == '__main__':
    while True:
        main()