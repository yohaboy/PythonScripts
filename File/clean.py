#python script for cleaning

import os

folder_path = './my_folder'

for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        if os.path.isfile(file_path) and os.path.getsize(file_path) == 0:
            os.remove(file_path)
            print(f'Deleted empty file: {file_path}')

print('Done! All empty files removed.')

