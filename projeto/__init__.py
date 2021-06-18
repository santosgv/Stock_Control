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
        self.main.geometry('1024x1024')
        self.main.resizable(False, False)

    def Frame(self):
        self.principal = Frame(self.main, bg='white')
        self.principal.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

    def Grid(self):
        self.grid=ttk.Treeview(self.principal,columns=('col1', 'col2', 'col3','col4','col5','col6','col7'), show='headings')
        self.grid.place(relx=0.01, rely=0.01, relwidth=1.0, relheight=1.0)
        self.grid.column('#0', width=0, minwidth=0)
        self.grid.column('col1', minwidth=100, width=100)
        self.grid.column('col2', minwidth=100, width=100)
        self.grid.column('col3', minwidth=100, width=100)
        self.grid.column('col4', minwidth=100, width=100)
        self.grid.column('col5', minwidth=100, width=100)
        self.grid.column('col6', minwidth=100, width=100)
        self.grid.column('col7', minwidth=100, width=410)
        self.grid.heading('#0', text='')
        self.grid.heading('#1', text='Acao')
        self.grid.heading('#2', text='Valor Compra')
        self.grid.heading('#3', text='Quantidade')
        self.grid.heading('#4', text='Valor Atual')
        self.grid.heading('#5', text='Volume')
        self.grid.heading('#6', text='GANHO')
        self.grid.heading('#7', text='Por Que Comprou')
        self.grid.pack()


aplicacao()