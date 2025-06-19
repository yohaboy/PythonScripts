import os
import shutil

folder_path = './my_folder'

file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.mov', '.avi'],
}

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        ext = os.path.splitext(filename)[1].lower()
        moved = False
        for folder, extensions in file_types.items():
            if ext in extensions:
                dest_folder = os.path.join(folder_path, folder)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder, filename))
                moved = True
                break
        if not moved:
            other_folder = os.path.join(folder_path, 'Others')
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, filename))

print('Files organized by type.')
