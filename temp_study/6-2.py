from openpyxl import Workbook, load_workbook
import os

CUR_PATH = os.path.dirname(os.path.abspath(__file__))

# 새로운 시트를 가져옴
xlsx = load_workbook(f'{CUR_PATH}\\other.xlsx')
sheet = xlsx['새로운 시트']

# 내용 출력
print(sheet['A1'].value)