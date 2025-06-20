import os
import hashlib

folder_path = './my_folder'
hashes = {}

for root, dirs, files in os.walk(folder_path):
    for filename in files:
        file_path = os.path.join(root, filename)
        with open(file_path, 'rb') as f:
            file_hash = hashlib.md5(f.read()).hexdigest()
        if file_hash in hashes:
            print(f'Duplicate found: {file_path} == {hashes[file_hash]}')
        else:
            hashes[file_hash] = file_path

print('Duplicate check complete.')

