print('Các ví dụ liên quan đến Mapping/Filter ...')
print('--------------------------------------------')

sampleTuple = (1, 2, -5, 3, 11, 9, 30, 22, 15)
lists = list(sampleTuple)


def multiply(x):
  return x * x


print(' - sampleTuple : ' + str(sampleTuple))
print(' - map(multiply, sampleTuple): ' + str(list(map(multiply, sampleTuple))))
print(' - sampleTuple : ' + str(sampleTuple))

multiplyResult2 = map(lambda x: x * x, [-3, 9, 12, 10, 5, 7])
print(' - map(lambda x: x * x, [-3, 9, 12, 10, 5, 7]): ')
print(' ---------------------> ' + str(list(multiplyResult2)))

result2Lists = map(lambda x, y: x + ' ' + y, ['red', 'green', 'blue', 'orange', 'magenta'], ['light', 'medium', 'dark', 'highlight'])
print('Map for 2 lists: ' + str(list(result2Lists)))

print('----------------------------------------------------------')
print('---------- Sample for filter() ...........................')
print(' - original: ' + str(sampleTuple))
resultFilter = filter(lambda item: item % 2 == 0, sampleTuple)
print('----------------------------------------------------------')
print(' - resultFilter: ' + str(list(resultFilter)))