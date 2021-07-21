from calculator.gerar_calc import gerar_calculo_pos_relativa_duas_retas
from calculator.operations import calcularPosRelativaDuasRetas
from tkinter import *
from tkinter import ttk

from tabs import *
def on_mousewheel(self, event):
    self.yview_scroll(int(-1*event.delta/120), 'units')

def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox('all'))

def onCanvasConfigure(canvas, frame):
    canvas.update()
    canvas.create_window((0,0), window=frame, anchor=NW, width=canvas.winfo_width())

def criarTab(tab_control):
    global linhas, lbl_resultado

    linhas = list()

    pos_relativa_reta_reta = ttk.Frame(tab_control)
    pos_relativa_reta_reta.grid_columnconfigure(0, weight=1)
    pos_relativa_reta_reta.grid_rowconfigure(0, weight=1)

    tab_control.add(pos_relativa_reta_reta, text='Duas Retas')

    cv = Canvas(pos_relativa_reta_reta)
    vsb = Scrollbar(pos_relativa_reta_reta, orient=VERTICAL, command=cv.yview)
    frame = Frame(cv)
    
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
    
    # RETA R

    #LINHA 1
    linhas.append(criarLinhaDeTexto(frame, 'Digite as coordenadas de um PONTO da reta R:', LBL_FONT1, row = 1, columnspan=3))
    #LINHA 2
    linhas.append(criarLinhaDeCoordenadas(frame, row = 2))
    #LINHA 3
    linhas.append(criarLinhaDeTexto(frame, 'Digite as coordenadas do VETOR diretor da reta R:', LBL_FONT1, row = 3, columnspan=3))
    #LINHA 4
    linhas.append(criarLinhaDeCoordenadas(frame, row = 4))

    # RETA S
    linhas.append(tk.Label(frame).grid(row=5))
    #LINHA 5
    linhas.append(criarLinhaDeTexto(frame, 'Digite as coordenadas de um PONTO da reta S:', LBL_FONT1, row = 6, columnspan=3))
    #LINHA 6
    linhas.append(criarLinhaDeCoordenadas(frame, row = 7))
    #LINHA 7
    linhas.append(criarLinhaDeTexto(frame, 'Digite as coordenadas do VETOR diretor da reta S:', LBL_FONT1, row = 8, columnspan=3))
    #LINHA 8
    linhas.append(criarLinhaDeCoordenadas(frame, row = 9))

    #LINHA 5
    linhas.append(criarBotãoCalcular(frame, 95, lambda: calcular(tab_control)))


def calcular(widget):
    pR = obterVetor(linhas[2])
    vR = obterVetor(linhas[4])
    pS = obterVetor(linhas[7])
    uS = obterVetor(linhas[9])
    linhas[0]['resultado'].set(f'{calcularPosRelativaDuasRetas(pR, vR, pS, uS)}')
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
