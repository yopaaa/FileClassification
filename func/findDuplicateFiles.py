import os
from collections import defaultdict

def findDuplicateFiles(directory):
    file_sizes = defaultdict(list)
    duplicate_files = {}
    duplicate_files_length = 0
    
    if not os.path.exists(directory):
        print('directory doests exits')
        return False

    # Mengumpulkan ukuran file
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            file_sizes[file_size].append(file_path)

    # Mencari file duplikat berdasarkan ukuran
    for size, files in file_sizes.items():
        if len(files) > 1:
            duplicate_files[size] = files
            duplicate_files_length += len(files)


    if duplicate_files:
        print("File duplikat ditemukan: ", duplicate_files_length)
    else:
        print("Tidak ada file duplikat.")

    return duplicate_files
