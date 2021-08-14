import os
from urllib.request import urlopen
from urllib.error import URLError
import json
from tkinter import messagebox as msg
from tkinter import *
import zipfile
from tqdm import tqdm


__version__ = 2.0

def main():
    response = check_updates()
    if response is not False:
        update_app(response)
    
    os.system(f'cmd /c ".\\app.vbs"')
   
def check_updates():
    "Checks for updates; return download_url if an update is found, otherwise return False"
    url='https://api.github.com/repos/iCarlosCode/problematika/releases/latest'

    try:
        print('Buscando atualizações...')
        with urlopen(url, timeout=10) as response:
            response_content = response.read()

            response_content.decode('utf-8')
            json_response = json.loads(response_content)
            download_url = [a['browser_download_url'] for a in json_response['assets'] if a['name'] == 'update.zip']

            if __version__ < float(json_response['tag_name']):
                print(f'Versão {float(json_response["tag_name"])} disponível!')
                win = Tk()
                result = msg.askyesno('Atualização', 'Há uma nova atualiação disponível, em geral atualizações demoram menos de 30 segundos, deseja baixá-la?')
                win.destroy()
                return result if result is False else (download_url[0] if download_url else False) 
            else:
                return False
    except URLError:
        return False

    
def update_app(url):

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

        os.remove('upd.zip')

        pb.update(100)
        print('Calculadora atualizada!')
        return True


if __name__ == "__main__":
    main()
    
    
