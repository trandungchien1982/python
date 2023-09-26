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

# Ví dụ [02.Variables+Operations]
==============================================================

**Ta sẽ tạo 1 App Python mẫu với các mục liên quan đến sử dụng biến & các thao tác:**<br/>
- string/number/tuple/dictionary/...
- if/else/for/while/switch/case/...
- map+filter trên lists
- sử dụng modules cơ bản thông qua import library
- các thao tác cơ bản trên string/lists

**Nguồn tham khảo**
- https://toidicode.com/series/python-co-ban
- https://www.scaler.com/topics/switch-case-in-python/

**Kết quả thực thi**<br/>
```shell
tdc@tdc:~/python/variables-operations$ python3 variables.py 
------------------------------------------------------------------------
Thử nghiệm với các biến trong Python ...
Chào ngày mới ...
In ra các biến cơ bản ...
+ Number : 
  x = 10
  y = 20.14
+ String: 
 - Val01 = Mỗi năm đến hè lòng man mác buồn, type: <class 'str'>
 - Val02 = Chín mươi ngày qua chứa chan tình thương
 - Val03 = Xin chào Paul, bạn sắp sửa bước qua tuổi 45 vào năm 2020
+ List: 
 - list01 = [10, 20, 30.12, 'Test 01', 'Test 02'], type: <class 'list'>
+ Tuple: 
 - Tuple01: ('Pair01 value', 20, 'Pair 03 value', 10.25), type: <class 'tuple'>
 - Tuple02: ('Index 01', 'Index 02')
 - Tuple03 = Tuple01 + Tuple02 = ('Pair01 value', 20, 'Pair 03 value', 10.25, 'Index 01', 'Index 02')
+ Dictionary/Map: 
 - Map01: {'key01': 'Value 01', 'key02': True, 'key03': False, 'key04': 20.17, 'key05': 100}, type: <class 'dict'>
+ Format string/numbers/...
Format string: [Chuoi so 01], integer value: 123, float value: 45.670000
```

```shell
tdc@tdc:~/python/variables-operations$ python3 operations.py
-----------------------------------------------------------------
Thử nghiệm các operations trong Python ...
Vd như : if/else loop/while/for switch/case ...
+ Điều kiên if .. else 
  - OK, KHÔNG thỏa đk if 1 == 2
  - x == 10
  - y == 20
  -> OK. Thỏa điều kiện x != y
  - OK thỏa đk ngược lại với x < 0, x < 5, x < 10
+ Xử lý vòng lặp for
  - Current item: 1
  - Current item: 2
  - Current item: 3
  - Current item: Value 01
  - Current item: True
  - Current item: Value 02
  - Current item: 7.89
    => Stop for() because item == 7.89
+ Xử lý vòng lặp while
  - Current value: 10
  - Current value: 9
  - Current value: 8
  - Current value: 7
  - Current value: 6
  - Current value: 5
  - Current value: 4
   => Stop while() because i < 5
+ Xử lý Exception 
Bat dau khoi try..except..
   => Loi ZeroDivisionError xảy ra ...
+ Switch case bằng cách sử dụng Dictionary/Map : 
 (TODO: Sẽ tìm hiểu chi tiết sau ...)
+ Xử lý Exception (multiples) + finally
Bat dau khoi try..except.. tiep theo
     => Lỗi ZeroDivisionError xảy ra cho mục 2
 .... Khối lệnh finally ...
  - TH thu 01: <function function01 at 0x7f07c41661f0>
  - <function function02 at 0x7f07c4166280>
```

```shell
tdc@tdc:~/python/variables-operations$ python3 strings.py
-----------------------------------------------------------------
Các ví dụ liên quan đến strings ...
--------------------------------------------
Chuỗi ví dụ mẫu : strSample
một chuỗi ví dụ mẫu dành cho chúng ta
 - strSample.capitalize(): Một chuỗi ví dụ mẫu dành cho chúng ta, length = 37
 - strSample.center(100): [                một chuỗi ví dụ mẫu dành cho chúng ta                 ]
 - strSample.center(100, '*')****************một chuỗi ví dụ mẫu dành cho chúng ta*****************]
 ------------------------------
 - strSample.endswith("chúng ta"): True
 - strSample.find("ví dụ mẫu"): 10
 - strSample.find("đường xưa"): -1
 - "123abcEFG".isalnum(): True
 - "123abcEFG".isalpha(): False
 - "012345".isdigit(): True
 - strSample.islower(): True
 - strSample.isupper(): False
 - "012345".isnumeric(): True
 - "12345".isnumeric(): True
 - strSample.istitle(): False
 - strSample.join(["{item01}", "{item02}", "{item03}"]): {item01}một chuỗi ví dụ mẫu dành cho chúng ta{item02}một chuỗi ví dụ mẫu dành cho chúng ta{item03}
 - strSample.ljust(100,"+" ): một chuỗi ví dụ mẫu dành cho chúng ta+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 - strSample.r(100,"+" ): +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++một chuỗi ví dụ mẫu dành cho chúng ta
 ------------------------------------------
 - strSample.upper(): MỘT CHUỖI VÍ DỤ MẪU DÀNH CHO CHÚNG TA
 - strSample.title(): Một Chuỗi Ví Dụ Mẫu Dành Cho Chúng Ta
```

