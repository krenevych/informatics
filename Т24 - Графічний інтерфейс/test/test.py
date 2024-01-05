from tkinter import *
#import filedialog

def Quit():
    global root
    root.destroy()
    
def LoadFile(): 
    fn = filedialog.Open(root, filetypes = [('*.txt files', '.txt')]).show()
    if fn == '':
        return
    textbox.delete('1.0', 'end') 
    textbox.insert('1.0', open(fn, 'rt').read())
    
def SaveFile():
    fn = filedialog.SaveAs(root, filetypes = [('*.txt files', '.txt')]).show()
    if fn == '':
        return
    if not fn.endswith(".txt"):
        fn+=".txt"
    open(fn, 'wt').write(textbox.get('1.0', 'end'))

root = Tk()

panelFrame = Frame(root, height = 60, bg = 'gray')
textFrame = Frame(root, height = 340, width = 600)

panelFrame.pack(side = 'top', fill = 'x')
textFrame.pack(side = 'bottom', fill = 'both', expand = 1)

textbox = Text(textFrame, font='Arial 14', wrap='word')
scrollbar = Scrollbar(textFrame)

scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set

textbox.pack(side = 'left', fill = 'both', expand = 1)
scrollbar.pack(side = 'right', fill = 'y')

loadBtn = Button(panelFrame, text = 'Load', command = LoadFile)
saveBtn = Button(panelFrame, text = 'Save', command = SaveFile)
quitBtn = Button(panelFrame, text = 'Quit', command = Quit)

loadBtn.place(x = 10, y = 10, width = 40, height = 40)
saveBtn.place(x = 60, y = 10, width = 40, height = 40)
quitBtn.place(x = 110, y = 10, width = 40, height = 40)

root.mainloop()
