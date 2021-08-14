from distutils.dir_util import copy_tree
from shutil import copy

modules = {
    'tabs/':'build/python/tabs/',
    'calculator/':'build/python/calculator/',
    #'base/python':'build/python',
    #'base/mathjax2':'build/mathjax2',
    }

files = {
    'main.py':'build/',
    'i.ico':'build/',
    'pix.png':'build/',
    'pk.png':'build/',
    'base/app.vbs':'build/',
    'base/__init__.py':'build/',
    'base/Problematika.bat':'build/'
}


for module, dst in modules.items():
    print(f'Module {module} added to {dst}')
    copy_tree(module, dst)

for file, dst in files.items():
    print(f'File {file} added to {dst}')
    copy(file, dst)