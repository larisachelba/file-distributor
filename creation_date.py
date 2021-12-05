import os
from datetime import datetime
from time import strftime

from size import get_list_of_files


def get_creation_date():
    all_files = get_list_of_files('filesystem')
    all_files_creation_date = {}
    for file in all_files:
        file_creation_date = datetime.fromtimestamp(os.path.getctime(file)).strftime(format='%m/%d/%Y, %H:%M:%S')
        all_files_creation_date[file] = file_creation_date
    return all_files_creation_date


print(get_creation_date())

