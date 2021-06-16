from tkinter import *
from tkinter import ttk
from webbrowser import open_new_tab

from tabs import *
from calculator.operations import calcularSoma, calcularSubtração, obterVetorDePontos

"""import os

from webbrowser import open_new_tab
open_new_tab(f'{os.getcwd()}\calculo.html')

def ptohtml():
    texto='i'
    calc = open(f'{os.getcwd()}\calculo.html', 'w')
    calc.write(texto)
    calc.close()"""


def criarTab(tab_control):
    global linhas, lbl_resultado, modo, modos

    linhas = list()
    lbl_font = ('arial', 11, 'bold')

    padrao = ttk.Frame(tab_control)
    tab_control.add(padrao, text='Padrão')

    #LINHA 0
    linhas.append(criarLinhaDeTexto(padrao, 'Digite a primeira coordenada:', lbl_font, row = 0, columnspan=3))
    #LINHA 1
    linhas.append(criarLinhaDeCoordenadas(padrao, row = 1))
    #LINHA 3
    linhas.append(criarLinhaDeTexto(padrao, 'Digite a segunda coordenada:', lbl_font, row = 2, columnspan=3))
    #LINHA 4
    linhas.append(criarLinhaDeCoordenadas(padrao, row = 3))
    #LINHA 5
    escolha_lbl = ttk.Label(padrao, text = "Escolha uma operação:")
    escolha_lbl.grid(row = 4, stick='W')
    escolha_lbl.config(font=lbl_font)

    modo = tk.StringVar()
    modos = ('Formar vetor por dois pontos', 'Soma', 'Subtração')
    modos_cb = ttk.Combobox(padrao, width = 15 , textvariable = modo, values=modos)
    modos_cb.grid(column = 1, row = 4, columnspan = 2, sticky='WE')

    #LINHA 6
    btn_calcular = ttk.Button(padrao, text='Calcular', command=calcular)
    btn_calcular.grid(columnspan = 3, row = 5, sticky='EW')
    #LINHA 7
    btn_mostrar = ttk.Button(padrao, text='Mostrar Cálculo Passo a Passo')
    btn_mostrar.grid(columnspan = 3, row = 6, sticky='EW')
    #LINHA 8
    lbl_resultado = ttk.Label(padrao, text='O resultado é ESSE HEHEHE')
    lbl_resultado.grid(columnspan = 3, row = 7, sticky='EW')
    #ptohtml()
    #open_new_tab(f'{os.getcwd()}\calculo.html')
    
  
def calcular():
    a = obterVetor(linhas[1])
    b = obterVetor(linhas[3])

    print(a,b)
    if(modo.get() == modos[0]):
        lbl_resultado.configure(text= f'O resultado é: {obterVetorDePontos(a, b)}.')
    elif(modo.get() == modos[1]):
        lbl_resultado.configure(text= f'O resultado é: {calcularSoma(a, b)}.')
    elif(modo.get() == modos[2]):
        lbl_resultado.configure(text= f'O resultado é: {calcularSubtração(a, b)}.')


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
