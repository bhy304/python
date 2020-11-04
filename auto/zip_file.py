import os
import glob
import zipfile
import fnmatch

file_path = os.path.dirname(os.path.abspath(__file__))

zip_list = glob.glob(f'{file_path}/data/*')

for zip_fname in os.listdir('./auto/data'):
    if fnmatch.fnmatch(zip_fname, '*_txt.zip'):
        print('_txt.zip: ', zip_fname)
    elif fnmatch.fnmatch(zip_fname, '*_xml.zip'):
        print('_xml.zip: ', zip_fname)

'''
ROOT_PATH = os.getcwd()
CUR_PATH = os.path.dirname(os.path.abspath(__file__))

file_path = ROOT_PATH + '\\data\\*'
# zip_file_list = glob.glob(zip_file_path)
# zip_file_name = os.listdir(f'{ROOT_PATH}/data')

# for fname in zip_file_name:
#     for i in zip_file_list:
#         with zipfile.ZipFile(i, 'a') as existing_zip:
#             print(existing_zip)
            # if i[-7:-4] == 'txt':
            #     existing_zip.extractall(f'{ROOT_PATH}/temp/{fname[:-8]}/txt')
            # else:
            #     existing_zip.extractall(f'{ROOT_PATH}/temp/{fname[:-8]}/xml')
'''