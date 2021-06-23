from .models import  BancoDados
from .principal import *


class FuncionalidadeS(BancoDados):
    def __init__(self):
        Aplicacao()
    def adiciona(self):
        banco=BancoDados()
        banco.insert(self.entacao.get(),self.entvr.get(),self.entq.get(),'100,0',2,100,self.entpc.get())

    def altera(self):
        self.update()

    def excluir(self):
        self.delete()

