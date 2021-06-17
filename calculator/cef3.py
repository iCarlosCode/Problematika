import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from cefpython3 import cefpython as cef
import threading
import sys


def test_thread(frame):
    global browser, window_info
    sys.excepthook = cef.ExceptHook
    window_info = cef.WindowInfo()

    rect = [0, 0, frame.winfo_width(), frame.winfo_height()]
    window_info.SetAsChild(frame.winfo_id(), rect)
    cef.Initialize()
    browser = cef.CreateBrowserSync(window_info, url = 'file:///C:/Users/pcarl/Dropbox/iCarlosCode/Problematika/calculo.html')
    win.bind("<Configure>", on_root_configure)
    cef.MessageLoop()


def on_closing():
    print('closing')
    win.destroy()


def on_root_configure(self):
        # Root <Configure> event will be called when top window is moved
        if browser:
            print('hi')
            browser.NotifyMoveOrResizeStarted()

if __name__ == '__main__':
    win = Tk()
    
    win.minsize(600,600)
    win.protocol('WM_DELETE_WINDOW', on_closing)
    
    win.grid_columnconfigure(0, weight=1)
    win.grid_rowconfigure(0, weight=1)

    #Create Frame
    frame = Frame(win, bg='black')
    frame.grid(row=0, column=0, sticky=('NSWE'))

    # Create Browser Frame
    #rect = [1, 1, 1200, 600]
    
    thread = threading.Thread(target=test_thread, args=(frame,))
    thread.start()
    
    win.mainloop()