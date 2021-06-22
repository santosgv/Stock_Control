import sqlite3


class BancoDados():
    def __init__(self):
        self.conn=sqlite3.connect('planilhadb')
        self.cursor=self.conn.cursor()
        self.cursor.execute("""
             CREATE TABLE IF NOT EXISTS Acoes (
                 COD INTEGER PRIMARY KEY,
                 ACAO CHAR(40) NOT NULL,
                 ValorCompra INTEGER(10),
                 Quantidade int,
                 ValorAtual money,
                 Volume money,
                 Ganho int,
                 PQ char(200),              
             );
         """)
        self.conn.commit()

    def insert(self,acao,valorcompra,quantidade,valoratual,volume,ganho,porque):
        self.conn.execute(f'''
            insert into Acoes (ACAO,ValorCompra,Quantidade,ValorAtual,Volume,Ganho,PQ) values('{acao}',{valorcompra},{quantidade},{valoratual},{volume},{ganho},'{porque}')
        ''')
        self.conn.commit()
        self.conn.close()
        return print('Inserido com sucesso')

    def update(self):
        pass

    def delete(self):
        pass
