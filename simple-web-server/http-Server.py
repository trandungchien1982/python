from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime

print('Các ví dụ liên quan đến Web Server cơ bản ...')
print('--------------------------------------------')


# HTTPRequestHandler class
class SimpleHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        print('\n Tiến hành gọi do_GET()')
        # Nhận HTTP Request GET gủi lên server
        self.send_response(200)
        # Thiết lập header trả về
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Data
        message = "Hoc Lap Trinh Tai Toidicode.com, dành cho GET HTTP RESTful ..."
        # Write data dưới dạng utf8
        self.wfile.write(bytes(message, "utf8"))


    def do_POST(self):
        # Thực hiện 1 lời gọi POST từ main libray vào thư viện gốc
        print('\n Tiến hành gọi do_POST()')
        # Nhận HTTP Request POST gủi lên server
        self.send_response(200)
        # Thiết lập header trả về
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Data
        message = "Message từ Toidicode.com - For POST type of HTTP RESTful ..."
        # Write data dưới dạng utf8
        self.wfile.write(bytes(message, "utf8"))
        pass


# cấu hình host và cổng port cho server
server_address = ('127.0.0.1', 9500)

# Khởi tạo server với thông số cấu hình ở trên.
httpd = HTTPServer(server_address, SimpleHTTP)

# Tiến hành chạy server
httpd.serve_forever()


#
# showData(person)
#
# print('---------------------------------')
# print('--------- Khởi tạo Person2 ------')
# print('---------------------------------')
# p2 = Person('NAME 2', 222)
# showData(p2)
