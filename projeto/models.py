import sqlite3


class BancoDados():
    def __init__(self):
        self.conn = sqlite3.connect("planilha")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS Acoes(
        cod integer primary key,
        ACAO char(10) not null,
        ValorCompra money,
        Quantidade int,
        ValorAtual money,
        Volume int,
        Ganho char(10),
        PQ char(200)
        );          
         ''')

    def insert(self, acao, valorcompra, quantidade, valoratual, volume, ganho, porque):
        self.conn.execute(f'''
            insert into Acoes values('{acao}',{valorcompra},{quantidade},{valoratual},{volume},{ganho},{porque})
        '''),self.conn.commit()
        return print('Inserido com sucesso')

    def update(self):
        pass

    def delete(self):
        pass
a=BancoDados()
a.insert('123',10,11,15,100,'100%','comprei')