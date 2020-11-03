from openpyxl import Workbook, load_workbook
import os

ROOT_PATH = os.getcwd()
CUR_PATH = os.path.dirname(os.path.abspath(__file__))

xlsx = load_workbook(f'{CUR_PATH}\\other.xlsx', data_only=True)
sheet = xlsx.active

sheet.append(['A5-data', 'B5-data', 'C5-data'])
sheet.append(['A6-data', 'B6-data', 'C6-data'])

xlsx.save(f'{CUR_PATH}\\other.xlsx')
xlsx.close()