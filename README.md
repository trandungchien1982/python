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

# Ví dụ [07.MultiThreading] Xử lý đa luồng ...
==============================================================

**Ta sẽ tạo các Class Python bao gồm:**<br/>
- 2 functions được xử lý tuần tự trong 1 Thread chính duy nhất (legacy), mỗi bước tính toán chờ 0.2s và 0.3s
- 2 functions được xử lý concurrency ở 2 Thread khác nhau, bước tính toán chờ như trên
- 2 function xử lý tài nguyên chung & cần cơ chế Lock
- Tạo daemond thread để có thể tuỳ biến việc stop thread an toàn ...


**Nguồn tham khảo**
- https://viblo.asia/p/da-luong-trong-python-multithreading-WAyK8MO6ZxX


**Kết quả thực thi**<br/>
- *1 Thread duy nhất: 2 functions (legacy)*
```shell
tdc@tdc:~/python/multi-threading$ python3 one-thread+2functions.py
Ví dụ về xử lý data luồng (1 thread + 2 functions tính toán) ...
-------------------------------------------------------

--- Hàm cal_square với numbers: (2, 6, 7, 30, 10, 9, 17, 20, -30)
 ----> Current number 2: square(2) = 4
 ----> Current number 6: square(6) = 36
 ----> Current number 7: square(7) = 49
 ----> Current number 30: square(30) = 900
 ----> Current number 10: square(10) = 100
 ----> Current number 9: square(9) = 81
 ----> Current number 17: square(17) = 289
 ----> Current number 20: square(20) = 400
 ----> Current number -30: square(-30) = 900

--- Hàm cal_cube với numbers: [1, 2, 5, 10, 11, 12, 15, 8, 77, -39]
 ===> Current number 1: cube(1) = 1
 ===> Current number 2: cube(2) = 8
 ===> Current number 5: cube(5) = 125
 ===> Current number 10: cube(10) = 1000
 ===> Current number 11: cube(11) = 1331
 ===> Current number 12: cube(12) = 1728
 ===> Current number 15: cube(15) = 3375
 ===> Current number 8: cube(8) = 512
 ===> Current number 77: cube(77) = 456533
 ===> Current number -39: cube(-39) = -59319
>> Tổng thời gian: 4

```

- *2 Threads + xử lý 2 functions*
```shell
tdc@tdc:~/python/multi-threading$ python3 two-threads.py
------------------------------------------------------------------------
Ví dụ về xử lý data luồng (2 threads cho 2 functions tính toán) ...
-------------------------------------------------------

--- Hàm cal_square với numbers: (2, 6, 7, 30, 10, 9, 17, 20, -30)

--- Hàm cal_cube với numbers: [1, 2, 5, 10, 11, 12, 15, 8, 77, -39]
 ----> Current number 2: square(2) = 4
 |||||||||||| ~ ~ ~> Current number 1: CUBE(1) = 1
 ----> Current number 6: square(6) = 36
 ----> Current number 7: square(7) = 49
 |||||||||||| ~ ~ ~> Current number 2: CUBE(2) = 8
 ----> Current number 30: square(30) = 900
 |||||||||||| ~ ~ ~> Current number 5: CUBE(5) = 125
 ----> Current number 10: square(10) = 100
 |||||||||||| ~ ~ ~> Current number 10: CUBE(10) = 1000
 ----> Current number 9: square(9) = 81
 ----> Current number 17: square(17) = 289
 |||||||||||| ~ ~ ~> Current number 11: CUBE(11) = 1331
 ----> Current number 20: square(20) = 400
 ----> Current number -30: square(-30) = 900
 |||||||||||| ~ ~ ~> Current number 12: CUBE(12) = 1728
 |||||||||||| ~ ~ ~> Current number 15: CUBE(15) = 3375
 |||||||||||| ~ ~ ~> Current number 8: CUBE(8) = 512
 |||||||||||| ~ ~ ~> Current number 77: CUBE(77) = 456533
 |||||||||||| ~ ~ ~> Current number -39: CUBE(-39) = -59319
>> Tổng thời gian: 3


```

- *Xử lý tài nguyên chung & Apply cơ chế Lock*
```shell
tdc@tdc:~/python/multi-threading$ python3 ...
------------------------------------------------------------------------

```

- *Tạo Daemond Thread để tuỳ biến việc stop thread an toàn*
```shell
tdc@tdc:~/python/multi-threading$ python3 ...
------------------------------------------------------------------------

```