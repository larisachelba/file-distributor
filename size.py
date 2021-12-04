import os
from os import listdir
from shutil import copyfile, copy, rmtree


def get_list_of_files(dir_name):

    list_of_file = os.listdir(dir_name)
    all_files = list()
    for entry in list_of_file:
        full_path = os.path.join(dir_name, entry)
        if os.path.isdir(full_path):
            all_files = all_files + get_list_of_files(full_path)
        else:
            all_files.append(full_path)

    return all_files


def get_all_sizes():
    all_files_size = {}
    all_files = get_list_of_files('filesystem')
    for file in all_files:
        file_size = os.path.getsize(file)
        all_files_size[file] = file_size
    return all_files_size


def separate_files(size):
    d = get_all_sizes()

    smaller_files = []
    bigger_files = []
    for key, value in d.items():
        if value > size:
            bigger_files.append(key)
        else:
            smaller_files.append(key)
    return bigger_files, smaller_files


def create_size_directories():
    try:
        os.mkdir('new_filesystem/bigger_files')
    except:
        print('Directory already exists')
    try:
        os.mkdir('new_filesystem/smaller_files')
    except:
        print('Directory already exists')


def copy_files(size):
    create_size_directories()
    bigger_files, smaller_files = separate_files(size)
    for file in bigger_files:
        copy(file, 'new_filesystem/bigger_files/')
    for file in smaller_files:
        copy(file, 'new_filesystem/smaller_files/')


def delete_old_directories():
    try:
        rmtree('new_filesystem/bigger_files')
    except:
        print('Directory doesn\'t exist')
    try:
        rmtree('new_filesystem/smaller_files')
    except:
        print('Directory does not exist')
