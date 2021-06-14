from tkinter import *
from tkinter import ttk

def criarTab(tab_control):
    tab1 = ttk.Frame(tab_control)
    
    tab_control.add(tab1, text='tab1')
    label = Label(tab1, text='Name').grid(column=0,row=0)
    #label.pack()

if __name__ == '__main__':
    win = Tk()
    win.minsize(600,600)

    tab_control = ttk.Notebook(win)
    tab_control.pack(expan=1,fill='both')

    criarTab(tab_control)

    win.mainloop()
