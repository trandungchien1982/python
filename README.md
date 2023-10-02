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

# Ví dụ [03.OOP] Lập trình hướng đối tượng ...
==============================================================

**Ta sẽ tạo các Class Python mẫu liên quan đến OOP như sau:**<br/>
- Khai báo các biến public/protected/private
- Hàm constructor/destructor
- Kế thừa (multiple)
- Abstract class/methods


**Nguồn tham khảo**
- https://toidicode.com/hoc-python-nang-cao
- https://toidicode.com/class-va-cach-khai-bao-class-trong-python-357.html
- https://toidicode.com/constructor-va-destructor-trong-python-358.html


**Kết quả thực thi**<br/>
- *Basic Class*
```shell
tdc@tdc:~/python/OOP$ python3 basic-class.py
------------------------------------------------------------------------
Các ví dụ liên quan đến Class cơ bản (member/constructor/destructor ...
--------------------------------------------
 - Taọ mới class Person ...
 ---> Hiển thị data của person: <__main__.Person object at 0x1099f7f10>
------> name: EMPTY, age: 10, birthday: 2020-10-10 00:00:00, active: True
---------------------------------
----- Modify data of Person -----
---------------------------------
 ---- person.age =  100
 ---- person.name = Value of Name
 ---> Hiển thị data của person: <__main__.Person object at 0x1099f7f10>
------> name: Value of Name, age: 100, birthday: 2022-07-08 00:00:00, active: False
---------------------------------
--------- Khởi tạo Person2 ------
---------------------------------
 ---> Hiển thị data của person: <__main__.Person object at 0x1099f7d50>
------> name: NAME 2, age: 222, birthday: 2020-10-10 00:00:00, active: True
--------------------------------------------
Tiến hành gọi hàm destrutor() của Person ...Value of Name
------------- END --------------------------
--------------------------------------------
Tiến hành gọi hàm destrutor() của Person ...NAME 2
------------- END --------------------------

```

- *public-protected-private*
```shell
tdc@tdc:~/python/OOP$ python3 public-protected-private.py
----------------------------------------------------------------------------
Các ví dụ liên quan đến public/protected/private variable/methods ...
----------------------------------------------------------------------------

----------------- Show Person (new created) ----------------
   ------> <__main__.Person object at 0x102ddb450>
Value of attr02: Value 02222222222
Value of attr03: Giá trị của Attribute 03
------> name: EMPTY, age: 10, birthday: 2020-10-10 00:00:00, active: True
--------------------------------------------
Tiến hành gọi hàm destrutor() của Person ...EMPTY
------------- END --------------------------


```

- *Kế thừa (nhiều class)*
```shell
tdc@tdc:~/python/OOP$ python3 inherits.py 
------------------------------------------------------------------------
Các ví dụ liên quan đến kế thừa Class ...
--------------------------------------------

----------------- Show all data of Male after being created -----------
------> name: Name of MALE, age: 1234, birthday: 2020-10-10 00:00:00, active: True

----------------- Try to update some properties of Male ---------------
Animal: eat() ...
Animal: sleep() ...
------> name: Update Name of MALE, age: 12, birthday: 2020-10-10 00:00:00, active: False

------------------------------------------------------------------------

Data of Female --------------------------------------
Person: Name of MALE
Person: 10
Animal: eat() ...
Animal: sleep() ...
--- Show Female name: Name of MALE
--- Show Female age: 10
--------------------------------------------
Tiến hành gọi hàm destrutor() của Person ...Update Name of MALE
------------- END --------------------------
--------------------------------------------
Tiến hành gọi hàm destrutor() của Person ...Name of MALE
------------- END --------------------------

```

- *Abstraction*
```shell
tdc@tdc:~/python/OOP$ python3 abstraction.py
------------------------------------------------------------------------
Các ví dụ liên quan đến Abstraction ...
--------------------------------------------
Try to initialize Person ...
Exception occur: ... [Can't instantiate abstract class Person with abstract methods methodAbstract01, methodAbstract02]

------------------------------------------------------------------------

------ RealPerson.methodAbstract01: 
----------------------------------------------------
---- Method Abstract01, name: EMPTY
---- Method Abstract01, age: 10

------ RealPerson.methodAbstract02: 
----------------------------------------------------
---- Method Abstract02, name: EMPTY
---- Method Abstract02, age: 10
--------------- Ket thuc RealPerson ------------------

```