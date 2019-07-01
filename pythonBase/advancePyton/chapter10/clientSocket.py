import socket
import threading


class RecieverThread(threading.Thread):

    def __init__(self, client):
        super(RecieverThread, self).__init__()
        self.client = client

    def run(self):
        while True:
            data = client.recv(1024)
            print(data.decode('utf8'))


class SendThread(threading.Thread):

    def __init__(self, client):
        super(SendThread, self).__init__()
        self.client = client

    def run(self):
        while True:
            send_data = input()
            client.send(send_data.encode('utf8'))


if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8001))
    sendclient = SendThread(client=client)
    sendclient.start()

    rcvclient = RecieverThread(client=client)
    rcvclient.start()

# client.close()
