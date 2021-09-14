from calculator.gerar_calc import (
    gerar_calculo_formar_vetores,
    gerar_calculo_paralelismo,
    gerar_calculo_perpendincularismo,
    gerar_calculo_soma,
    gerar_calculo_subtração,
)
from tkinter import *
from tkinter import ttk

from . import *
from calculator.operations import calcularSoma, calcularSubtração, checarParalelismo, checarPerpedincularismo, obterVetorDePontos


def criarTab(tab_control):
    global linhas, lbl_resultado, modo, modos
    # maybe dar pra fazer reload
    print(Tk._root(tab_control).winfo_children())
    linhas = list()
    lbl_font = ("arial", 11, "bold")

    padrao = ttk.Frame(tab_control)
    padrao.grid(sticky="NSEW")
    padrao.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
    tab_control.add(padrao, text="Padrão")

    # LINHA 0
    linhas.append(criarLinhaDeResultado(padrao))
    # LINHA 1
    linhas.append(
        criarLinhaDeTexto(
            padrao, "Digite a primeira coordenada:", lbl_font, row=1, columnspan=3
        )
    )
    # LINHA 2
    linhas.append(criarLinhaDeCoordenadas(padrao, row=2))
    # LINHA 3
    linhas.append(
        criarLinhaDeTexto(
            padrao, "Digite a segunda coordenada:", lbl_font, row=3, columnspan=3
        )
    )
    # LINHA 4
    linhas.append(criarLinhaDeCoordenadas(padrao, row=4))
    # LINHA 5
    escolha_lbl = ttk.Label(padrao, text="Escolha uma operação:")
    escolha_lbl.grid(row=5, stick="W")
    escolha_lbl.config(font=lbl_font)

    modos = ("Formar vetor por dois pontos", "Soma", "Subtração", 'Checar se são perpedinculares', 'Checar se são paralelos')
    modo = tk.StringVar(value=modos[0])
    modos_cb = ttk.Combobox(padrao, width=15, textvariable=modo, values=modos)
    modos_cb.grid(column=1, row=5, columnspan=2, sticky="WE")

    # LINHA 6
    linhas.append(criarBotãoCalcular(padrao, 6, lambda: calcular(tab_control)))

    # ptohtml()
    # open_new_tab(f'{os.getcwd()}\calculo.html')


def calcular(widget):
    a = obterVetor(linhas[2])
    b = obterVetor(linhas[4])

    print(a, b)
    if modo.get() == modos[0]:
        linhas[0]["resultado"].set(f"{obterVetorDePontos(a, b)}")
        gerar_calculo_formar_vetores(a, b)

    elif modo.get() == modos[1]:
        linhas[0]["resultado"].set(f"{calcularSoma(a, b)}")
        gerar_calculo_soma(a, b)
    elif modo.get() == modos[2]:
        linhas[0]["resultado"].set(f"{calcularSubtração(a, b)}")
        gerar_calculo_subtração(a, b)
    elif modo.get() == modos[3]:
        linhas[0]["resultado"].set('Perpedinculares' if checarPerpedincularismo(a, b) else 'Não perpedinculares')
        gerar_calculo_perpendincularismo(a, b)
    elif modo.get() == modos[4]:
        linhas[0]["resultado"].set('Paralelos' if checarParalelismo(a, b) else 'Não paralelos')
        gerar_calculo_paralelismo(a, b)
    
    Tk._root(widget).winfo_children()[2].winfo_children()[0].browser.Reload()


if __name__ == "__main__":
    win = Tk()
    win.minsize(600, 600)
    win.grid_columnconfigure(0, weight=1)
    win.grid_rowconfigure(0, weight=1)

    # Create Tab Control
    tab_control = ttk.Notebook(win)
    tab_control.grid(sticky="NSEW")

    criarTab(tab_control)

    win.mainloop()
