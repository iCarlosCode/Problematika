import tkinter as tk
from tkinter import *
from tkinter import ttk

def criarLinhaDeCoordenadas(master, row = 0):
    linha = dict()
    eixos = ('x','y','z')

    for i in range(0, 3):
        c = dict()
        c['coordenada'] = tk.IntVar()
        c['label'] = ttk.Label(master,text = f'{eixos[i].upper()}:')
        c['label'].pack()#.grid(column = i * 2, row = row, sticky='E')
        c['entry'] = ttk.Entry(master,width = 15, textvariable = c['coordenada'])
        c['entry'].pack()#grid(column = ((i * 2) + 1), row = row)
        linha[eixos[i]] = c
    return (linha)

