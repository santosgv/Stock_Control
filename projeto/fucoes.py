from .models import Banco, cursor
from .principal import *


class FuncionalidadeS(Banco):
    def __init__(self):
        pass
    def adiciona(self):
        volume=(int(self.entvr.get())*int(self.entq.get()))
        Banco(self.entacao.get(),self.entvr.get(),self.entq.get(),100,volume,100,self.entpc.get()).insert()

    def altera(self):
        self.update()

    def excluir(self):
        self.delete()

