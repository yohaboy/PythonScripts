import os
import shutil
from datetime import datetime

source_folder = './important_files'
backup_root = './backups'

date_str = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
backup_folder = os.path.join(backup_root, f'backup_{date_str}')

shutil.copytree(source_folder, backup_folder)

print(f'Backup created: {backup_folder}')

