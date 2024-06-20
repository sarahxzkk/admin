class Empresa:

    empresas = []

    def __init__ (self, empresa, funcao, endereco, telefone):
        self.empresa = empresa
        self.funcao = funcao
        self.endereco = endereco
        self.telefone = telefone
        Empresa.empresas.append(self)

    def __str__(self):
            return f'Empresa: {self.empresa} | Função: {self.funcao} | Endereço: {self.endereco} | Tel: {self.telefone}'
        

    # @classmethod
    # def listar_empresas(cls):
    #     print(f"{'Nome da empresa'.ljust(20)} | {'Sua função'.ljust(20)} | {'Endereço'.ljust(20)} | {'Telefone'}")
    #     for empresa in cls.empresas:
    #         print(f'{empresa.empresa.ljust(20)} | {empresa.funcao.ljust(20)} | {empresa.endereco.ljust(20)} | {empresa.telefone}')  
                

