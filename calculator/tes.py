import matplotlib
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use('TkAgg')

from tkinter import *
from tkinter import ttk

def graph(text):
    tmptext = entry.get()
    tmptext = "$"+tmptext+"$"

    ax.clear()
    ax.text(0.2, 0.6, tmptext, fontsize = 50)  
    canvas.draw()


root = Tk()

mainframe = Frame(root)
mainframe.pack()

text = StringVar()
entry = Entry(mainframe, width=70, textvariable=text)
entry.pack()

label = Label(mainframe)
label.pack()

fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=label)
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

root.bind('<Return>', graph)
root.mainloop()