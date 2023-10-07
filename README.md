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

# Ví dụ [09.RabbitMQ+AMQP] Xử lý message queue dùng RabbitMQ với giao thức AMQP
==============================================================

**Dùng Docker Compose để khởi tạo message broker RabbitMQ**
- Tham khảo file `docker-compose.yml`
- Thực thi lệnh : 
```shell
docker-compose up
```

**Sử dụng thư viện pika trong Python để tương tác với RabbitMQ**
```shell
pip3 install pika
```

**Ta sẽ tạo các Class Python bao gồm:**<br/>
- Tạo 1 Producer để push messages đến RabbitMQ vào 1 queue chỉ định
- Tạo 1 Consumer để get message từ RabbitMQ từ 1 queue chỉ định


**Nguồn tham khảo**
- https://www.lhsang.dev/posts/technique/rabbitmq/
- https://galaxyz.net/cach-su-dung-rabbitmq-va-pythons-puka-de-gui-thong-diep-den-nhieu-nguoi-tieu-dung.2238.anews
- https://www.phamquangloc.vn/2020/08/reference-test-RabbitMQ-performance-voi-python-dung-pika.html

**Kết quả thực thi**<br/>
```shell
tdc@tdc:~/python/rabbitmq-amqp$ python3 producer.py 
-----------------------------------------------------------------
 >> Sent message at time: 2023-10-09 11:00:53.930411

```

```shell
tdc@tdc:~/python/rabbitmq-amqp$ python3 consumer.py 
-----------------------------------------------------------------
|| Hiện tại đang bị lỗi, sẽ giải quyết sau: 
 [*] Waiting for messages:

```
