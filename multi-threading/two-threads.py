import time
from threading import Thread


print('Ví dụ về xử lý data luồng (2 threads cho 2 functions tính toán) ...')
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

        print(' |||||||||||| ~ ~ ~> Current number %d: CUBE(%d) = %d' % (curNum, curNum, curNum * curNum * curNum))


try:
    startTime = time.time()

    # Chuẩn bị params
    arrCalSquare = (2, 6, 7, 30, 10, 9, 17, 20, -30)
    arrCalCube = [1, 2, 5, 10, 11, 12, 15, 8, 77, -39]

    # Tạo 2 Threads
    thread1 = Thread(target=cal_square, args=(arrCalSquare, ))
    thread2 = Thread(target=cal_cube, args=(arrCalCube, ))

    # Start 2 Threads
    thread1.start()
    thread2.start()

    # Yêu cầu chờ cho đến khi 2 Threads này kết thúc thì mới kết thúc chương trình
    thread1.join()
    thread2.join()

    endTime = time.time() - startTime
    print('>> Tổng thời gian: %d' % endTime)
except Exception as ex:
    print('.... Ngoại lệ xảy ra : ' + str(ex))

