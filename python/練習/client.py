import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
text = input("Please inout a string: ")
data = text.encode('ascii')
sock.sendto(data, ('127.0.0.1', 5000))
print('The OS assigned me the address {}'.format(sock.getsockname()))
data, address = sock.recvfrom(1000)
text = data.decode('ascii')
print('The server {} replied {!r}'.format(address, text))