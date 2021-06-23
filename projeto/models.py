import sqlite3
banco = sqlite3.connect('planilha.db')
cursor = banco.cursor()
cursor.execute('''
               CREATE TABLE IF NOT EXISTS PLANILHA(
               ID INTEGER PRIMARY KEY,
               ACAO CHAR(6)NOT NULL,
               VLCOMPRA MONEY NOT NULL,
               QT INT NOT NULL,
               VLATUAL MONEY NOT NULL,
               VOLUME INT NOT NULL,
               GANHO FLOAT,
               PQ VARCHAR(200)
               );
               ''')
class Banco():
    def __init__(self,ACAO,VLCOMPRA,QT,VLATUAL,VOLUME,GANHO,PQ):
        self.banco = sqlite3.connect('planilha.db')
        self.cursor = self.banco.cursor()
        self.acao=ACAO
        self.vlcompra=VLCOMPRA
        self.qt=QT
        self.vlatual=VLATUAL
        self.vol=VOLUME
        self.gn=GANHO
        self.pq=PQ

    def insert(self):
        self.cursor.execute(f'''
        INSERT INTO PLANILHA (ACAO,VLCOMPRA,QT,VLATUAL,VOLUME,GANHO,PQ) VALUES('{str(self.acao)}',{self.vlcompra},{self.qt},{self.vlatual},{self.vol},{self.gn},'{str(self.pq)}')
        '''), self.banco.commit()
        return print('inserido')

    def show(self):
        dados=self.cursor.execute(f'''
        select * from PLANILHA
        ''')
        for i in dados.fetchall():
            return i

