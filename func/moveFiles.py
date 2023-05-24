import os
import shutil
from .searchFiles import searchFiles
# import .searchFiles

def moveFiles(source_folder, target_folder, target_name):
    found_files = searchFiles(source_folder, target_name)
    if found_files:
        print("File ditemukan. Memindahkan file...")
        if not os.path.exists(target_folder):
            os.makedirs(target_folder) 

        for file_path in found_files:
            file_name = os.path.basename(file_path)
            target_path = os.path.join(target_folder, file_name)
            shutil.move(file_path, target_path)
        print("Pemindahan file selesai.")
