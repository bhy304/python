import os 
import glob
from openpyxl import Workbook, load_workbook

ROOT_PATH = os.getcwd() #C:\Users\aithe_백하연\Desktop\python
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__)) #c:\Users\aithe_백하연\Desktop\python\examples

txt_file_list = glob.glob(f'{ROOT_PATH}/txt/*')
xml_file_list = glob.glob(f'{ROOT_PATH}/xml/*')


for idx in range(len(txt_file_list)):
    txt_contents = []
    with open(txt_file_list[idx], 'r', encoding='utf-8') as f:
        contents = f.readlines()
        txt_contents.extend(contents[0].strip().split(' '))
        txt_contents.extend(contents[1].strip().split(' '))
        # print(txt_contents)
    f.close()

    raw_rows = []