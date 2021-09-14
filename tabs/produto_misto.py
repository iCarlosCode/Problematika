from calculator.gerar_calc import gerar_calculo_produto_misto
from tkinter import *
from tkinter import ttk

from tabs import *
from calculator.operations import calcularProdutoMisto

def criarTab(tab_control):
    global linhas, lbl_resultado

    linhas = list()
    lbl_font = ('arial', 11, 'bold')

    produto_misto = ttk.Frame(tab_control)
    produto_misto.grid_columnconfigure(0, weight=1)
    produto_misto.grid_rowconfigure(0, weight=1)

    
    tab_control.add(produto_misto, text='Produto Misto')

    
    cv = Canvas(produto_misto, highlightthickness=0)
    vsb = Scrollbar(produto_misto, orient=VERTICAL, command=cv.yview)
    frame = Frame(cv)
    #frame.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
    
    cv.configure(yscrollcommand=vsb.set)
    
    cv.grid(row=0, column=0, sticky=NSEW)#.pack(side=LEFT, fill=BOTH, expand=True)
    vsb.grid(row=0, column=1, sticky=NSEW)#.pack(side=RIGHT, fill=Y)

    cv.update()
    cv.create_window((0,0), window=frame, anchor=NW, width=cv.winfo_width())

    cv.bind_all('<MouseWheel>', lambda event, canvas=cv: on_mousewheel(canvas, event))
    cv.bind('<Configure>', lambda event, canvas=cv, frame=frame: onCanvasConfigure(canvas, frame))
    frame.bind('<Configure>', lambda event, canvas=cv: onFrameConfigure(canvas))

    #LINHA 0
    linhas.append(criarLinhaDeResultado(frame))
    #LINHA 1
    linhas.append(criarLinhaDeTexto(frame, 'Digite as coordenadas do primeiro vetor:', lbl_font, row = 1, columnspan=3))
    #LINHA 2
    linhas.append(criarLinhaDeCoordenadas(frame, row = 2))
    #LINHA 3
    linhas.append(criarLinhaDeTexto(frame, 'Digite as coordenadas do segundo vetor:', lbl_font, row = 3, columnspan=3))
    #LINHA 4
    linhas.append(criarLinhaDeCoordenadas(frame, row = 4))
    #LINHA 5
    linhas.append(criarLinhaDeTexto(frame, 'Digite as coordenadas do terceiro vetor:', lbl_font, row = 5, columnspan=3))
    #LINHA 5
    linhas.append(criarLinhaDeCoordenadas(frame, row = 6))
    #LINHA 6
    linhas.append(criarBotãoCalcular(frame, 7, lambda: calcular(tab_control)))
    

def calcular(widget):
    v = obterVetor(linhas[2])
    u = obterVetor(linhas[4])
    w = obterVetor(linhas[6])
    linhas[0]['resultado'].set(f'{calcularProdutoMisto(v, u, w)}')
    gerar_calculo_produto_misto(v, u, w)

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
