
class Client(self):
    import socket
        def client(host, port, message):

                s = socket.socket()
                s.connect((host, port))
                while True:
                    _message = message
                    s.send(_message.encode('utf-8'))
                    data = s.recv(1024).decode('utf-8')
                    return data
                s.close()

class ServerTrue(host, port):
    import socket
        def Server(host, port):
            s = socket.socket()
            s.bind((host,port))
            s.listen(1)
            c, addr = s.accept()
            while True:
                data = c.recv(1024).decode('utf-8')
                if not data:
                    break
                else
                    data = True
                    data = data.upper()
                c.send(data.encode('utf-8'))
            c.close()
