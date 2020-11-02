import os
from os import listdir, makedirs
from os.path import isdir
from shutil import copyfile

DIR_PATH = os.getcwd()

# 폴더의 파일 목록 조회
orig_dir = f"{DIR_PATH}\\scandata\\"
out_dir = f"{DIR_PATH}\\organized\\"

file_list = listdir(orig_dir)
# print(file_list)

# 파일명 분석
for f_name in file_list:
    f_date = f_name[5:-4]
    f_date = f_date.split('_')
    f_date = f_date[0]
    f_date = f_date.split('-')

    year = f_date[0]
    month = f_date[1]
    day = f_date[2]
    # print(year, month, day)

    # 폴더 생성
    target_dir = out_dir + year + '\\' + month + '\\' + day
    if not isdir(target_dir):
        makedirs(target_dir)
    
    # 파일 복사
    copyfile(orig_dir+f_name, target_dir+'\\'+f_name)
    print(orig_dir+f_name + " => " + target_dir + "\\" + f_name)