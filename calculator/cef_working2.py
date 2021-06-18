from cefpython3 import cefpython as cef
import ctypes
import tkinter as tk
from tkinter import *
from tkinter import ttk
import platform


# Fix for PyCharm hints warnings
WindowUtils = cef.WindowUtils()

# Platforms
WINDOWS = (platform.system() == "Windows")
LINUX = (platform.system() == "Linux")
MAC = (platform.system() == "Darwin")


    
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

    # Focus problems solved
    win.bind("<Button-1>", lambda event: event.widget.focus_force())

    #Create Frame
    frame = ttk.Frame(win)
    frame.grid(row=1, column=0, sticky=('NSWE'))

    ff = ttk.Frame(win)
    ff.grid(row=2, column=0, sticky=('WE'))
    lblurl = tk.StringVar(value="file:///calculo.html")
    lbl1 = ttk.Entry(ff, textvariable=lblurl)
    lbl1.grid(row=2, column=0, sticky=('WE'))
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
        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)
        self.bind("<Configure>", self.on_configure)
        """For focus problems see Issue #255 and Issue #535. """
        self.focus_set()

        

    def embed_browser(self):
        window_info = cef.WindowInfo()
        rect = [0, 0, self.winfo_width(), self.winfo_height()]
        window_info.SetAsChild(self.get_window_handle(), rect)
        self.browser = cef.CreateBrowserSync(window_info,
                                             url=self.entry_url_var.get() if self.entry_url_var else "https://www.google.com.br")#"file:///C:/Users/pcarl/Dropbox/iCarlosCode/Problematika/calculo.html")
        assert self.browser
        self.browser.SetClientHandler(LoadHandler(self))
        #self.browser.SetClientHandler(FocusHandler(self))
        self.message_loop_work()

    def get_window_handle(self):
        if MAC:
            # Do not use self.winfo_id() on Mac, because of these issues:
            # 1. Window id sometimes has an invalid negative value (Issue #308).
            # 2. Even with valid window id it crashes during the call to NSView.setAutoresizingMask:
            #    https://github.com/cztomczak/cefpython/issues/309#issuecomment-661094466
            #
            # To fix it using PyObjC package to obtain window handle. If you change structure of windows then you
            # need to do modifications here as well.
            #
            # There is still one issue with this solution. Sometimes there is more than one window, for example when application
            # didn't close cleanly last time Python displays an NSAlert window asking whether to Reopen that window. In such
            # case app will crash and you will see in console:
            # > Fatal Python error: PyEval_RestoreThread: NULL tstate
            # > zsh: abort      python tkinter_.py
            # Error messages related to this: https://github.com/cztomczak/cefpython/issues/441
            #
            # There is yet another issue that might be related as well:
            # https://github.com/cztomczak/cefpython/issues/583
            
            # noinspection PyUnresolvedReferences
            from AppKit import NSApp
            # noinspection PyUnresolvedReferences
            import objc
            # noinspection PyUnresolvedReferences
            content_view = objc.pyobjc_id(NSApp.windows()[-1].contentView())
            return content_view
        elif self.winfo_id() > 0:
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

    def on_root_configure(self):
        # Root <Configure> event will be called when top window is moved
        if self.browser:
            self.browser.NotifyMoveOrResizeStarted()

    def on_mainframe_configure(self, width, height):
        if self.browser:
            if WINDOWS:
                ctypes.windll.user32.SetWindowPos(
                    self.browser.GetWindowHandle(), 0,
                    0, 0, width, height, 0x0002)
            elif LINUX:
                self.browser.SetBounds(0, 0, width, height)
            self.browser.NotifyMoveOrResizeStarted()

    def on_focus_in(self, _):
        if self.browser:
            self.browser.SetFocus(True)

    def on_focus_out(self, _):
        """For focus problems see Issue #255 and Issue #535. """
        if LINUX and self.browser:
            self.browser.SetFocus(False)


# FAZ O LINK APARECER
class LoadHandler(object):

    def __init__(self, browser_frame):
        self.browser_frame = browser_frame

    def OnLoadStart(self, browser, **_):
        if self.browser_frame.entry_url_var:
            self.browser_frame.entry_url_var.set(browser.GetUrl())

# FAZ O FOCO FUNCIONAR NO LINUX
class FocusHandler(object):
    """For focus problems see Issue #255 and Issue #535. """

    def __init__(self, browser_frame):
        self.browser_frame = browser_frame

    def OnSetFocus(self, source, **_):
        if LINUX:
            return False
        else:
            return True

    def OnGotFocus(self, **_):
        if LINUX:
            self.browser_frame.focus_set()


if __name__ == '__main__':
    main()