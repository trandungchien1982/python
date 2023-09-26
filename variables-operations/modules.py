
from math import sqrt, pow
import os, sys

print ('Tìm hiểu về xử lý các modules cơ bản như math/os/file/...')

# Xử lý toán học
print('- Xử lý toán học ')
x = 9
print(' - x = ' + str(x) + " >> sqrt(x): " + str(sqrt(x)) + ', pow(x,2): ' + str(pow(x,2)))

# Xử lý OS, System
print('- Xử lý OS, System ')
workPath = os.path.abspath(os.path.join('modules'))
print('   + workPath: ' + workPath)
print('   + sys.path: ' + str(sys.path))

# Xử lý đọc/ghi file
def readFileCustom(fileName: str):
  fileObj = open(fileName)
  strData = fileObj.read()
  fileObj.close()
  return strData

fileName = 'variables.py'
print('- Đọc file & in ra nội dung của file: ' + fileName)
print('    ---------> File content: -----------------------------')
print(readFileCustom(fileName))
print('------------------------------------- KẾT THÚC ĐỌC FILE ...')