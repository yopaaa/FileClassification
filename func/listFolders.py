import os

def listFolders(directory):
    matches = []
    if not os.path.exists(directory):
        print('directory doests exits')
        return False

    resultSerch = os.listdir(directory)
    for item in resultSerch:
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            matches.append(item_path)
        else:
            matches.append(item_path + '/')
    return matches

def printFolderTree(contents,subFolder = False, indent=''):
    if subFolder:
        for item in contents:
            if not item.endswith('/'):
                print(indent + '├── ' + os.path.basename(item))
            else:
                print(indent + '├── /' + os.path.basename(os.path.normpath(item)))
                folder_contents = listFolders(item)  # Menghapus "(Folder)" dari path
                printFolderTree(folder_contents, subFolder, indent + '│   ')
    else:
        for item in contents:
            if not item.endswith('/'):
                print(indent + '├── ' + os.path.basename(item))
            else:
                print(indent + '├── /' + os.path.basename(os.path.normpath(item)))
