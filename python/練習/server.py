import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 5000))
print('Listening at {}'.format(sock.getsockname()))
while True:
    data, address = sock.recvfrom(1000)
    text = data.decode('ascii')
    print('The client at {} says {!r}'.format(address, text))
    text = 'Server Echo: ' + text
    data = text.encode('ascii')
    sock.sendto(data, address)




    
#######################聊天室接收不同長度訊息的處理：
back = b''
# 定義message之間的分隔符號，例如'\n'，
while True: #當收到一個完整的message時才break
    # 收一筆資料進來 (最多收1024個bytes)
    data = sock.recv(1024) # data的長度介於1~1024之間
    data = back + data #將新進的data串在之前剩餘未處理的data後面
    #對data的每個byte做檢查，檢查其是否為'\n'，即一個message的結尾，記錄其位置
    for x in data:
        pos = -1
        if x=='\n': 
            #設定pos為x在data的索引位置
            #離開迴圈
    #如果pos>=0：
        #把data在索引pos處分為兩段：front, back
        #把front轉成字串，存入message，進行後續的處理








#####################聊天室Server轉送訊息的處理
# Server轉送來自tom的訊息

# 假設tom送來的訊息是"你好，我想放年假"

#建立一個dictionary放置JSON訊息內的所有資料
dict = {"sender": "tom","message": "你好，我想放年假","datetime": "2021-12-30 15:20:30"}

#轉成要送出去的JSON字串，但中間不要有'\n'
#即 '{"sender":"tom","message":"你好，我想放年假","datetime": "2021-12-30 15:20:30"}'
text = json.dumps(dict, separators=(',',':'))
text = text + '\n' #串一個'\n'讓接收端可識別一個完整的JSON訊息

#送出
data = text.encode('utf-8')
sock.sendall(data)