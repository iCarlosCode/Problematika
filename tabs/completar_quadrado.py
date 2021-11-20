from tkinter import *
from tkinter import ttk
from . import *
from calculator.operations import obter_coeficiente, completar_quadrado
from calculator.gerar_calc import gerar_completar_quadrado


def criarTab(tab_control):
    global linhas, lbl_resultado

    linhas = list()
    lbl_font = ('arial', 11, 'bold')

    completar_quadrado = ttk.Frame(tab_control)
    completar_quadrado.grid(sticky="NSEW")
    completar_quadrado.columnconfigure(0, weight=1)
    completar_quadrado.rowconfigure(1, weight=1)
    
    tab_control.add(completar_quadrado, text='Completar Quadrado')
    c = tk.StringVar()
    #LINHA 0
    linhas.append(criarLinhaDeResultado(completar_quadrado, columnspan=4))
    #LINHA 0
    linhas.append(CustomText(completar_quadrado))#, textvariable = c))
    linhas[1].grid(sticky='EW', columnspan=4)
    linhas[1].config(font=('arial', 20, 'bold'))
    linhas[1].bind('<<TextModified>>', checar_expoente)
    #LINHA 2
    linhas.append(criarBotãoCalcular(completar_quadrado, 2, lambda: calcular(tab_control)))
    ttk.Button(completar_quadrado, text='■^2', command=adicionar_expoente).grid(row=2, column=3, sticky='NSEW')


def calcular(widget):
    equation = linhas[1].get("1.0",END)
    li = equation_to_list(equation)

    result = completar_eq(equation, li)
    linhas[0]['resultado'].set(result)

    if '=0' in equation or '= 0' in equation: #re.match(r"=\s*([-+]\s*)*0*", equation):
        gerar_completar_quadrado(equation, result, (li[0],li[1]), y=(li[2], li[3]), z=(li[4], li[5]), F=li[6])
    elif li[6]:
        gerar_completar_quadrado(equation, result, (li[0],li[1]), y=(li[2], li[3]), z=(li[4], li[5]), F=li[6]*-1)
    else:
        gerar_completar_quadrado(equation, result, (li[0],li[1]), y=(li[2], li[3]), z=(li[4], li[5]), F=li[6])

    # Reload the browser after generating the calc
    Tk._root(widget).winfo_children()[2].winfo_children()[0].browser.Reload()
    equation_to_list

def checar_expoente(e):
    text =  e.widget.get("1.0",END)
    text = text.replace('^2', '²')
    e.widget.replace("1.0", END, text)
    e.widget.mark_set("insert", e.widget.index('1.0 lineend'))
    

def adicionar_expoente():
    linhas[1].insert(linhas[1].index("insert"), '²')

def equation_to_list(equation = 'x²+y²-6x+10y+18=0'):
    array = split_equation(equation)
    incognitas = ['x', 'y', 'z']
    li = list()
    for i in incognitas:
        li.append(obter_coeficiente(f'{i}²', array))
        li.append(obter_coeficiente(i, array))
        
    li.append(obter_coeficiente('=', array))
    return li

def completar_eq(equation = 'x²+y²-6x+10y+18=0', li=[]):
    # TODO tabs split equation resolver a questão dos números antes e depois do igual, # TODO resolver obter coeficiente em completar_eq
    # GAMBIARRA
    if '=0' in equation or '= 0' in equation: #re.match(r"=\s*([-+]\s*)*0*", equation):
        return completar_quadrado((li[0],li[1]), y=(li[2], li[3]), z=(li[4], li[5]), F=li[6])
    elif li[6]:
        return completar_quadrado((li[0],li[1]), y=(li[2], li[3]), z=(li[4], li[5]), F=li[6]*-1)
    else:
        return completar_quadrado((li[0],li[1]), y=(li[2], li[3]), z=(li[4], li[5]))



if __name__ == '__main__':
    win = Tk()
    win.minsize(600,600)

    tab_control = ttk.Notebook(win)
    tab_control.pack(expan=1,fill='both')

    criarTab(tab_control)

    win.mainloop()
