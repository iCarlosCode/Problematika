from tkinter import *
from tkinter import ttk

from widgets_utils import criarLinhaDeCoordenadas


def criarTab(tab_control):
    tab1 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='Produto misto')
    label = Label(tab1, text='Produto misto')
    label.pack()

    criarLinhaDeCoordenadas(tab1)

    lf = ttk.LabelFrame(tab_control, text="Coordenada X").grid(column=0, row=0)

if __name__ == '__main__':
    win = Tk()
    win.minsize(600,600)

    tab_control = ttk.Notebook(win)
    tab_control.pack(expan=1,fill='both')

    criarTab(tab_control)

    win.mainloop()
