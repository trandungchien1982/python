print('Các ví dụ liên quan đến function() ...')
print('--------------------------------------------')

print('Khai báo & gọi hàm')


def function01():
  return 'Function01 - VALUE'


def function02():
  return 'Function02-CALL: ' + function01()


def function03(x: str, y: float):
  print(' - x value: ' + x)
  print(' - y value: ' + str(y))
  return 'Value of function03'


def functionFinal(xVal: str, yVal: float):
  switchCaseMap = {
    'TH01': function01(),
    'TH02': function02(),
    'TH03': function03(xVal, yVal)
  }
  
  strSelection = 'TH03';
  resultSw = switchCaseMap.get(strSelection, 'DEFAULT CASE - NoAction ...')
  print(' ---> Gia tri resultSw: ' + resultSw)


print('The result of function2(): ' + function02())
print('The result of function03(): ' + function03('GT001', 12))

# Goi function functionFinal()
print('---------------------------------------- ')
print("Goi ham functionFinal('Gia tri X', 12.34)')")
functionFinal('Gia tri X', 12.34)
