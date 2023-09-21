import datetime
# import 가 여러 개 있으면 앞에 화살표 버튼 눌러서 접어 놓을 수 있다.


import datetime
# 파이썬 내부 datetime 이라는 함수를 가져온다.

# 현재 날짜
now = datetime.date.today()
print(now)
print(now.year)
print(now.month)
print(now.day)

# 지정된 날짜
date = datetime.date(2023, 12, 4)
print(date)

# 현재 시간
now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

# 지정된 시간
date = datetime.datetime(2023, 12, 4, 12, 00, 00)
print(date)