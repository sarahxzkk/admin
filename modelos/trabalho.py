class Trabalho:

    trabalhos = []

    def __init__(self, valor, hora_entrada, hora_saida, data_inicio, data_fim, descricao):
        self.valor = valor
        self.hora_entrada = hora_entrada
        self.hora_saida = hora_saida
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.descricao = descricao
        Trabalho.trabalhos.append(self)

    def __str__(self):
            return f'{self.valor} | {self.hora_entrada} | {self.hora_saida} | {self.data_inicio} | {self.data_fim} | {self.descricao}'
        
    
    @classmethod
    def listar_trabalhos(cls):
        print(f'{"Valor da hora".ljust(20)} | {"Hora de entrada".ljust(20)} | {"Hora de saída".ljust(20)} | {"Data de início".ljust(20)} | {"Data fim".ljust(20)} | {"Descrição"}')
        for trabalho in cls.trabalhos:
            print(f'{trabalho.valor.ljust(20)} | {trabalho.hora_entrada.ljust(20)} | {trabalho.hora_saida.ljust(20)} | {trabalho.data_inicio.ljust(20)} | {trabalho.data_fim.ljust(20)} | {trabalho.descricao}')  





                
