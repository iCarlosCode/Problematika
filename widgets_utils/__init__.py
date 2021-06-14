import tkinter as tk
from tkinter import *
from tkinter import ttk




def criarLinhaDeCoordenadas(master, row = 0):
    linha = dict()
    eixos = ('x','y','z')

    for i in range(0, 3):
        # Enable horizontal scaling in this column
        master.grid_columnconfigure(i, weight=1)

        c = dict()
        c['coordenada'] = tk.IntVar()

        c['label'] = ttk.LabelFrame(master, text = f'Coordenada {eixos[i].upper()}')
        c['label'].grid(column = i, row = row, sticky='EW')
        c['label'].grid_columnconfigure(0, weight=1)

        c['entry'] = ttk.Entry(c['label'],width = 15, textvariable = c['coordenada'])
        c['entry'].grid(sticky='EW')
        c['entry'].config(font=('arial', 20, 'bold'))
        
        linha[eixos[i]] = c
    
    return (linha)