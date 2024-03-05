'''
Created on Jan 14, 2018

@author: aditya

This program shows the use of notebook in tkinter
Notebook is used to create Tabs in the application.
This enables browsing different pages in the application.

Frame widget from tkinter is used in this Application to demostrate the use of Notebook/tabs.
Please note that other widgets can also be used as per the requirement.
'''

import tkinter as tk
from tkinter import ttk

class NoteBookApp:
    def __init__(ego, master):
        ego.master = master
        ego.notebk = ttk.Notebook(ego.master)
        ego.notebk.pack()
        ego.frame1 = ttk.Frame(ego.notebk, width = 400, height = 400, relief = tk.SUNKEN)
        ego.frame2 = ttk.Frame(ego.notebk, width = 400, height = 400, relief = tk.SUNKEN)
        ego.notebk.add(ego.frame1, text = 'One')
        ego.notebk.add(ego.frame2, text = 'Two')
        
        ego.btn = ttk.Button(ego.frame1, text='Add/Insert Tab at Position 1', command = ego.AddTab)
        ego.btn.pack()
        
        ego.btn2 = ttk.Button(ego.frame1, text='Disable Tab at Position 1', command = ego.disableTab)
        ego.btn2.pack()

        strdisplay = r'Tab ID:{}'.format(ego.notebk.select())
        ttk.Label(ego.frame1, text = strdisplay).pack()
        
        strdisplay2 = 'Tab index:{}'.format(ego.notebk.index(ego.notebk.select()))
        ttk.Label(ego.frame1, text = strdisplay2).pack()
        
    def AddTab(ego):
        if ego.btn['text'] == 'Add/Insert Tab at Position 1':
            ego.frame3 = ttk.Frame(ego.notebk, width = 400, height = 400, relief = tk.SUNKEN)
            ego.notebk.insert(1, ego.frame3, text = 'Additional Tab')
            ego.btn.config(text = 'Remove/Forget Tab')
        else:
            ego.notebk.forget(1)
            ego.btn.config(text = 'Add/Insert Tab at Position 1')
    
    def disableTab(ego):
        # properties of tab - accessible by using notbook.tab(tab_id, option)
        # to see available properties - print(notbook.tab(tab_id))
        if ego.btn2['text'] == 'Disable Tab at Position 1':
            ego.notebk.tab(1, state = 'disabled')
            ego.btn2.config(text = 'Hide Tab at Position 1')
        elif ego.btn2['text'] == 'Hide Tab at Position 1':
            ego.notebk.tab(1, state = 'hidden')
            ego.btn2.config(text = 'Normalize Tab at Position 1')
        elif ego.btn2['text']== 'Normalize Tab at Position 1':
            ego.notebk.tab(1, state = 'normal')
            ego.btn2.config(text = 'Disable Tab at Position 1')
        

def launchNoteBookApp():
    root = tk.Tk()
    NoteBookApp(root)
    tk.mainloop()
    

if __name__=='__main__':
    launchNoteBookApp()
    
        
