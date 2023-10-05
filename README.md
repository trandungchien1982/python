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

# Ví dụ [08.DateTime] Xử lý thời gian (date/datetime) ...
==============================================================

**Ta sẽ tạo các Class Python bao gồm:**<br/>
- Xử lý trên date time objects (thêm ngày/tháng/năm/đếm thời gian ...)
- Format date object thành chuỗi thời gian
- Convert từ String sang Date Object dựa trên format chỉ định
- Xử lý Timezone, DST, ...


**Nguồn tham khảo**
- https://quantrimang.com/hoc/datetime-trong-python-162195
- https://bobbyhadz.com/blog/python-add-months-to-date<br/>
	(cần bổ sung thư viện ngoài bằng lệnh `pip3 install python-dateutil`)


**Kết quả thực thi**<br/>
```shell
tdc@tdc:~/python/date-time$ python3 date-time-calculate.py 
-----------------------------------------------------------------
Ví dụ về xử lý tính toán trên date/time object ...
-------------------------------------------------------

 + Thao tác trên date/datetime objects ...
------------------------------------------------
Current date/time/datetime: ...
 -- date: 2023-10-05
 -- datetime: 2023-10-05 23:00:14.701761
 -- timedelta: 613 days, 6:54:55.298239
 -- timedelta: 
Tăng lên 1 ngày ...
 -- date(now) + 1d =  2023-10-06
 -- datetime(now) + 1d =  2023-10-06 23:00:14.701761
Tăng lên 1 tuần ...
 -- date(now) + 1w =  2023-10-12
 -- datetime(now) + 1w =  2023-10-12 23:00:14.701761
Tăng lên 1 tháng ...
 -- date(now) + 1month = 2023-11-05
 -- datetime(now) + 1month = 2023-11-05 23:00:14.701761
Tăng lên 1 năm ...
 -- date(now) + 1year = 2024-10-05
 -- datetime(now) + 1year = 0001-10-05 23:00:14.701761

 + Format date/datetime ...
------------------------------------------------
 -- date:  05-10-2023
 -- date (nicer):  Thursday, 05-October-2023
 -- date (short):  Thu, 05-Oct-2023
 -- datetime:  05-10-2023 23:00:14
 -- datetime(nicer):  Thursday, 05-October-2023 23:00:14
 -- datetime(short):  Thu, 05-Oct-2023 11:00:14 PM
 -- datetime(short+TZ):  Thu, 05-Oct-2023 11:00:14 PM

 + Convert từ string sang date/datetime object ...
-----------------------------------------------------------
TODO: 

 + Xử lý Timezone, DST ...
-----------------------------------------------------------
TODO: 


```
