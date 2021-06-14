from tkinter import *
from tkinter import ttk
from tabs import tab1, produto_misto


win = Tk()
win.minsize(600,600)
win.grid_columnconfigure(0, weight=1)
win.grid_rowconfigure(0, weight=1)

#Create Tab Control
tab_control = ttk.Notebook(win)
tab_control.grid(sticky='NSEW')




tab1.criarTab(tab_control)
produto_misto.criarTab(tab_control)


win.mainloop()

"""
tab1 = ttk.Frame(tab_control)
tab1.grid(column=0, row=0)
tab_control.add(tab1, text='tab1')
aba = ttk.Frame(tab_control)
aba.grid_columnconfigure(0, weight=1)
aba.grid_rowconfigure(0, weight=0)
lbl = ttk.Button(aba, text='teste')
lbl.grid(column=0, row=0, columnspan=2, rowspan=2, sticky='NSEW')

tab_control.add(aba, text='Texto oo aba')
"""
