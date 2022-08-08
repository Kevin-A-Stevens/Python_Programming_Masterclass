"""
Grid Geometry Manager
He called it the Place Geometry Manager
"""
try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry('640x480-8-200')  # heightxwidth+from_left+from_top

# First, add a label
label = tkinter.Label(mainWindow, text="Hello World")
# Add with grid and specify where
label.grid(row=0, column=0)

# Second, add a canvas
leftFrame = tkinter.Frame(mainWindow)
canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
# Add with grid and specify where
# Note the fill=tkinter.Y does not require the expand option
# Also fill=tkinter.BOTH, expand=True will expand both
# Need to add expand=True in certain circumstances
leftFrame.grid(row=1, column=1)
# canvas.pack(side='top', fill=tkinter.X, expand=True)
canvas.grid(row=1, column=0)

rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1,column=2, sticky='n')
# Create buttons
button1 = tkinter.Button(rightFrame, text='button1')
button2 = tkinter.Button(rightFrame, text='button2')
button3 = tkinter.Button(rightFrame, text='button3')
# Add buttons
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

# configure the columns
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)

leftFrame.config(relief='sunken', borderwidth=1)
rightFrame.config(relief='sunken', borderwidth=1)
leftFrame.grid(sticky='ns')
rightFrame.grid(sticky='new')

rightFrame.columnconfigure(0, weight=1)
button2.grid(sticky='ew')

mainWindow.mainloop()