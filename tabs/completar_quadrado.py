from tkinter import *
from tkinter import ttk
from . import *
from calculator.operations import obter_coeficiente, completar_quadrado

def criarTab(tab_control):
    global linhas, lbl_resultado

    linhas = list()
    lbl_font = ('arial', 11, 'bold')

    completar_quadrado = ttk.Frame(tab_control)
    completar_quadrado.grid(sticky="NSEW")
    completar_quadrado.columnconfigure(0, weight=1)
    #completar_quadrado.rowconfigure((0, 1, 2), weight=1, uniform=True)
    completar_quadrado.rowconfigure(1, weight=1)
    
    tab_control.add(completar_quadrado, text='Completar Quadrado')
    c = tk.StringVar()
    #LINHA 0
    linhas.append(criarLinhaDeResultado(completar_quadrado))
    #LINHA 0
    linhas.append(tk.Text(completar_quadrado))#, textvariable = c))
    linhas[1].grid(sticky='EW')
    linhas[1].config(font=('arial', 20, 'bold'))
    #LINHA 2
    linhas.append(criarBotãoCalcular(completar_quadrado, 2, lambda: calcular(tab_control)))

def calcular(widget):
    
    #v = obterVetor(linhas[2])
    #u = obterVetor(linhas[4])
    linhas[0]['resultado'].set(completar_eq(linhas[1].get("1.0",END)))
    #gerar_calculo_produto_vetorial(v, u)

    # Reload the browser after generating the calc
    Tk._root(widget).winfo_children()[2].winfo_children()[0].browser.Reload()

def completar_eq(equation = 'x²+y²-6x+10y+18=0'):
    array = split_equation(equation)
    incognitas = ['x', 'y', 'z']
    li = list()
    for i in incognitas:
        li.append(obter_coeficiente(f'{i}²', array))
        li.append(obter_coeficiente(i, array))
        
    li.append(obter_coeficiente('=', array))
    print(li)
    #print(f'a:{a}, b:{b}, c:{c}, d:{d}, f:{f}')
    #print(completar_quadrado((a,b), y=(c, d), F=f))

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
