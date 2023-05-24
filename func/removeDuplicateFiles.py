import os

def removeDuplicateFiles(duplicate_files_dict):
    for size, files in duplicate_files_dict.items():
        if len(files) > 1:
            while len(files) > 1:
                file_path = files.pop()
                if os.path.isfile(file_path):
                    try:
                        os.remove(file_path)
                        print(f"File dihapus: {file_path}")
                    except OSError as e:
                        print(f"Terjadi kesalahan saat menghapus file: {file_path}")
                        print(e)
                else:
                    print(f"Path tidak valid atau bukan file: {file_path}")