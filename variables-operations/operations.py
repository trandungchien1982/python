print('Thử nghiệm các operations trong Python ...')
print('Vd như : if/else loop/while/for switch/case ...')

print('+ Điều kiên if .. else ')
x = 10
y = 20
if 1 == 2:
  print('  - OK, thỏa đk if 1 == 2')
else:
  print('  - OK, KHÔNG thỏa đk if 1 == 2')

if x != y:
  print('  - x == ' + str(x))
  print('  - y == ' + str(y))
  print('  -> OK. Thỏa điều kiện x != y')

if x < 0:
  print('  - OK thỏa đk x < 0')
elif x < 5:
  print('  - OK thỏa đk x < 5')
elif x < 10:
  print('  - OK thỏa đk x < 10')
else:
  print('  - OK thỏa đk ngược lại với x < 0, x < 5, x < 10')

print('+ Xử lý vòng lặp for')
for item in [1, 2, 3, 'Value 01', True, 'Value 02', 7.89, False]:
  print('  - Current item: ' + str(item))
  if item == 7.89:
    print('    => Stop for() because item == 7.89')
    break;

print('+ Xử lý vòng lặp while')
i = 10
while i > 0:
  print('  - Current value: ' + str(i))
  if i < 5:
    print('   => Stop while() because i < 5')
    break;
  
  i -= 1

print('+ Xử lý Exception ')
testVal = 0
try:
  print("Bat dau khoi try..except..")
  print('Try to print value of 6/testVal: ' + str(6 / testVal))
  print('Ket thuc khoi try..except.. ')
except ZeroDivisionError:
  print('   => Loi ZeroDivisionError xảy ra ...')

print('+ Switch case bằng cách sử dụng Dictionary/Map : ')
print(' (TODO: Sẽ tìm hiểu chi tiết sau ...)')

print('+ Xử lý Exception (multiples) + finally')
testVal2 = 0
try:
  print('Bat dau khoi try..except.. tiep theo')
  print('Try to print value of 10/testVal: ' + str(10 / testVal2))
  print('Ket thuc khoi try..except..finally')
except RuntimeError:
  print('     => Lỗi RuntimeError')
except ZeroDivisionError:
  print('     => Lỗi ZeroDivisionError xảy ra cho mục 2')
finally:
  print(' .... Khối lệnh finally ...')


def function01():
  print(' .... This is the function01')
  return 'Value 01'


def function02():
  print(' .... This is the second function02')
  return 'Value 02'


def function03():
  print(' .... This is the THIRD function03')
  return 'Value 03'


swCaseMap = {
  'TH01': function01,
  'TH02': function02,
  'TH03': function03
}

print('  - TH thu 01: ' + str(swCaseMap.get('TH01', 'khong ro nua')))
print('  - ' + str(swCaseMap.get('TH02', 'khong ro nua')))
