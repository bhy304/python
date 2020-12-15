import os
from openpyxl import load_workbook, Workbook
from datetime import datetime 

xlsx = Workbook()
sheet = xlsx.active    
sheet.freeze_panes = 'A2'

today = datetime.today().strftime("%Y%m%d");
today_time = datetime.today().strftime("%H%M%S");

sheet.append(['폴더명','txt_파일명', '0(dish)', 'xmin', 'ymin', 'xmax', 'ymax','1(food)', 'xmin', 'ymin', 'xmax', 'ymax'])     

txt_contents = []
for root, dirs, files in os.walk('./auto/temp/txt'):
    for fname in files:
        file_path = os.path.join(root, fname)
        with open(file_path, 'r', encoding='utf-8') as f:
            contents = f.readlines()
            folder_name = os.path.split(os.path.dirname(file_path))[1] 
            first_field = contents[0].strip().split(' ')
            second_field = contents[1].strip().split(' ')
            # print(first_field, second_field)
            # print(folder_name)
            # print(folder_name, fname, first_field, second_field)
            sheet.append([folder_name, fname, first_field[0], first_field[1], first_field[2], first_field[3], first_field[4], second_field[0], second_field[1], second_field[2], second_field[3], second_field[4]])
            # print('{0} {1} {2}'.format(fname, contents[0], contents[1]))
        f.close()

xlsx.save(f'./auto/Check_{today}_{today_time}.xlsx')
xlsx.close()