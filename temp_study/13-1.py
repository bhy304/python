from datetime import datetime

today = datetime.now()
# print(today.year) # 년
# print(today.month) # 월
# print(today.day) # 일
# print(today.hour) # 시
# print(today.minute) # 분
# print(today.second) # 초

# print(today.strftime('%Y-%m-%d %H:%M:%S'))

print(today.strftime('%a')) # Mon
print(today.strftime('%A')) # Monday
print(today.strftime('%w')) # 1 요일(숫자로 표현)
print(today.strftime('%d')) # 02 일
print(today.strftime('%b')) # Nov
print(today.strftime('%B')) # November
print(today.strftime('%m'))
print(today.strftime('%y'))
print(today.strftime('%Y'))
print(today.strftime('%H')) # 시(24시간 표현)
print(today.strftime('%I')) # 시(12시간 표현)
print(today.strftime('%p')) # PM
print(today.strftime('%M'))
print(today.strftime('%S'))
print(today.strftime('%f')) # 마이크로 초



