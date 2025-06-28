import os
import shutil

def organize_images(source_folder, target_folder):
    # Create target folder if it doesn't exist
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    # Loop through all files in the source folder
    for filename in os.listdir(source_folder):
        # Check if the file is an image by extension
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
            source_path = os.path.join(source_folder, filename)
            target_path = os.path.join(target_folder, filename)
            # Move the image to the target folder
            shutil.move(source_path, target_path)

