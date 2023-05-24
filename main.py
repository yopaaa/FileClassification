import os
import shutil

def search_files(directory, filename):
    matches = []
    if not os.path.exists(directory):
        print('directory doests exits')
        return False

    resultSerch = os.walk(directory)

    for root, _, files in resultSerch:
        for file in files:
            if filename.lower() in file.lower():
                matches.append(os.path.join(root, file))

    return matches

def move_files(source_folder, target_folder, target_name):
    found_files = search_files(source_folder, target_name)
    if found_files:
        print("File ditemukan. Memindahkan file...")
        if not os.path.exists(target_folder):
            os.makedirs(target_folder) 

        for file_path in found_files:
            file_name = os.path.basename(file_path)
            target_path = os.path.join(target_folder, file_name)
            shutil.move(file_path, target_path)
        print("Pemindahan file selesai.")


print('select working tolls')
print('1. search files')
print('2. search and move files')
tools_options = input("select: ")

if tools_options == '1':
    folder_path = input("Masukkan direktori tempat pencarian file: ")
    target_filename = input("Masukkan nama file yang ingin dicari: ")

    found_files = search_files(folder_path, target_filename)

    if found_files:
        print("File ditemukan:")
        for file_path in found_files:
            print(file_path)

elif tools_options == '2':
    source_folder_path = input('Masukan folder sumber: ')  # Ganti dengan path folder sumber
    target_folder_path = input('Masukan folder tujuan: ')  # Ganti dengan path folder tujuan
    target_name = input('masukan nama ataupun extensi file target: ')  # Ganti dengan nama yang ingin Anda cari dan pindahkan

    move_files(source_folder_path, target_folder_path, target_name)
