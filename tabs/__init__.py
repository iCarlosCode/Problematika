import tkinter as tk
from tkinter import *
from tkinter import ttk
from cefpython3 import cefpython as cef
import ctypes


def criarLinhaDeResultado(master, row = 0):
    r = dict()
    r['resultado'] = tk.StringVar()

    r['label'] = ttk.LabelFrame(master, text = 'Resultado:')
    r['label'].grid(columnspan = 3, column = 0, row = row, sticky='EW')
    r['label'].grid_columnconfigure(0, weight=1)

    r['entry'] = ttk.Entry(r['label'], width = 15, textvariable = r['resultado'])
    r['entry'].grid(sticky='EW')
    r['entry'].config(font=('arial', 20, 'bold'))
    r['entry'].config(state='readonly', background = r['entry'].cget('background'))
    
    return (r)



def criarLinhaDeCoordenadas(master, row = 0):
    linha = dict()
    eixos = ('x','y','z')

    # Enable horizontal scaling in this column
    master.grid_columnconfigure((0,1,2), weight=1)
    for i in range(0, 3):
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

def criarLinhaDeTexto(master, text='', font=(), row = 0, columnspan=1):
    lbl = ttk.Label(master, text=text)
    lbl.grid(row=row, columnspan=columnspan, sticky='W')
    lbl.config(font=font)
    return lbl


def obterVetor(linha):
    return (linha['x']['coordenada'].get(), linha['y']['coordenada'].get(), linha['z']['coordenada'].get())
    
class BrowserFrame(tk.Frame):

    def __init__(self, mainframe, entry_url_var = None):
        self.entry_url_var = entry_url_var
        self.browser = None
        tk.Frame.__init__(self, mainframe)
        self.mainframe = mainframe
        self.bind("<Configure>", self.on_configure)
        """For focus problems see Issue #255 and Issue #535. """
        self.focus_set()

        

    def embed_browser(self):
        window_info = cef.WindowInfo()
        rect = [0, 0, self.winfo_width(), self.winfo_height()]
        window_info.SetAsChild(self.get_window_handle(), rect)
        self.browser = cef.CreateBrowserSync(window_info,
                                             url=self.entry_url_var.get() if self.entry_url_var else "https://www.google.com.br")#"file:///C:/Users/pcarl/Dropbox/iCarlosCode/Problematika/calculo.html")
        self.message_loop_work()

    def get_window_handle(self):
        if self.winfo_id() > 0:
            return self.winfo_id()
        else:
            raise Exception("Couldn't obtain window handle")

    def message_loop_work(self):
        cef.MessageLoopWork()
        self.after(10, self.message_loop_work)

    # Ativa o resize
    def on_configure(self, _):
        if self.browser:
            self.on_mainframe_configure(_.width, _.height)
        else:
            self.embed_browser()


    def on_mainframe_configure(self, width, height):
        if self.browser:
            ctypes.windll.user32.SetWindowPos(
                self.browser.GetWindowHandle(), 0,
                0, 0, width, height, 0x0002)
            self.browser.NotifyMoveOrResizeStarted()