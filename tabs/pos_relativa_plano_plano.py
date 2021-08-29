#from calculator.gerar_calc import gerar_calculo_pos_relativa_duas_retas
#from calculator.operations import calcularPosRelativaDuasRetas
# [ ] Criar o teste para posição relativa entre dois planos
# [ ] Criar a função para calcular a posição entre dois planos
# [ ] Criar a função para gerar o Cálculo da Posição relativa entre dois planos
from tkinter import *
from tkinter import ttk
from tabs import *


def criarTab(tab_control):
    global linhas, lbl_resultado

    linhas = list()

    pos_relativa_plano_plano = ttk.Frame(tab_control)
    pos_relativa_plano_plano.grid_columnconfigure(0, weight=1)
    pos_relativa_plano_plano.grid_rowconfigure((0,1,2,3,4), weight=1)

    tab_control.add(pos_relativa_plano_plano, text='Dois planos')
    
    #LINHA 0
    linhas.append(criarLinhaDeResultado(pos_relativa_plano_plano, columnspan = 6))
    
    # PLANO α
    #LINHA 1
    linhas.append(criarLinhaDeTexto(pos_relativa_plano_plano, 'Digite as coordenadas do VETOR NORMAL ao plano α:', LBL_FONT1, row = 1, columnspan=6))
    #LINHA 2
    linhas.append(criarLinhaDeCoordenadasPlano(pos_relativa_plano_plano, row = 2))

    # PLANO π
    #LINHA 3
    linhas.append(criarLinhaDeTexto(pos_relativa_plano_plano, 'Digite as coordenadas do VETOR NORMAL ao plano π:', LBL_FONT1, row = 3, columnspan=6))    
    #LINHA 4
    linhas.append(criarLinhaDeCoordenadasPlano(pos_relativa_plano_plano, row = 4))

    # LINHA 5
    linhas.append(criarBotãoCalcular(pos_relativa_plano_plano, 5, lambda: calcular(tab_control), columnspan=6))


def calcular(widget):
    pR = obterVetor(linhas[2])
    vR = obterVetor(linhas[4])
    pS = obterVetor(linhas[7])
    uS = obterVetor(linhas[9])
    #linhas[0]['resultado'].set(f'{calcularPosRelativaDuasRetas(pR, vR, pS, uS)}')
    #gerar_calculo_pos_relativa_duas_retas(pR, vR, pS, uS)

    # Reload the browser after generating the calc
    Tk._root(widget).winfo_children()[2].winfo_children()[0].browser.Reload()


if __name__ == '__main__':
    win = Tk()
    win.minsize(600,600)

    tab_control = ttk.Notebook(win)
    tab_control.pack(expan=1,fill='both')

    criarTab(tab_control)

    win.mainloop()
