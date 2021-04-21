class PostgresDB:

    def __init__(self) -> None:
        self.__conexao = 'Postgres'

    def conectar(self):
        print('Conecntando ao banco Postgres...')
    
    def desconectar(self) -> str:
        print('Desconectando ao banco Postgres...')
