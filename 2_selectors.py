import socket
import selectors

selector = selectors.DefaultSelector()

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 4981))
    server_socket.listen()

    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_conntection)


def accept_conntection(server_socket):
    print('Before accept()')
    client_socket, addr = server_socket.accept()
    print('Connection from', addr)
    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_message)


def send_message(client_socket):
    print('Before recv()')
    request = client_socket.recv(4096)

    if request:
        print('Before send()')
        response = 'Hello world\n'.encode()
        client_socket.send(response)
    else:
        print('Before client socket close')
        selector.unregister(client_socket)
        client_socket.close()    


def event_loop():
    while True:
        events = selector.select()

        for key, _ in events:
            callback = key.data
            callback(key.fileobj)



if __name__ == "__main__":
    server()
    event_loop()