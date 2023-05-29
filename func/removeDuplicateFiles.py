import os

def removeDuplicateFiles(duplicate_files_dict):
    for size, files in duplicate_files_dict.items():
        if len(files) > 1:
            while len(files) > 1:
                file_path = files.pop()
                removeFiles(file_path)


def removeFiles(target):
    if os.path.isfile(target):
        try:
            os.remove(target)
            print(f"File dihapus: {target}")
        except OSError as e:
            print(f"Terjadi kesalahan saat menghapus file: {target}")
            print(e)
    else:
        try:
            os.removedirs(target)
            print(f"Directory dihapus: {target}")
        except OSError as e:
            print(f"Terjadi kesalahan saat menghapus Directory: {target}")
            print(e)
