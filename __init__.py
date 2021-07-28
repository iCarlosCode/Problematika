import os
from urllib.request import urlopen
from urllib.error import URLError
import json
from tkinter import messagebox as msg
from tkinter import *
import zipfile
from tqdm import tqdm
from distutils.dir_util import copy_tree
from shutil import rmtree


__version__ = 1.1

def main():

    if check_updates():
        url = 'https://github.com/iCarlosCode/Problematika/archive/refs/heads/update.zip'
        update_app(url)
    
    os.system(f'cmd /c ".\\app.vbs"')
   
def check_updates() -> bool:
    url='https://api.github.com/repos/iCarlosCode/problematika/releases/latest'

    try:
        print('Buscando atualizações...')
        with urlopen(url, timeout=10) as response:
            response_content = response.read()

            response_content.decode('utf-8')
            json_response = json.loads(response_content)
            
            if __version__ < int(json_response['tag_name']):
                print(f'Versão {float(json_response["tag_name"])} disponível!')
                win = Tk()
                result = msg.askyesno('Atualização', 'Há uma nova atualiação disponível, deseja baixá-la?')
                win.destroy()
                return result
            else:
                return False
    except URLError:
        return False

    
def update_app(url='https://github.com/iCarlosCode/Problematika/archive/refs/heads/update.zip'):

    with tqdm(total=100) as pb:
        # Passo 1
        try:
            pb.update(10)
            pb.write('Baixando atualização...')
            with urlopen(url) as response:
                response_content = response.read()
            
                # Passo 2
                pb.update(50)
                pb.write('Salvando arquivos no disco...')
                with open('upd.zip', 'wb') as f:
                    f.write(response_content)
        except URLError:
                
                r = msg.askretrycancel('Erro de Rede', 'Houve um problema ao baixar a atualização. Por favor, verifique a sua conexão com a internet.')
                
                if r is True:
                    return update_app(url)
                else:
                    return False
            
        # Passo 3
        pb.update(75)
        pb.write('Extraindo arquivos...')

        with zipfile.ZipFile('upd.zip', 'r') as zf:
            zf.extractall()

        copy_tree('Problematika-update/', '')
        rmtree('Problematika-update', ignore_errors=True)
        rmtree('run.bat', ignore_errors=True)
        os.remove('upd.zip')

        pb.update(100)
        print('Calculadora atualizada!')
        return True


if __name__ == "__main__":
    main()
    
    