```shell
tdc@tdc:~/python/variables-operations$ python3 modules.py
-----------------------------------------------------------------
Tìm hiểu về xử lý các modules cơ bản như math/os/file/...
- Xử lý toán học 
 - x = 9 >> sqrt(x): 3.0, pow(x,2): 81.0
- Xử lý OS, System 
   + workPath: /home/tdc/python/variables-operations/modules
   + sys.path: ['/home/tdc/python/variables-operations', '/usr/lib/python38.zip', '/usr/lib/python3.8', '/usr/lib/python3.8/lib-dynload', '/home/tdc/.local/lib/python3.8/site-packages', '/usr/local/lib/python3.8/dist-packages', '/usr/lib/python3/dist-packages']
- Đọc file & in ra nội dung của file: variables.py
    ---------> File content: -----------------------------
print('Thử nghiệm với các biến trong Python ...')
print('Chào ngày mới ...')

print('In ra các biến cơ bản ...')
print('+ Number : ')
x = 10
y = 20.14
print('  x = ' + str(x))
print('  y = ' + str(y))

print('+ String: ')
strVal01 = 'Mỗi năm đến hè lòng man mác buồn'
strVal02 = 'Chín mươi ngày qua chứa chan tình thương'
strName1 = 'Paul'
strAge1 = 25
strVal03 = 'Xin chào %s, bạn sắp sửa bước qua tuổi %d vào năm %d' % (strName1, 45, 2020)
print(' - Val01 = ' + strVal01 + ', type: ' + str(type(strVal01)))
print(' - Val02 = ' + strVal02)
print(' - Val03 = ' + strVal03)

print('+ List: ')
list01 = [10, 20, 30.12, 'Test 01', 'Test 02']
print(' - list01 = ' + str(list01) + ', type: ' + str(type(list01)))

print('+ Tuple: ')
tuple01 = ('Pair01 value', 20, 'Pair 03 value', 10.25)
tuple02 = ('Index 01', "Index 02")
print(' - Tuple01: ' + str(tuple01) + ', type: ' + str(type(tuple01)))
print(' - Tuple02: ' + str(tuple02))
print(' - Tuple03 = Tuple01 + Tuple02 = ' + str(tuple01 + tuple02))

print('+ Dictionary/Map: ')
map01 = {
  'key01': 'Value 01',
  'key02': True,
  'key03': False,
  'key04': 20.17,
  'key05': 100,
}

print(' - Map01: ' + str(map01) + ', type: ' + str(type(map01)))

print('+ Format string/numbers/...')
print('Format string: %s, integer value: %d, float value: %f' % ('[Chuoi so 01]', 123, 45.67))

------------------------------------- KẾT THÚC ĐỌC FILE ...
```


```shell
tdc@tdc:~/python/variables-operations$ python3 lists.py
-----------------------------------------------------------------
Các ví dụ liên quan đến Lists ...
--------------------------------------------
 - sampleTuple : (1, 2, -5, 3, 11, 9, 30, 22, 15)
 - lists: [1, 2, -5, 3, 11, 9, 30, 22, 15], len = 9
 - max(lists): 30
 - min(lists): -5
 - lists.append(100): [1, 2, -5, 3, 11, 9, 30, 22, 15, 100]
--------------------------------------------
 - lists.extend((77, 88, 99)): 
 - lists.extend((111, 222, 333)): 
 - [1, 2, -5, 3, 11, 9, 30, 22, 15, 100, 77, 88, 99, 111, 222, 333]
--------------------------------------------
 - lists.insert(2, 10000): [1, 2, 10000, -5, 3, 11, 9, 30, 22, 15, 100, 77, 88, 99, 111, 222, 333]
--------------------------------------------
 - lists.reverse(): [333, 222, 111, 99, 88, 77, 100, 15, 22, 30, 9, 11, 3, -5, 10000, 2, 1]
--------------------------------------------
 - lists.remove(10000): [333, 222, 111, 99, 88, 77, 100, 15, 22, 30, 9, 11, 3, -5, 2, 1]
--------------------------------------------
 - lists.pop(): 333, lists = [222, 111, 99, 88, 77, 100, 15, 22, 30, 9, 11, 3, -5, 2, 1]
--------------------------------------------
 - lists.sort(): [-5, 1, 2, 3, 9, 11, 15, 22, 30, 77, 88, 99, 100, 111, 222]
--------------------------------------------
 - lists.clear(): []
```


```shell
tdc@tdc:~/python/variables-operations$ python3 functions.py
-----------------------------------------------------------------
Các ví dụ liên quan đến function() ...
--------------------------------------------
Khai báo & gọi hàm
The result of function2(): Function02-CALL: Function01 - VALUE
 - x value: GT001
 - y value: 12
The result of function03(): Value of function03
---------------------------------------- 
Goi ham functionFinal('Gia tri X', 12.34)')
 - x value: Gia tri X
 - y value: 12.34
 ---> Gia tri resultSw: Value of function03
```



```shell
tdc@tdc:~/python/variables-operations$ python3 map+filter.py
-----------------------------------------------------------------
Các ví dụ liên quan đến Mapping/Filter ...
--------------------------------------------
 - sampleTuple : (1, 2, -5, 3, 11, 9, 30, 22, 15)
 - map(multiply, sampleTuple): [1, 4, 25, 9, 121, 81, 900, 484, 225]
 - sampleTuple : (1, 2, -5, 3, 11, 9, 30, 22, 15)
 - map(lambda x: x * x, [-3, 9, 12, 10, 5, 7]): 
 ---------------------> [9, 81, 144, 100, 25, 49]
Map for 2 lists: ['red light', 'green medium', 'blue dark', 'orange highlight']
----------------------------------------------------------
---------- Sample for filter() ...........................
 - original: (1, 2, -5, 3, 11, 9, 30, 22, 15)
----------------------------------------------------------
 - resultFilter: [2, 30, 22]
```