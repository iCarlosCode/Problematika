from tabs import produto_escalar, produto_vetorial, produto_misto
from tkinter import *
from tkinter import ttk

def criarTab(tab_control):
    produtos = ttk.Frame(tab_control)
    produtos.grid(sticky="NSEW")
    produtos.grid_columnconfigure(0, weight=1)
    produtos.grid_rowconfigure(0, weight=1)
    tab_control.add(produtos, text='Produtos')
    
    prod_tab_control = ttk.Notebook(produtos)
    prod_tab_control.grid(sticky="NSEW")
    produto_escalar.criarTab(prod_tab_control)
    produto_vetorial.criarTab(prod_tab_control)
    produto_misto.criarTab(prod_tab_control)
    
 

if __name__ == '__main__':
    win = Tk()
    win.minsize(600,600)

    tab_control = ttk.Notebook(win)
    tab_control.pack(expan=1,fill='both')

    criarTab(tab_control)

    win.mainloop()
