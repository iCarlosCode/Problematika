from tabs import criarLinhaDeResultado
import tkinter as tk
from tkinter import *
from tkinter import ttk

def criarLinhaDeBotões(master, row, items):
    r = list()
    
    for i,n in enumerate(items):
        r.append(ttk.Button(master, text=f'{n}'))
        r[i].grid(row = row, column=i, sticky=('NSWE'))
    return r

def criarTeclado(frame):
    frame.grid_columnconfigure((0,1,2), weight=1)
    frame.grid_rowconfigure((0,1,2,3), weight=1)
    
    teclado = list()

    teclado.append(criarLinhaDeBotões(frame, 0, (7, 8, 9, 'C')))
    teclado.append(criarLinhaDeBotões(frame, 1, (4, 5, 6, '+')))
    teclado.append(criarLinhaDeBotões(frame, 2, (1, 2, 3, '-')))
    teclado.append([ttk.Button(frame, text=f'0')])
    teclado[3][0].grid(row = 3, column=0, columnspan=4, sticky=('NSWE'))

    teclado[0][0].configure(command=lambda:commando(teclado[0][0].cget('text')))
    teclado[0][1].configure(command=lambda:commando(teclado[0][1].cget('text')))
    teclado[0][2].configure(command=lambda:commando(teclado[0][2].cget('text')))
    teclado[0][3].configure(command=lambda:commando(teclado[0][3].cget('text')))

    teclado[1][0].configure(command=lambda:commando(teclado[1][0].cget('text')))
    teclado[1][1].configure(command=lambda:commando(teclado[1][1].cget('text')))
    teclado[1][2].configure(command=lambda:commando(teclado[1][2].cget('text')))
    teclado[1][3].configure(command=lambda:commando(teclado[1][3].cget('text')))

    teclado[2][0].configure(command=lambda:commando(teclado[2][0].cget('text')))
    teclado[2][1].configure(command=lambda:commando(teclado[2][1].cget('text')))
    teclado[2][2].configure(command=lambda:commando(teclado[2][2].cget('text')))
    teclado[2][3].configure(command=lambda:commando(teclado[2][3].cget('text')))

    teclado[3][0].configure(command=lambda:commando(teclado[3][0].cget('text')))

    return teclado

def commando(self):
    print(self)

win = Tk()

win.minsize(600,600)
win.grid_columnconfigure(0, weight=2, uniform='uniform')
win.grid_columnconfigure(1, weight=1, uniform='uniform')
win.grid_rowconfigure(0, weight=1)


#Create Frame
frame = ttk.Frame(win)
frame.grid(row=0, column=0, sticky=('NSWE'))

criarTeclado(frame)

'''
for i in range(10, 0):
    row = list()
    if i >6:
        row.append(ttk.Button(frame, text=f'{i}'))
        row[0].grid(row = 2, column=i%3)
    elif i >3:
        row.append(ttk.Button(frame, text=f'{i}'))
        row[0].grid(row = 1, column=i%3)
    elif i >0:
        row.append(ttk.Button(frame, text=f'{i}'))
        row[0].grid(row = 0, column=i%3)
    else:
        row.append(ttk.Button(frame, text=f'{i}'))
        row[0].grid(row = 4, column=0)
    teclado.append(row)
'''



win.mainloop()