from tkinter import *
from tkinter import ttk

def criarTab(tab_control):
    sobre = ttk.Frame(tab_control)
    tab_control.add(sobre, text='Sobre')
    label = Label(sobre, text='Problematika - a Calculadora Vetorial que te ensina!'\
    '\nGostou da Calculadora?\n Você pode mostrar sua gratidão por compartilhá-la com o maior número de pessoas possível!'
    '\nVocê também pode me ajudar enviando qualquer quantia no PIX abaixo.')
    label.pack()


    ttk.Button(sobre, text='Verificar se há atualizações.')

if __name__ == '__main__':
    win = Tk()
    win.minsize(600,600)

    tab_control = ttk.Notebook(win)
    tab_control.pack(expan=1,fill='both')

    criarTab(tab_control)

    win.mainloop()
