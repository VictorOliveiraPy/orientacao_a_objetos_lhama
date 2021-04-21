class MysqlDB:

    def __init__(self) -> None:
        self.__conexao = 'Mysql'

    def conectar(self):
        print('Conecntando ao banco Mysql...')
    
    def desconectar(self) -> str:
        print('Desconectando ao banco Mysql...')
