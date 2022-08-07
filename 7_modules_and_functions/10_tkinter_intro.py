"""
Tkinter introduction

Everything is a window in Tkinter
Tkinter has a heirarchy with mainWindow the root
"""
try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# tkinter._test()

mainWindow = tkinter.Tk()
mainWindow.title("Hello World")
mainWindow.geometry('640x480+8+400')  # heightxwidth+from_left+from_top
mainWindow.mainloop()



