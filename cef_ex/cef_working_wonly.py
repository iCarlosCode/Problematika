from cefpython3 import cefpython as cef
import ctypes
import tkinter as tk
from tkinter import *
from tkinter import ttk


# Fix for PyCharm hints warnings
WindowUtils = cef.WindowUtils()


    
def main():
    def go_back():
        browser_frame.browser.GoBack()

    def go_forward():
        browser_frame.browser.GoForward()

    def reload():
        browser_frame.browser.Reload()

    def load(x):
        browser_frame.browser.StopLoad()
        browser_frame.browser.LoadUrl(lbl1.get())


    def on_button1(self):
        """For focus problems see Issue #255 and Issue #535. """
        win.focus_force()

    win = Tk()
    cef.Initialize()

    win.minsize(600,600)
    win.grid_columnconfigure((0,1), weight=1)
    win.grid_rowconfigure((1,2,3), weight=1)

    #Create Frame
    frame = ttk.Frame(win)
    frame.grid(row=1, column=0, sticky=('NSWE'))

    ff = ttk.Frame(win)
    ff.grid(row=2, column=0, sticky=('WE'))
    lblurl = tk.StringVar(value='https://www.google.com.br')
    lbl1 = ttk.Entry(ff, textvariable=lblurl)
    lbl1.grid(row=2, column=0, sticky=('WE'))
    

    # setar foco
    lbl1.bind("<Button-1>", lambda event: event.widget.focus_force())
    lbl1.bind("<Return>", load)
    

    # Create Browser Frame
    browser_frame = BrowserFrame(frame, entry_url_var=lblurl)
    browser_frame.pack(fill=tk.BOTH, expand=tk.YES)


    #Create a Button
    bt = ttk.Button(win, text="Hi", command=go_back).grid(row=1, column=1, sticky=('NSWE'))
    bt1 = ttk.Button(win, text="Hi", command=go_forward).grid(row=2, column=1, sticky=('NSWE'))
    bt2 = ttk.Button(win, text="Hi", command=load).grid(row=3, column=1, sticky=('NSWE'))

    #Create a Label
    lbl = ttk.Label(win, text="Its working Perfectly Thanks").grid(row=0, column=0, sticky=('WE'))


    lbl2 = ttk.Entry(win)
    lbl2.grid(row=3, column=0, sticky=('WE'))
    win.mainloop()
    cef.Shutdown()

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
                                             url=self.entry_url_var if self.entry_url_var else "https://www.google.com.br")#"file:///C:/Users/pcarl/Dropbox/iCarlosCode/Problematika/calculo.html")
        assert self.browser
        self.browser.SetClientHandler(LoadHandler(self))
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



# FAZ O LINK APARECER
class LoadHandler(object):

    def __init__(self, browser_frame):
        self.browser_frame = browser_frame

    def OnLoadStart(self, browser, **_):
        if self.browser_frame.entry_url_var:
            self.browser_frame.entry_url_var.set(browser.GetUrl())


if __name__ == '__main__':
    main()