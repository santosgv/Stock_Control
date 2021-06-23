from tkinter import *
from tkinter import ttk
from .fucoes import FuncionalidadeS


main = Tk()


class Aplicacao(FuncionalidadeS):
    def __init__(self):
        self.main = main
        self.principal()
        self.frame()
        self.grid()
        self.botoes()
        main.mainloop()

    def principal(self):
        self.main.title('Planilha de Açoes')
        self.main.geometry('1024x500')
        self.main.resizable(False, False)

    def frame(self):
        self.Main = Frame(self.main, bg='white', highlightbackground='black')
        self.Main.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.18)
        self.second = Frame(self.main, bg='red', highlightbackground='black')
        self.second.place(relx=0.01, rely=0.20, relwidth=0.98, relheight=0.75)

    def grid(self):
        self.grid = ttk.Treeview(self.second, columns=('Acao', 'VC', 'Quantidade', 'VA', 'Volume', 'GANHO', 'PC'),show='headings', height=25)
        self.grid.place(relx=0.01, rely=0.01, relwidth=0.99, relheight=0.75)
        self.grid.column('#0', width=10, minwidth=10)
        self.grid.column('Acao', minwidth=100, width=102)
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



    # self.grid.insert(parent='', index=0, iid=0, text='', values=('1','Vineet','Alpha','a','s','c','g'))

    def botoes(self):
        Label(self.Main, text='Acao', bg='white').place(relx=0.08, rely=0.01)
        Label(self.Main, text='Valor', bg='white').place(relx=0.23, rely=0.01)
        Label(self.Main, text='Quantidade', bg='white').place(relx=0.33, rely=0.01)
        Label(self.Main, text='Por que Comprou', bg='white').place(relx=0.43, rely=0.01)

        self.entacao = Entry(self.Main)
        self.entacao.place(relx=0.03, rely=0.30)

        self.entvr = Entry(self.Main)
        self.entvr.place(relx=0.20, rely=0.30, relwidth=0.10)
        self.entq = Entry(self.Main)
        self.entq.place(relx=0.33, rely=0.30, relwidth=0.05)

        self.entpc = Entry(self.Main)
        self.entpc.place(relx=0.43, rely=0.30, relwidth=0.30)
        Button(self.Main, text='Adicionar', command=self.adiciona).place(relx=0.80, rely=0.30)

    def getentry(self):
        self.entacao.get()
        self.entvr.get()
        self.entq.get()
        self.entpc.get()
        print(self.entacao.get(),self.entvr.get(),self.entq.get(),self.entpc.get())

