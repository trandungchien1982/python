import time

print('Ví dụ về xử lý data luồng (1 thread + 2 functions tính toán) ...')
print('-------------------------------------------------------')


def cal_square(numbers):
    print('\n--- Hàm cal_square với numbers: ' + str(numbers))
    for curNum in numbers:
        # Ngủ 0.2s
        time.sleep(0.2)

        print(' ----> Current number %d: square(%d) = %d' % (curNum, curNum, curNum * curNum))


def cal_cube(numbers):
    print('\n--- Hàm cal_cube với numbers: ' + str(numbers))
    for curNum in numbers:
        # Ngủ 0.3s
        time.sleep(0.3)

        print(' ===> Current number %d: cube(%d) = %d' % (curNum, curNum, curNum * curNum * curNum))


startTime = time.time()

cal_square((2, 6, 7, 30, 10, 9, 17, 20, -30))
cal_cube([1, 2, 5, 10, 11, 12, 15, 8, 77, -39])

endTime = time.time() - startTime
print('>> Tổng thời gian: %d' % endTime)
