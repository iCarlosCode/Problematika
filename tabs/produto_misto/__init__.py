from tkinter import *
from tkinter import ttk

from widgets_utils import criarLinhaDeCoordenadas


def criarTab(tab_control):
    linhas = list()

    produto_misto = ttk.Frame(tab_control)
    tab_control.add(produto_misto, text='Produto misto')

    #LINHA 0
    lbl_vetor1 = ttk.Label(produto_misto, text='Digite as coordenadas do primeiro vetor:').grid(row=0)
    #LINHA 1
    linhas.append(criarLinhaDeCoordenadas(produto_misto, row = 1))
    #LINHA 3
    lbl_vetor1 = ttk.Label(produto_misto, text='Digite as coordenadas do primeiro vetor:').grid(row=2)
    #LINHA 4
    linhas.append(criarLinhaDeCoordenadas(produto_misto, row = 3))
    #LINHA 5
    lbl_vetor1 = ttk.Label(produto_misto, text='Digite as coordenadas do primeiro vetor:').grid(row=4)
    #LINHA 5
    linhas.append(criarLinhaDeCoordenadas(produto_misto, row = 5))
    #LINHA 6
    btn_calcular = ttk.Button(produto_misto, text='Calcular')
    btn_calcular.grid(columnspan = 3, row = 6, sticky='EW')
    #LINHA 7
    lbl_resultado = ttk.Label(produto_misto, text='O resultado é ESSE HEHEHE')
    lbl_resultado.grid(columnspan = 3, row = 7, sticky='EW')




if __name__ == '__main__':
    win = Tk()
    win.minsize(600,600)
    win.grid_columnconfigure(0, weight=1)
    win.grid_rowconfigure(0, weight=1)

    #Create Tab Control
    tab_control = ttk.Notebook(win)
    tab_control.grid(sticky='NSEW')

    criarTab(tab_control)

    win.mainloop()
