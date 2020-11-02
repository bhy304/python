import os
PATH = os.path.dirname(os.path.abspath(__file__))

f = open(f'{PATH}/test.txt', 'r+', encoding='UTF8')
contents = f.read()
print(contents)
f.write('문자열 추가 테스트\n')
f.seek(0) #ㅇ 원하는 경로의 파일이 가지고 있는 현재 위치를 변경
contents = f.read()
print(contents)
f.close()