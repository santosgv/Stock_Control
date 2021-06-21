from tkinter import *
from tkinter import ttk

main=Tk()

class aplicacao():
    def __init__(self):
        self.main=main
        self.Principal()
        self.Frame()
        self.Grid()
        self.Botoes()
        main.mainloop()

    def Principal(self):
        self.main.title('Planilha de Açoes')
        self.main.geometry('1024x500')
        self.main.resizable(False, False)

    def Frame(self):
        self.Main = Frame(self.main, bg='white', highlightbackground='black')
        self.Main.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.18)
        self.second = Frame(self.main, bg='red', highlightbackground='black')
        self.second.place(relx=0.01, rely=0.20, relwidth=0.98, relheight=0.75)


    def Grid(self):
        self.grid=ttk.Treeview(self.second,columns=('Acao', 'VC', 'Quantidade','VA','Volume','GANHO','PC'), show='headings',height=25)
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
       # self.grid.insert(parent='', index=1, iid=1, text='', values=('2', 'Vineet', 'Alpha', 'a', 's', 'c', 'g'))
       # self.grid.insert(parent='', index=2, iid=2, text='', values=('3', 'Vineet', 'Alpha', 'a', 's', 'c', 'g'))
       # self.grid.insert(parent='', index=3, iid=3, text='', values=('4', 'Vineet', 'Alpha', 'a', 's', 'c', 'g'))
       # self.grid.insert(parent='', index=4, iid=4, text='', values=('5', 'Vineet', 'Alpha', 'a', 's', 'c', 'g'))
       # self.grid.insert(parent='', index=5, iid=5, text='', values=('6', 'Vineet', 'Alpha', 'a', 's', 'c', 'g'))
       # self.grid.insert(parent='', index=6, iid=6, text='', values=('7', 'Vineet', 'Alpha', 'a', 's', 'c', 'g'))
       # self.grid.insert(parent='', index=7, iid=7, text='', values=('8', 'Vineet', 'Alpha', 'a', 's', 'c', 'g'))
       # self.grid.insert(parent='', index=8, iid=8, text='', values=('9', 'Vineet', 'Alpha', 'a', 's', 'c', 'g'))
       # self.grid.insert(parent='', index=9, iid=9, text='', values=('10', 'Vineet', 'Alpha', 'a', 's', 'c', 'g'))
       # self.grid.insert(parent='', index=10, iid=10, text='', values=('11', 'Vineet', 'Alpha', 'a', 's', 'c', 'g'))
       # self.grid.insert(parent='', index=11, iid=11, text='', values=('12', 'Vineet', 'Alpha', 'a', 's', 'c', 'g'))
       # self.grid.insert(parent='', index=12, iid=12, text='', values=('13', 'Vineet', 'Alpha', 'a', 's', 'c', 'g'))
    def Botoes(self):
        Label(self.Main,text='Acao',bg='white').place(relx=0.03, rely=0.01)
        Label(self.Main, text='Valor', bg='white').place(relx=0.10, rely=0.01)
        Label(self.Main, text='Quantidade', bg='white').place(relx=0.23, rely=0.01)
        Label(self.Main, text='Por que Comprou', bg='white').place(relx=0.33, rely=0.01)
aplicacao()