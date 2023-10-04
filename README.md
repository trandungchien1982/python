# python
Các ví dụ liên quan đến Python từ cơ bản đến nâng cao<br/>
Mỗi nhánh trong Repo sẽ là 1 ví dụ/ giải pháp/ project mẫu trong Python

# Môi trường phát triển
- Python 3.8.10
- Tạo alias ngắn gọn trên Ubuntu 20.04
```shell
    alias p=python3
    -----------------------
    p --version
    -----------------------
    Python 3.8.10 
    
```

# Folder liên quan trên Windows
```
D:\Projects\python
```

==============================================================

# Ví dụ [05.ServerClientSocket] Tạo Web App Socket đơn giản với 1 Server + 1 Client
==============================================================

**Ta sẽ tạo 2 WebApps bao gồm:**<br/>
- ServerSocket cho phép accept 1 kết nối Client
- ClientSocket thực hiện kết nối đến Server


**Nguồn tham khảo**
- https://toidicode.com/hoc-python-nang-cao
- https://toidicode.com/lap-trinh-mang-voi-module-socket-trong-python-364.html


**Kết quả thực thi**<br/>
- *Launch Server Socket*
```shell
tdc@tdc:~/python/server-client-socket$ python3 server-socket.py 
------------------------------------------------------------------------
Server Side Socket!
Các ví dụ liên quan đến Server-Client dùng Socket ...
Thiết lập Server Socket cho phép accept() 1 kết nối ...
-------------------------------------------------------------
Connected by ('127.0.0.1', 57526)
b'Gui loi chao den ServerSocket!'
b''

```

- *Launch Client Socket*
```shell
tdc@tdc:~/python/server-client-socket$ python3 client-socket.py
------------------------------------------------------------------------
ClientSide - Socket
Thiết lập Socket từ phía Client và tiến hành kết nối để tương tác với ServerSocket ...
-------------------------------------------------------------
Server Response: b'Hello Client!'

```
