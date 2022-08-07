"""
Tkinter Pack Geometry
"""
try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry('640x480+8+400')  # heightxwidth+from_left+from_top

# First, add a label
label = tkinter.Label(mainWindow, text="Hello World")
# Add with pack and specify where
label.pack(side='top')

# Second, add a canvas
leftFrame = tkinter.Frame(mainWindow)
canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
# Add with pack and specify where
# Note the fill=tkinter.Y does not require the expand option
# Also fill=tkinter.BOTH, expand=True will expand both
# Need to add expand=True in certain circumstances
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)
# canvas.pack(side='top', fill=tkinter.X, expand=True)
canvas.pack(side='left', anchor='n')

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', anchor='n', expand=True)
# Create buttons
button1 = tkinter.Button(rightFrame, text='button1')
button2 = tkinter.Button(rightFrame, text='button2')
button3 = tkinter.Button(rightFrame, text='button3')
# Add buttons
button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')


mainWindow.mainloop()

