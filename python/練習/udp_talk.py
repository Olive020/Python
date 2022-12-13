import socket, argparse

def send():
    global sock
    while True:
        # 讓使用者輸入文字
        text = input(">>> ")
        # 將文字傳出
        data = text.encode('ascii')
        sock.send(data)
    
def recv():
    while True:
        # 收來自sock的資料
        data = sock.recv(1000)
        # 將資料印出來
        text = data.decode('ascii')
        print('<<< '+text)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='UDP talk with thread')
    parser.add_argument('localIP', help='local IP address for binding')
    parser.add_argument('localPort', metavar='PORT', type=int, help='local UDP port for binding')
    parser.add_argument('remoteIP', help='remote IP address for connecting')
    parser.add_argument('remotePort', metavar='PORT', type=int, help='remote UDP port for connecting')
    args = parser.parse_args()
    #print(args.localIP, args.localPort, args.remoteIP, args.remotePort)
    
    # 建立socket，然後bind到local address，connect到remote address
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((args.localIP, args.localPort))
    sock.connect((args.remoteIP, args.remotePort))