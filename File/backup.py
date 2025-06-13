import os
import shutil
from datetime import datetime

source_folder = './my_important_files'
backup_root = './backups'

date_str = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
backup_name = f'backup_{date_str}'
backup_path = os.path.join(backup_root, backup_name)

shutil.make_archive(backup_path, 'zip', source_folder)

print(f'Backup zip created: {backup_path}.zip')

