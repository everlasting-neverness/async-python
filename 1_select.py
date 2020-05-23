import socket
from select import select

to_monitor = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 4981))
server_socket.listen()


def accept_conntection(server_socket):
    print('Before accept()')
    client_socket, addr = server_socket.accept()
    print('Connection from', addr)

    to_monitor.append(client_socket)


def send_message(client_socket):
    print('Before recv()')
    request = client_socket.recv(4096)

    if request:
        print('Before send()')
        response = 'Hello world\n'.encode()
        client_socket.send(response)
    else:
        print('Before client socket close')
        client_socket.close()    


def event_loop():
    while True:
        ready_to_read, ready_to_write, ready_with_exceptions = select(to_monitor, [], [])

        for sock in ready_to_read:
            if sock is server_socket:
                accept_conntection(sock)
            else:
                send_message(sock)

if __name__ == "__main__":
    to_monitor.append(server_socket)
    event_loop()