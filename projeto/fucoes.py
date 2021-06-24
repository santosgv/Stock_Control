from .models import Banco, cursor
from .principal import *


class FuncionalidadeS(Banco):
    def __init__(self):
        pass
    def adiciona(self):

        Banco(self.entacao.get(),self.entvr.get(),self.entq.get(),100,100,100,self.entpc.get()).insert()

    def altera(self):
        self.update()

    def excluir(self):
        self.delete()

