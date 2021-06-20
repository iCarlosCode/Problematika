from tkinter import *
from tkinter import ttk

from tabs import *
from calculator.operations import calcularProdutoEscalar


def criarTab(tab_control):
    global linhas, lbl_resultado

    linhas = list()
    lbl_font = ('arial', 11, 'bold')

    produto_escalar = ttk.Frame(tab_control)
    produto_escalar.grid(sticky='NSEW')
    produto_escalar.rowconfigure((0, 1, 2, 3, 4, 5),weight=1)
    tab_control.add(produto_escalar, text='Produto Escalar')

    #LINHA 0
    linhas.append(criarLinhaDeResultado(produto_escalar))
    #LINHA 1
    linhas.append(criarLinhaDeTexto(produto_escalar, 'Digite as coordenadas do primeiro vetor:', lbl_font, row = 1, columnspan=3))
    #LINHA 2
    linhas.append(criarLinhaDeCoordenadas(produto_escalar, row = 2))
    #LINHA 3
    linhas.append(criarLinhaDeTexto(produto_escalar, 'Digite as coordenadas do segundo vetor:', lbl_font, row = 3, columnspan=3))
    #LINHA 4
    linhas.append(criarLinhaDeCoordenadas(produto_escalar, row = 4))
    #LINHA 5
    linhas.append(criarBotãoCalcular(produto_escalar, 5, calcular))

    


def calcular():
    v = obterVetor(linhas[2])
    u = obterVetor(linhas[4])
    linhas[0]['resultado'].set(f'{calcularProdutoEscalar(v, u)}')


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
