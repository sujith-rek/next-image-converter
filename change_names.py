import os
import re

def change_data_of_file(file_path):
    # read file
    file = open(file_path, 'r')
    data = file.read()
    file.close()

    # change data
    data = re.sub(r'\.png', '.webp', data)
    data = re.sub(r'\.jpeg', '.webp', data)
    data = re.sub(r'\.jpg', '.webp', data)

    # write file
    file = open(file_path, 'w')
    file.write(data)
    file.close()

def change_data_of_dir(dir_path):
    # crawl through all files and folders of dir_path
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.isdir():
                change_data_of_dir(file)
            else:
                change_data_of_file(file)

