from tkinter import *
from tkinter import ttk

main=Tk()

class aplicacao():
    def __init__(self):
        self.main=main
        self.Principal()
        self.Frame()
        self.Grid()
        main.mainloop()

    def Principal(self):
        self.main.title('Planilha de Açoes')
        self.main.geometry('1024x500')
        self.main.resizable(False, False)

    def Frame(self):
        self.Main = Frame(self.main, bg='white', highlightbackground='black')
        self.Main.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.50)
        self.second = Frame(self.main, bg='red', highlightbackground='black')
        self.second.place(relx=0.01, rely=0.48, relwidth=0.98, relheight=0.50)


    def Grid(self):
        self.grid=ttk.Treeview(self.second,columns=('Acao', 'VC', 'Quantidade','VA','Volume','GANHO','PC'), show='headings')
        self.grid.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=1.0)
        self.grid.column('#0', width=0, minwidth=0)
        self.grid.column('Acao', minwidth=100, width=100)
        self.grid.column('VC', minwidth=100, width=100)
        self.grid.column('Quantidade', minwidth=100, width=100)
        self.grid.column('VA', minwidth=100, width=100)
        self.grid.column('Volume', minwidth=100, width=100)
        self.grid.column('GANHO', minwidth=100, width=100)
        self.grid.column('PC', minwidth=100, width=400)
        self.grid.heading('#0', text='')
        self.grid.heading('Acao', text='Acao')
        self.grid.heading('VC', text='Valor Compra')
        self.grid.heading('Quantidade', text='Quantidade')
        self.grid.heading('VA', text='Valor Atual')
        self.grid.heading('Volume', text='Volume')
        self.grid.heading('GANHO', text='GANHO')
        self.grid.heading('PC', text='Por Que Comprou')
        self.grid.pack()


aplicacao()