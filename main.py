from func.findFiles import findFiles
from func.moveFiles import moveFiles
from func.findDuplicateFiles import findDuplicateFiles
from func.removeDuplicateFiles import removeDuplicateFiles
from func.listFolders import printFolderTree,listFolders
from func.findAllFiles import findAllFiles
from func.synchronizeFolders import synchronizeFolders,synchronize_and_copy_files
import os

tools_options = 0
options = {
    'q': 'exit',
    '1': 'search files',
    '2': 'search and move files',
    '3': 'find duplicate files',
    '4': 'list folders',
    '5': 'sync 2 folders'
}
def clearBash():
    is_clear = input("Apakah kamu ingin membersihkan console? (y/n) >>> ")
    if is_clear == 'n':
        return
    print("\033c")
    return

while tools_options != 'q':

    print('-------select working tolls-------')
    for key, value in options.items():
        print(f'[{key}]. {value}')
        
    tools_options = input(">>> ")
    if tools_options not in options.keys():
        print(tools_options,'not found')
        clearBash()
        
    if tools_options == '1':
        folder_path = os.path.normpath(input("Masukkan direktori tempat pencarian file: "))
        target_filename = os.path.normpath(input("Masukkan nama file yang ingin dicari: "))

        found_files = findFiles(folder_path, target_filename)

        if found_files:
            print("File ditemukan:")
            for file_path in found_files:
                print(file_path)
        else:
            print('files not found')
            
        clearBash()

    elif tools_options == '2':
        source_folder_path = os.path.normpath(input('Masukan folder sumber: '))
        target_folder_path = os.path.normpath(input('Masukan folder tujuan: ')) 
        target_name = os.path.normpath(input('masukan nama ataupun extensi file target: ')) 
        found_files = findFiles(source_folder_path, target_name)

        moveFiles(found_files, target_folder_path, )
        
        clearBash()

    elif tools_options == '3':
        target_folder_path = os.path.normpath(input('Masukan folder tujuan: ')) 

        duplicate = findDuplicateFiles(target_folder_path)
        # print(duplicate)
        if duplicate:
            isDeleteDuplicate = input('Apakah kamu ingin menghapus file duplicate(y/n): ')
            if isDeleteDuplicate == 'y':
                removeDuplicateFiles(duplicate)
            else:
                # print(duplicate)
                for size, file_path in duplicate.items():
                    print(file_path)
        clearBash()
                
    elif tools_options == '4':
        source_folder_path = os.path.normpath(input('Masukan folder sumber: '))
        x = listFolders(source_folder_path)
        is_tree = input('Tampilkan tree? (y/n): ')
        if is_tree == 'n':
            printFolderTree(x)
        else:
            printFolderTree(x, True)
        clearBash()
        
    elif tools_options == '5':
        source_folder_path = os.path.normpath(input('Masukan folder sumber: ')) 
        target_folder_path = os.path.normpath(input('Masukan folder tujuan: '))
        
        print(source_folder_path)
        
        synchronized_contents = synchronizeFolders(source_folder_path, target_folder_path)
        if synchronized_contents:
            print("File yang perlu disinkronisasi:", len(synchronized_contents))
            is_sync = input('Synchronize sekarang? (y/n): ')
            if is_sync== 'n':
                for file_path in synchronized_contents:
                    print(file_path)
            else:
                synchronize_and_copy_files(synchronized_contents, source_folder_path, target_folder_path)
        else:
            print("Tidak ada file yang perlu disinkronisasi.")
        
        clearBash()
        

