from tkinter import *
from tkinter import ttk

def criarTab(tab_control):


    sobre = ttk.Frame(tab_control)
    sobre.columnconfigure((0,1), uniform='uniform', weight=1)
    tab_control.add(sobre, text='Sobre')
    SIZE = 200
    lbl_img = Label(sobre)
    lbl_img.image=PhotoImage(file='pk.png', height=SIZE, width=SIZE)
    lbl_img.configure(image=lbl_img.image)
    lbl_img.grid(column=0, row=0)

    lbl_pix = Label(sobre)
    lbl_pix.image=PhotoImage(file='pix.png', height=SIZE, width=SIZE)
    lbl_pix.configure(image=lbl_pix.image)
    lbl_pix.grid(column=1, row=0)

    label = Label(sobre, text="""Gostou da Calculadora? Você pode ajudar:
1) Compartilhando a calculadora com o maior número de pessoas possível.
2) Você também pode me ajudar enviando qualquer quantia no PIX (QR CODE ACIMA).
3) Meu email para contato e PIX: carlospos@aluno.ufrb.edu.br
4) Você contribuir para o desenvolvimento da calculadora no GitHub.
5) Pode também fazer sugestões e reportar bugs.""")
    label.grid(column=0, row=1, columnspan=2)


if __name__ == '__main__':
    win = Tk()
    win.minsize(600,600)

    tab_control = ttk.Notebook(win)
    tab_control.pack(expan=1,fill='both')

    criarTab(tab_control)

    win.mainloop()
