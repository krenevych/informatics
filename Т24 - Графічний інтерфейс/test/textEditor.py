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

def Clear():
    
    textbox.delete('1.0', END)


root = Tk()


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Відкрити", command=LoadFile)
filemenu.add_command(label="Зберегти як", command=SaveFile)
filemenu.add_separator()
filemenu.add_command(label="Вихід", command=Quit)
menubar.add_cascade(label="Файл", menu=filemenu)
root.config(menu=menubar)


panelFrame = Frame(root, height = 60, bg = 'gray')
textFrame  = Frame(root, height = 340, width = 600)

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
clearBtn = Button(panelFrame, text = 'ClearText', command = Clear)

loadBtn.place(x = 10, y = 10, width = 40, height = 40)
saveBtn.place(x = 60, y = 10, width = 40, height = 40)
quitBtn.place(x = 110, y = 10, width = 40, height = 40)
clearBtn.place(x = 160, y = 10, width = 70, height = 40)

root.mainloop()
