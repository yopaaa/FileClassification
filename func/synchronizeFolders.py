import os
import shutil
from .findAllFiles import findAllFiles

def synchronizeFolders(source_folder_path, target_folder_path):
    contents = []
    resultFindSourceFolder = findAllFiles(source_folder_path)
    resultFindTargetFolder = findAllFiles(target_folder_path)
        
    for file_path in resultFindSourceFolder:
        extract_des_path = file_path.replace(source_folder_path + '/', '')
        destination_path = os.path.join(target_folder_path, extract_des_path)
        
        if destination_path not in resultFindTargetFolder:
            print(destination_path)
            print(file_path)
            contents.append(file_path)
    
    return contents


def synchronize_and_copy_files(synchronized_contents,source_folder, target_folder):
    for file_path in synchronized_contents:
        destination_path = file_path.replace(source_folder, target_folder)
        destination_folder = os.path.dirname(destination_path)

        # Membuat folder tujuan jika belum ada
        os.makedirs(destination_folder, exist_ok=True)

        # Menyalin file dari folder sumber ke folder tujuan
        shutil.copy2(file_path, destination_path)

    print("Sinkronisasi dan penyalinan file selesai.")
