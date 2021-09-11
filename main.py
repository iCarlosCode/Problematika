import tkinter as tk
from tkinter import *
from tkinter import ttk
from tabs import (
    padrao,
    produto_escalar,
    produto_misto,
    produto_vetorial,
    BrowserFrame,
    criarLinhaDeBotões,
    sobre,
    pos_relativa,
    completar_quadrado
)
from cefpython3 import cefpython as cef
from shutil import rmtree


def main():
    global browser_frame

    win = Tk()
    cef.Initialize()
    last_entry = ttk.Entry()

    win.title("Calculadora Problematika")
    win.minsize(750, 620)
    win.wm_geometry("750x620")
    win.wm_iconbitmap("i.ico")
    win.grid_columnconfigure(0, weight=2, uniform="uniform")
    win.grid_columnconfigure(1, weight=1, uniform="uniform")
    win.grid_rowconfigure(0, weight=5, uniform="uniform")
    win.grid_rowconfigure(1, weight=4, uniform="uniform")
    # Solve focus problems
    win.bind("<Button-1>", lambda event: event.widget.focus_force())
    
    win.bind_class("TEntry", "<FocusIn>", le)
    # Create Tab Control
    tab_control = ttk.Notebook(win)
    tab_control.grid(sticky="NSEW")

    # Create Tabs
    completar_quadrado.criarTab(tab_control)
    padrao.criarTab(tab_control)
    produto_escalar.criarTab(tab_control)
    produto_vetorial.criarTab(tab_control)
    produto_misto.criarTab(tab_control)
    pos_relativa.criarTab(tab_control)
    sobre.criarTab(tab_control)

    # Create Frame
    frame = ttk.LabelFrame(win, text="Calculo Passo a Passo")
    frame.grid(row=0, column=1, rowspan=2, sticky=("NSWE"))
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(0, weight=1)

    # Create Browser Frame
    lblurl = tk.StringVar(value="file:///calculo1.html")
    browser_frame = BrowserFrame(frame, entry_url_var=lblurl)
    browser_frame.pack(fill=tk.BOTH, expand=tk.YES)

    # Create Keyboard
    teclado_fr = ttk.Frame(win)
    teclado_fr.grid(row=1, column=0, sticky=("NSWE"))
    teclado = criarTeclado(teclado_fr)

    win.mainloop()
    cef.Shutdown()
    rmtree("webrtc_event_logs", ignore_errors=True)
    rmtree("blob_storage", ignore_errors=True)


def load(e):
    global browser_frame
    browser_frame.browser.Reload()


def insert_number(self):
    global last_entry
    if last_entry.get() == "0":
        last_entry.delete(0, tk.END)
        last_entry.insert(0, self)
    elif last_entry.get() == "-0":
        last_entry.delete(0, tk.END)
        last_entry.insert(0, int(self) * -1)
    else:
        last_entry.insert(last_entry.index("insert"), self)


def delete_number():
    global last_entry
    text = last_entry.get()

    if (int(text) > 0 and len(text) == 1) or (int(text) < 0 and len(text) == 2):
        last_entry.delete(0, tk.END)
        last_entry.insert(0, "0")
    elif text in '-0':
        last_entry.delete(0, tk.END)
        last_entry.insert(0, "0")
    else:
        last_entry.delete(last_entry.index("insert") - 1, last_entry.index("insert"))


def make_positive():
    global last_entry
    n = int(last_entry.get())
    if n < 0:
        last_entry.delete(0, tk.END)
        last_entry.insert(0, f"{n*-1}")


def make_negative():
    global last_entry
    n = int(last_entry.get())
    if n >= 0:
        last_entry.delete(0, tk.END)
        last_entry.insert(0, f"{n*-1}" if n != 0 else "-0")


def criarTeclado(frame):
    S = ttk.Style()
    S.configure("my.TButton", font=("arial", 20, "bold"))
    frame.grid_columnconfigure((0, 1, 2), weight=1)
    frame.grid_rowconfigure((0, 1, 2, 3), weight=1)

    teclado = list()

    teclado.append(criarLinhaDeBotões(frame, 0, (7, 8, 9, "←")))
    teclado.append(criarLinhaDeBotões(frame, 1, (4, 5, 6, "+")))
    teclado.append(criarLinhaDeBotões(frame, 2, (1, 2, 3, "-")))
    teclado.append([ttk.Button(frame, text=f"0", style="my.TButton")])
    teclado[3][0].grid(row=3, column=0, columnspan=4, sticky=("NSWE"))

    teclado[0][0].configure(command=lambda: insert_number(teclado[0][0].cget("text")))
    teclado[0][1].configure(command=lambda: insert_number(teclado[0][1].cget("text")))
    teclado[0][2].configure(command=lambda: insert_number(teclado[0][2].cget("text")))
    teclado[0][3].configure(command=delete_number)

    teclado[1][0].configure(command=lambda: insert_number(teclado[1][0].cget("text")))
    teclado[1][1].configure(command=lambda: insert_number(teclado[1][1].cget("text")))
    teclado[1][2].configure(command=lambda: insert_number(teclado[1][2].cget("text")))
    teclado[1][3].configure(command=make_positive)

    teclado[2][0].configure(command=lambda: insert_number(teclado[2][0].cget("text")))
    teclado[2][1].configure(command=lambda: insert_number(teclado[2][1].cget("text")))
    teclado[2][2].configure(command=lambda: insert_number(teclado[2][2].cget("text")))
    teclado[2][3].configure(command=make_negative)

    teclado[3][0].configure(command=lambda: insert_number(teclado[3][0].cget("text")))

    return teclado


def le(e):
    global last_entry
    last_entry = e.widget


if __name__ == "__main__":
    main()
