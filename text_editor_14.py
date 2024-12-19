from tkinter import *

root = Tk()
root.title("Rise-Coding (2010) ++")
root.geometry('600x700')
root.iconbitmap('C:/Users/dmitr/Desktop/PyFilesCDS/instruments/notepad.ico')


f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

text_fild = Text(f_text,
                 bg = 'black',
                 fg='lime',
                 padx=10,
                 pady=10,
                 wrap=WORD,
                 insertbackground='brown',
                 selectbackground='#8D917A',
                 spacing3=10,
                 width=30
                 )
text_fild.pack(expand=1, fill=BOTH, side=LEFT)

scroll = Scrollbar(f_text, command=text_fild.yview)
scroll.pack(side=LEFT, fill=Y)
text_fild.config(yscrollcommand=scroll.set)

root.mainloop()