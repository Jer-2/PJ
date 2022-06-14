import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import fir_support

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = 'gray40' # X11 color: #666666
        _ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
        _ana2color = 'beige' # X11 color: #f5f5dc
        _tabfg1 = 'black' 
        _tabfg2 = 'black' 
        _tabbg1 = 'grey75' 
        _tabbg2 = 'grey89' 
        _bgmode = 'light' 

        top.geometry("600x396+120+797")
        top.minsize(152, 1)
        top.maxsize(2564, 1390)
        top.resizable(1,  1)
        top.title("5566人力銀行")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.383, rely=0.399, height=31, width=60)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''應徵者''')

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.417, rely=0.222, height=22, width=43)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''5566''')

        self.Button2 = tk.Button(self.top)
        self.Button2.place(relx=0.6, rely=0.399, height=31, width=60)
        self.Button2.configure(activebackground="beige")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(compound='left')
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''廠商''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

class Toplevel2:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = 'gray40' # X11 color: #666666
        _ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
        _ana2color = 'beige' # X11 color: #f5f5dc
        _tabfg1 = 'black' 
        _tabfg2 = 'black' 
        _tabbg1 = 'grey75' 
        _tabbg2 = 'grey89' 
        _bgmode = 'light' 

        top.geometry("600x450+1056+1")
        top.minsize(152, 1)
        top.maxsize(2564, 1415)
        top.resizable(1,  1)
        top.title("應徵者注冊")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.133, rely=0.156, height=25, width=43)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Label''')

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.133, rely=0.244, height=25, width=43)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Label''')

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.133, rely=0.333, height=25, width=43)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Label''')

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.133, rely=0.467, height=25, width=43)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Label''')

        self.Label1_1 = tk.Label(self.top)
        self.Label1_1.place(relx=0.133, rely=0.4, height=25, width=43)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(anchor='w')
        self.Label1_1.configure(background="#d9d9d9")
        self.Label1_1.configure(compound='left')
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''Label''')

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.317, rely=0.733, height=31, width=60)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''確定''')

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.683, rely=0.778, height=31, width=60)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''上一頁''')

class Toplevel3:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = 'gray40' # X11 color: #666666
        _ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
        _ana2color = 'beige' # X11 color: #f5f5dc
        _tabfg1 = 'black' 
        _tabfg2 = 'black' 
        _tabbg1 = 'grey75' 
        _tabbg2 = 'grey89' 
        _bgmode = 'light' 

        top.geometry("600x353+1047+507")
        top.minsize(152, 1)
        top.maxsize(2564, 1415)
        top.resizable(1,  1)
        top.title("工作簡歷")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.433, rely=0.779, height=31, width=60)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''確定''')

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.65, rely=0.822, height=31, width=60)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''上一頁''')

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.183, rely=0.113, height=25, width=43)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Label''')

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.183, rely=0.227, height=25, width=43)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Label''')

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.2, rely=0.34, height=25, width=43)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Label''')

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.217, rely=0.425, height=25, width=43)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Label''')

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.183, rely=0.51, height=25, width=43)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Label''')

class Toplevel4:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = 'gray40' # X11 color: #666666
        _ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
        _ana2color = 'beige' # X11 color: #f5f5dc
        _tabfg1 = 'black' 
        _tabfg2 = 'black' 
        _tabbg1 = 'grey75' 
        _tabbg2 = 'grey89' 
        _bgmode = 'light' 

        top.geometry("600x449+1045+902")
        top.minsize(152, 1)
        top.maxsize(2564, 1415)
        top.resizable(1,  1)
        top.title("厰商注冊")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.367, rely=0.824, height=31, width=60)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''確定''')

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.6, rely=0.869, height=31, width=60)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''上一頁''')

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.117, rely=0.111, height=25, width=43)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Label''')

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.15, rely=0.267, height=25, width=43)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Label''')

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.183, rely=0.356, height=25, width=43)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Label''')

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.2, rely=0.468, height=25, width=43)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Label''')

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.167, rely=0.601, height=25, width=43)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Label''')

class Toplevel5:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = 'gray40' # X11 color: #666666
        _ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
        _ana2color = 'beige' # X11 color: #f5f5dc
        _tabfg1 = 'black' 
        _tabfg2 = 'black' 
        _tabbg1 = 'grey75' 
        _tabbg2 = 'grey89' 
        _bgmode = 'light' 

        top.geometry("600x450+1694+51")
        top.minsize(152, 1)
        top.maxsize(2564, 1415)
        top.resizable(1,  1)
        top.title("工作要求")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.183, rely=0.822, height=31, width=60)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''確定''')

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.55, rely=0.667, height=31, width=60)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''上一頁''')

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.217, rely=0.111, height=25, width=43)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Label''')

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.233, rely=0.222, height=25, width=43)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Label''')

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.25, rely=0.311, height=25, width=43)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Label''')

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.233, rely=0.378, height=25, width=43)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Label''')

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.217, rely=0.467, height=25, width=43)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Label''')

class Toplevel7:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = 'gray40' # X11 color: #666666
        _ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
        _ana2color = 'beige' # X11 color: #f5f5dc
        _tabfg1 = 'black' 
        _tabfg2 = 'black' 
        _tabbg1 = 'grey75' 
        _tabbg2 = 'grey89' 
        _bgmode = 'light' 

        top.geometry("600x350+122+383")
        top.minsize(152, 1)
        top.maxsize(2564, 1415)
        top.resizable(1,  1)
        top.title("應徵者")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.283, rely=0.4, height=31, width=60)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''注冊''')

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.55, rely=0.443, height=31, width=60)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''填寫簡歷''')

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.383, rely=0.171, height=25, width=43)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Label''')

class Toplevel8:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = 'gray40' # X11 color: #666666
        _ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
        _ana2color = 'beige' # X11 color: #f5f5dc
        _tabfg1 = 'black' 
        _tabfg2 = 'black' 
        _tabbg1 = 'grey75' 
        _tabbg2 = 'grey89' 
        _bgmode = 'light' 

        top.geometry("600x306+110+11")
        top.minsize(152, 1)
        top.maxsize(2564, 1415)
        top.resizable(1,  1)
        top.title("厰商")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.317, rely=0.51, height=31, width=60)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''注冊''')

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.583, rely=0.49, height=31, width=60)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''工作面試''')

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.483, rely=0.261, height=25, width=43)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Label''')

def start_up():
    fir_support.main()

if __name__ == '__main__':
    fir_support.main()




