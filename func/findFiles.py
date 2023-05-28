import os

def findFiles(directory, filename):
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
