import json
import os
from os import listdir, walk
from os.path import isfile, join

f = []
f_system = {}


def pathto_dict(path):
    for (dirpath, dirnames, filenames) in walk(path):
        tree = {"name": dirpath.split('\\')[-1], "type": "folder", "children": []}
        tree["children"].extend([pathto_dict(os.path.join(dirpath, d)) for d in dirnames])
        tree["children"].extend(
            [{"name": f, "type": "file", "size": os.path.getsize(os.path.join(dirpath, f))} for f in filenames])

        return tree


tree = pathto_dict('filesystem')

with open('structure.json', 'w') as file:
    file.write(json.dumps(tree, indent=4))
# onlyfiles    = [f for f in listdir('filesystem')]
# print(onlyfiles)
