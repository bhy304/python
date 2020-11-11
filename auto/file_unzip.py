import os
import glob
from zipfile import ZipFile
from openpyxl import load_workbook, Workbook

def unzip_file():
    txt_file_list = glob.glob('./auto/txt/*')
    xml_file_list = glob.glob('./auto/xml/*')

    if len(txt_file_list) != len(xml_file_list):
        print('txt: {}, xml: {}'.format(len(txt_file_list), len(xml_file_list)))

    # txt 파일 압축 해제
    for file in txt_file_list:
        folder_name = os.path.basename(file).split('.')[0]
        # print(folder_name)

        with ZipFile(file, 'r',) as zip:
            zip.printdir()

            print(f'Extracting all the files now... {file}')
            zip.extractall(f'./auto/temp/txt/{folder_name}')
            print('TXT DONE!')

    # xml 파일 압축 해제
    '''
    for file in xml_file_list:
        folder_name = os.path.basename(file).split('.')[0]
        # print(folder_name)

        with ZipFile(file, 'r') as zip:
            zip.printdir()

            print(f'Extracting all the files now... {file}')
            zip.extractall(f'./auto/temp/xml/{folder_name}')
            print('XML DONE!')
        '''

if __name__ == '__main__':
    print('실행 중...')
    unzip_file()
    print('ALL DONE!!!!!')