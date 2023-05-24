from func.searchFiles import searchFiles
from func.moveFiles import moveFiles
from func.findDuplicateFiles import findDuplicateFiles
from func.removeDuplicateFiles import removeDuplicateFiles


print('select working tolls')
print('1. search files')
print('2. search and move files')
print('3. find duplicate files')
tools_options = input("select: ")

if tools_options == '1':
    folder_path = input("Masukkan direktori tempat pencarian file: ")
    target_filename = input("Masukkan nama file yang ingin dicari: ")

    found_files = searchFiles(folder_path, target_filename)

    if found_files:
        print("File ditemukan:")
        for file_path in found_files:
            print(file_path)

elif tools_options == '2':
    source_folder_path = input('Masukan folder sumber: ')
    target_folder_path = input('Masukan folder tujuan: ') 
    target_name = input('masukan nama ataupun extensi file target: ') 

    moveFiles(source_folder_path, target_folder_path, target_name)

elif tools_options == '3':
    target_folder_path = input('Masukan folder tujuan: ') 

    duplicate = findDuplicateFiles(target_folder_path)
    # print(duplicate)
    if duplicate:
        isDeleteDuplicate = input('Apakah kamu ingin menghapus file duplicate(y/n): ')
        if isDeleteDuplicate == 'y':
            removeDuplicateFiles(duplicate)
        else:
            print(duplicate)
    #     for file_path in duplicate:
    #         print(file_path)
