import tkinter as tk
from tkinter import *
from tkinter import ttk
from cefpython3 import cefpython as cef
import ctypes

def main():
    global win
    win = Tk()
    cef.Initialize()

    win.wm_geometry('600x600')
    win.grid_columnconfigure((0,1), weight=1)
    win.grid_rowconfigure(0, weight=1)

    #Create Frame
    frame = Frame(win, bg='black')
    frame.grid(row=0, column=0, sticky=('NSWE'))
    frame.grid_columnconfigure((0,1), weight=1)
    frame.grid_rowconfigure(0, weight=1)

    # Create Browser Frame
    browser_frame = BrowserFrame(frame)
    browser_frame.grid(row=0, column=0, sticky=('NSWE'))#.pack(fill=tk.BOTH, expand=tk.YES)

    bt = ttk.Button(frame, text="Hi").grid(row=0, column=1, sticky=('NSWE'))
    win.mainloop()
    cef.Shutdown()

class BrowserFrame(tk.Frame):

    def __init__(self, mainframe, navigation_bar=None):
        self.navigation_bar = navigation_bar
        self.closing = False
        self.browser = None
        tk.Frame.__init__(self, mainframe)
        self.mainframe = mainframe
        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)
        self.bind("<Configure>", self.on_configure)
        """For focus problems see Issue #255 and Issue #535. """
        self.focus_set()

    #URLURLURL
    def embed_browser(self):
        window_info = cef.WindowInfo()
        rect = [0, 0, self.winfo_width(), self.winfo_height()]
        window_info.SetAsChild(self.get_window_handle(), rect)
        self.browser = cef.CreateBrowserSync(window_info,
                                             url="file:///calculo.html")
        assert self.browser
        win.bind("<Configure>", self.on_configure)
        
        self.browser.SetClientHandler(LifespanHandler(self))
        self.browser.SetClientHandler(LoadHandler(self))
        self.browser.SetClientHandler(FocusHandler(self))
        self.message_loop_work()

    def get_window_handle(self):
        if self.winfo_id() > 0:
            return self.winfo_id()
        else:
            raise Exception("Couldn't obtain window handle")

    def message_loop_work(self):
        cef.MessageLoopWork()
        self.after(10, self.message_loop_work)

    def on_configure(self, _):
        if not self.browser:
            self.embed_browser()
        self.browser.NotifyMoveOrResizeStarted()

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
            self.browser.NotifyMoveOrResizeStarted()
            print('changed')

    def on_focus_in(self, _):
        #logger.debug("BrowserFrame.on_focus_in")
        if self.browser:
            self.browser.SetFocus(True)

    def on_focus_out(self, _):
        #logger.debug("BrowserFrame.on_focus_out")
        """For focus problems see Issue #255 and Issue #535. """
        pass

    def on_root_close(self):
        #logger.info("BrowserFrame.on_root_close")
        if self.browser:
            #logger.debug("CloseBrowser")
            self.browser.CloseBrowser(True)
            self.clear_browser_references()
        else:
            #logger.debug("tk.Frame.destroy")
            self.destroy()
            

    def clear_browser_references(self):
        # Clear browser references that you keep anywhere in your
        # code. All references must be cleared for CEF to shutdown cleanly.
        self.browser = None

class LifespanHandler(object):

    def __init__(self, tkFrame):
        self.tkFrame = tkFrame

    def OnBeforeClose(self, browser, **_):
        #logger.debug("LifespanHandler.OnBeforeClose")
        self.tkFrame.quit()

class LoadHandler(object):

    def __init__(self, browser_frame):
        self.browser_frame = browser_frame

    def OnLoadStart(self, browser, **_):
        pass
        #if self.browser_frame.master.navigation_bar:
        #    self.browser_frame.master.navigation_bar.set_url(browser.GetUrl())


class FocusHandler(object):
    """For focus problems see Issue #255 and Issue #535. """

    def __init__(self, browser_frame):
        self.browser_frame = browser_frame

    def OnTakeFocus(self, next_component, **_):
        pass#logger.debug("FocusHandler.OnTakeFocus, next={next}".format(next=next_component))

    def OnSetFocus(self, source, **_):
            return True

    def OnGotFocus(self, **_):
        #logger.debug("FocusHandler.OnGotFocus")
        pass


if __name__ == '__main__':
    main()