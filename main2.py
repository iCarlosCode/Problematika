from tabs import criarLinhaDeResultado
import tkinter as tk
from tkinter import *
from tkinter import ttk

def criarLinhaDeBotões(master, row,start,end):
    r = list()
    
    for i,n in enumerate(tuple(range(start, end+1))):
        r.append(ttk.Button(master, text=f'{n}'))
        r[i].grid(row = row, column=i, sticky=('NSWE'))
    teclado.append(r)

win = Tk()

win.minsize(600,600)
win.grid_columnconfigure(0, weight=2, uniform='uniform')
win.grid_columnconfigure(1, weight=1, uniform='uniform')
win.grid_rowconfigure(0, weight=1)


#Create Frame
frame = ttk.Frame(win)
frame.grid(row=0, column=0, sticky=('NSWE'))
frame.grid_columnconfigure((0,1,2), weight=1)
frame.grid_rowconfigure((0,1,2), weight=1)
teclado = list()

teclado.append(criarLinhaDeBotões(frame, 0, 7, 9))
teclado.append(criarLinhaDeBotões(frame, 1, 4, 6))
teclado.append(criarLinhaDeBotões(frame, 2, 1, 3))

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