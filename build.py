from distutils.dir_util import copy_tree
from shutil import copy

modules = {
    'tabs/':'build/python/tabs/',
    'calculator/':'build/python/calculator/'
    }

files = {
    'main.py':'build/'
}


for module, dst in modules.items():
    print(f'Module {module} added to {dst}')
    copy_tree(module, dst)

for file, dst in files.items():
    print(f'File {file} added to {dst}')
    copy(file, dst)