from calculator.gerar_calc import gerar_calculo_produto_vetorial
from tkinter import *
from tkinter import ttk

from tabs import *
from calculator.operations import calcularProdutoVetorial


def criarTab(tab_control):
    global linhas, lbl_resultado

    linhas = list()
    lbl_font = ('arial', 11, 'bold')

    produto_vetorial = ttk.Frame(tab_control)
    produto_vetorial.grid(sticky='NSEW')
    produto_vetorial.columnconfigure((0,1,2), weight=1)
    produto_vetorial.rowconfigure((0,1,2,3,4, 5), weight=1)

    tab_control.add(produto_vetorial, text='Produto Vetorial')
    
    #LINHA 0
    linhas.append(criarLinhaDeResultado(produto_vetorial))
    #LINHA 1
    linhas.append(criarLinhaDeTexto(produto_vetorial, 'Digite as coordenadas do primeiro vetor:', lbl_font, row = 1, columnspan=3))
    #LINHA 2
    linhas.append(criarLinhaDeCoordenadas(produto_vetorial, row = 2))
    #LINHA 3
    linhas.append(criarLinhaDeTexto(produto_vetorial, 'Digite as coordenadas do segundo vetor:', lbl_font, row = 3, columnspan=3))
    #LINHA 4
    linhas.append(criarLinhaDeCoordenadas(produto_vetorial, row = 4))
    #LINHA 5
    linhas.append(criarBotãoCalcular(produto_vetorial, 5, lambda: calcular(tab_control)))



def calcular(widget):
    v = obterVetor(linhas[2])
    u = obterVetor(linhas[4])
    linhas[0]['resultado'].set(f'{calcularProdutoVetorial(v, u)}')
    gerar_calculo_produto_vetorial(v, u)

    # Reload the browser after generating the calc
    Tk._root(widget).winfo_children()[2].winfo_children()[0].browser.Reload()

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
