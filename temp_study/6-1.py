import os
from openpyxl import load_workbook

ROOT_PATH = os.getcwd()

# result.xlsx를 읽은 후 기본 시트를 선택
xlsx = load_workbook(f'{ROOT_PATH}/examples/result.xlsx', read_only=True)
sheet = xlsx.active

# A1 셀의 데이터를 출력
print(sheet['A1'].value)
# B1 셀의 데이터를 출력
print(sheet['B1'].value)