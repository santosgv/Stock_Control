from .models import  BancoDados
from .principal import *


class FuncionalidadeS(BancoDados):
    def adiciona(self,Aplicacao):
        banco=BancoDados()
        banco.insert(self.entacao.get(),self.entvr.get(),self.entq.get(),'100,0',2,100,self.entpc.get())
        print('adicionado com sucesso')

    def altera(self):
        self.update()

    def excluir(self):
        self.delete()

