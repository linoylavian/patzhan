import socket
import hashlib
import threading
global finish
global text
import Performance


class patz:
    def __init__(self):
        self.finish = False
        self.soc = socket.socket()
        self.soc.connect(("127.0.0.1", 13370))
        self.threads = list()

    def conn(self):
        self.soc.send("Howdy".encode())
        self.socket_id = self.soc.recv(1024).decode()
        self.soc.close()

    def catfish(self):
        self.soc = socket.socket()
        self.soc.bind(("0.0.0.0",13370+int(self.socket_id)))
        self.soc.listen()
        (self.client_socket, self.client_address) = self.soc.accept()
        self.data = self.client_socket.recv(1024).decode()
        if self.data:
            self.start, self.stop, self.md5 = self.data.split(",")
            self.start_finding()

    def listen(self):
        while True:
            self.data = self.client_socket.recv(1024).decode()
            if self.data[:6] == "finish":
                self.finish = True
                self.lights()
            elif self.data:
                self.start, self.stop, self.md5 = self.data.split(",")
                t = threading.Thread(target=self.allop, args=())
                self.threads.append(t)
                t.start()

    def strtomd5(self, st):
        hash_object = hashlib.md5(st.encode())
        return hash_object.hexdigest()

    def generator(self, s, place, stop):
        for f in range(25):
            if not self.finish:
                tmp = chr(ord(s[place]) + 1)
                s = s[:place] + tmp + s[place + 1:]
                if self.strtomd5(s) == self.md5:
                    self.send_pass(s)
                    self.finish = True
                elif s == stop:
                    self.send_notfound()
                for x in range(7 - place):
                    self.generator(s, 7 - x, stop)

    def allop(self):
        print('start search ' + self.start + ' to ' + self.stop)
        if self.strtomd5(self.start) == self.md5:
                self.send_pass(self.start)
        for i in range(8):
            self.generator(self.start, 7 - i, self.stop)
    
    def send_pass(self, s):
        self.client_socket.send((self.socket_id + ',true,' + self.md5 + ',' + s).encode())
        print('found ' + self.start + ' to ' + self.stop)

    def send_notfound(self):
        self.client_socket.send((self.socket_id + ',false,' + self.md5 + ',').encode())
        print('not found ' + self.start + ' to ' + self.stop)

    def start_finding(self):
        t = threading.Thread(target=self.listen, args=())
        self.threads.append(t)
        t.start()

        t = threading.Thread(target=self.allop, args=())
        self.threads.append(t)
        t.start()

    def lights(self):
        Performance.main()



def main():
    p = patz()
    p.conn()
    p.catfish()


if __name__ == '__main__':
    main()
