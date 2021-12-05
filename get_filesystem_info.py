import json
import os
from datetime import datetime
from os import listdir, walk
from os.path import isfile, join

f = []
f_system = {}


def pathto_dict(path):
    for (dirpath, dirnames, filenames) in walk(path):
        tree = {"name": dirpath.split('\\')[-1], "type": "folder", "children": []}
        tree["children"].extend([pathto_dict(os.path.join(dirpath, d)) for d in dirnames])
        tree["children"].extend(
            [{"name": f,
              "type": "file",
              "date": datetime.fromtimestamp(os.path.getctime(os.path.join(dirpath, f))).strftime(format='%m/%d/%Y, %H:%M:%S'),
              "size": os.path.getsize(os.path.join(dirpath, f))} for f in filenames])

        return tree


tree = pathto_dict('filesystem')

with open('structure.json', 'w') as file:
    file.write(json.dumps(tree, indent=4))
# onlyfiles    = [f for f in listdir('filesystem')]
# print(onlyfiles)
