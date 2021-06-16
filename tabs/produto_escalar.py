from tkinter import *
from tkinter import ttk

from tabs import *
from calculator.operations import calcularProdutoEscalar


def criarTab(tab_control):
    global linhas, lbl_resultado

    linhas = list()
    lbl_font = ('arial', 11, 'bold')

    produto_escalar = ttk.Frame(tab_control)
    tab_control.add(produto_escalar, text='Produto Escalar')

    #LINHA 0
    linhas.append(criarLinhaDeTexto(produto_escalar, 'Digite as coordenadas do primeiro vetor:', lbl_font, row = 0, columnspan=3))
    #LINHA 1
    linhas.append(criarLinhaDeCoordenadas(produto_escalar, row = 1))
    #LINHA 3
    linhas.append(criarLinhaDeTexto(produto_escalar, 'Digite as coordenadas do segundo vetor:', lbl_font, row = 2, columnspan=3))
    #LINHA 4
    linhas.append(criarLinhaDeCoordenadas(produto_escalar, row = 3))
    #LINHA 5
    btn_calcular = ttk.Button(produto_escalar, text='Calcular', command=calcular)
    btn_calcular.grid(columnspan = 3, row = 6, sticky='EW')
    #LINHA 7
    btn_mostrar = ttk.Button(produto_escalar, text='Mostrar Cálculo Passo a Passo')
    btn_mostrar.grid(columnspan = 3, row = 7, sticky='EW')
    #LINHA 8
    lbl_resultado = ttk.Label(produto_escalar, text='O resultado é ESSE HEHEHE')
    lbl_resultado.grid(columnspan = 3, row = 8, sticky='EW')


def calcular():
    v = obterVetor(linhas[1])
    u = obterVetor(linhas[3])
    lbl_resultado.configure(text= f'O resultado é: {calcularProdutoEscalar(v, u)}.')


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
