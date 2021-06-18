import tkinter as tk
from tkinter import *
from tkinter import ttk
from tabs import padrao, produto_escalar, produto_misto, produto_vetorial, BrowserFrame
from cefpython3 import cefpython as cef


win = Tk()
cef.Initialize()

win.minsize(600,600)
win.grid_columnconfigure((0,1), weight=1)
win.grid_rowconfigure(0, weight=1)

#Create Tab Control
tab_control = ttk.Notebook(win)
tab_control.grid(sticky='NSEW')



padrao.criarTab(tab_control)
produto_escalar.criarTab(tab_control)
produto_vetorial.criarTab(tab_control)
produto_misto.criarTab(tab_control)

#Create Frame
frame = ttk.Frame(win)
frame.grid(row=0, column=1, sticky=('NSWE'))
frame.grid_columnconfigure((0,1), weight=1)
frame.grid_rowconfigure(0, weight=1)


# Create Browser Frame
lblurl = tk.StringVar(value='file:///calculo.html')
browser_frame = BrowserFrame(frame)
browser_frame.pack(fill=tk.BOTH, expand=tk.YES)


win.mainloop()
cef.Shutdown()

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
