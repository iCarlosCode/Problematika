from tkinter import *
from tkinter import ttk

from tabs import *
from calculator.operations import calcularProdutoMisto

def criarTab(tab_control):
    global linhas, lbl_resultado

    linhas = list()
    lbl_font = ('arial', 11, 'bold')

    produto_misto = ttk.Frame(tab_control)
    tab_control.add(produto_misto, text='Produto Misto')

    #LINHA 0
    linhas.append(criarLinhaDeResultado(produto_misto))
    #LINHA 1
    linhas.append(criarLinhaDeTexto(produto_misto, 'Digite as coordenadas do primeiro vetor:', lbl_font, row = 1, columnspan=3))
    #LINHA 2
    linhas.append(criarLinhaDeCoordenadas(produto_misto, row = 2))
    #LINHA 3
    linhas.append(criarLinhaDeTexto(produto_misto, 'Digite as coordenadas do segundo vetor:', lbl_font, row = 3, columnspan=3))
    #LINHA 4
    linhas.append(criarLinhaDeCoordenadas(produto_misto, row = 4))
    #LINHA 5
    linhas.append(criarLinhaDeTexto(produto_misto, 'Digite as coordenadas do terceiro vetor:', lbl_font, row = 5, columnspan=3))
    #LINHA 5
    linhas.append(criarLinhaDeCoordenadas(produto_misto, row = 6))
    #LINHA 6
    btn_calcular = ttk.Button(produto_misto, text='Calcular', command=calcular)
    btn_calcular.grid(columnspan = 3, row = 7, sticky='EW')
    

def calcular():
    v = obterVetor(linhas[2])
    u = obterVetor(linhas[4])
    w = obterVetor(linhas[6])
    linhas[0]['resultado'].set(f'{calcularProdutoMisto(v, u, w)}')


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
