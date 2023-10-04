import socket

print('ClientSide - Socket')
print('Thiết lập Socket từ phía Client và tiến hành kết nối để tương tác với ServerSocket ...')
print('-------------------------------------------------------------')

HOST = 'localhost'
PORT = 9000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.sendall(b'Gui loi chao den ServerSocket!')

data = client.recv(1024)
print('Server Response: ' + repr(data))

# Ngat ket noi
client.close()
