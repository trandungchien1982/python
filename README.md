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

# Ví dụ [04.SimpleWebServer] Tạo WebApps đơn giản support GET/POST/... http requests ...
==============================================================

**Ta sẽ tạo 1 WebApps có xử lý 2 HTTP RESTful đơn giản:**<br/>
- GET  http://localhost:9005/
- POST http://localhost:9005/


**Nguồn tham khảo**
- https://toidicode.com/hoc-python-nang-cao
- https://toidicode.com/khoi-tao-server-trong-python-363.html


**Kết quả thực thi**<br/>
- *Launch WebApp server*
```shell
tdc@tdc:~/python/simple-web-server$ python3 http-Server.py
------------------------------------------------------------------------
Các ví dụ liên quan đến Web Server cơ bản ...
--------------------------------------------

```

- *GET*
```shell
GET  http://localhost:9500/
----------------------------------------------------------------------------
Hoc Lap Trinh Tai Toidicode.com, dành cho GET HTTP RESTful ...
```

- *POST*
```shell
POST  http://localhost:9500/
----------------------------------------------------------------------------
Message từ Toidicode.com - For POST type of HTTP RESTful ...
```