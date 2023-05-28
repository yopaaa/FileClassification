import os

def findAllFiles(folder_path):
    contents = []
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            contents.append(file_path)
    return contents


