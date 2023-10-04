import socket

print('Server Side Socket!')
print('Các ví dụ liên quan đến Server-Client dùng Socket ...')
print('Thiết lập Server Socket cho phép accept() 1 kết nối ...')
print('-------------------------------------------------------------')

HOST = 'localhost'
PORT = 9000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

conn, addr = server.accept()

with conn:
    try:
        # In ra client address
        print('Connected by ' + str(addr))
        while True:
            # Doc noi dung do client gui den
            data = conn.recv(1024)

            print(data)

            # Gui nguoc lai noi dung 'Hello Client' cho may khach
            conn.sendall(b'Hello Client!')

            # Neu khong con data thi dung doc tiep
            if not data:
                break
    finally:
        server.close()