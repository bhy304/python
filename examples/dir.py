import os
from os import listdir

DIR_PATH = os.getcwd()
PATH = os.path.dirname(os.path.abspath(__file__))
print(PATH)

write_file = open(f'{PATH}/statistics.csv', 'w', encoding='utf-8')
write_file.write('년월,매출\n') # csv header

csv_files = f'{DIR_PATH}/csv_files/'
file_list = listdir(csv_files)
file_list.sort()

for f_name in file_list:
    if f_name[-3:] != 'csv':
        continue
    sum_value = 0
    f = open(csv_files + f_name, 'r')

    while True:
        row = f.readline()
        if not row:
            break
        data = row.split(',')
        if data[1].isdigit():
            sum_value = sum_value + int(data[1])
    
    write_file.write('%s,%d\n'%(f_name[:7], sum_value))
    f.close()

write_file.close()