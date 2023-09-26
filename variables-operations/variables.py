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
