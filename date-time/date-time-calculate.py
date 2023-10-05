import time
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

print('Ví dụ về xử lý tính toán trên date/time object ...')
print('-------------------------------------------------------')

curDate = date.today()
curDateTime = datetime.now()
futureDateTime = datetime(year=2025, month=6, day=10, hour=5, minute=55, second=10)
curTimeDelta = futureDateTime - curDateTime

print('\n + Thao tác trên date/datetime objects ...')
print('------------------------------------------------')
print('Current date/time/datetime: ...')
print(' -- date: ' + str(curDate))
print(' -- datetime: ' + str(curDateTime))
print(' -- timedelta: ' + str(curTimeDelta))
print(' -- timedelta: ' + str())


print('Tăng lên 1 ngày ...')
print(' -- date(now) + 1d = ', curDate + timedelta(days=1))
print(' -- datetime(now) + 1d = ', curDateTime + timedelta(days=1))

print('Tăng lên 1 tuần ...')
print(' -- date(now) + 1w = ', curDate + timedelta(weeks=1))
print(' -- datetime(now) + 1w = ', curDateTime + timedelta(weeks=1))

print('Tăng lên 1 tháng ...')
print(' -- date(now) + 1month =', curDate + relativedelta(months=1))
print(' -- datetime(now) + 1month =', curDateTime + relativedelta(months=1))

print('Tăng lên 1 năm ...')
print(' -- date(now) + 1year =', curDate + relativedelta(years=1))
print(' -- datetime(now) + 1year =', curDateTime + relativedelta(year=1))

print('\n + Format date/datetime ...')
print('------------------------------------------------')
print(' -- date: ', curDate.strftime('%d-%m-%Y'))
print(' -- date (nicer): ', curDate.strftime('%A, %d-%B-%Y'))
print(' -- date (short): ', curDate.strftime('%a, %d-%b-%Y'))

print(' -- datetime: ', curDateTime.strftime('%d-%m-%Y %H:%M:%S'))
print(' -- datetime(nicer): ', curDateTime.strftime('%A, %d-%B-%Y %H:%M:%S'))
print(' -- datetime(short): ', curDateTime.strftime('%a, %d-%b-%Y %I:%M:%S %p'))
print(' -- datetime(short+TZ): ', curDateTime.strftime('%a, %d-%b-%Y %I:%M:%S %p'))


print('\n + Convert từ string sang date/datetime object ...')
print('-----------------------------------------------------------')
print('TODO: ')


print('\n + Xử lý Timezone, DST ...')
print('-----------------------------------------------------------')
print('TODO: ')
