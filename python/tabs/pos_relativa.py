from tabs import pos_relativa_reta_reta 
from tkinter import *
from tkinter import ttk

def criarTab(tab_control):
    pos_relativa = ttk.Frame(tab_control)
    pos_relativa.grid(sticky="NSEW")
    pos_relativa.grid_columnconfigure(0, weight=1)
    pos_relativa.grid_rowconfigure(0, weight=1)
    tab_control.add(pos_relativa, text='Posição Relativa')
    
    posr_tab_control = ttk.Notebook(pos_relativa)
    posr_tab_control.grid(sticky="NSEW")

    pos_relativa_reta_reta.criarTab(posr_tab_control)
 

if __name__ == '__main__':
    win = Tk()
    win.minsize(600,600)

    tab_control = ttk.Notebook(win)
    tab_control.pack(expan=1,fill='both')

    criarTab(tab_control)

    win.mainloop()
