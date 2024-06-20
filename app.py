
from modelos.usuario import User
from modelos.empresa import Empresa
from modelos.relatorio import Relatorio
from modelos.trabalho import  Trabalho
user_sarah = User('Sarah'.ljust(10), 'sara@sara'.ljust(10), 359999999)
 
user_sarah.adicionar_trabalho('FrontEnd', 10, 15, '19/06/2024', '19/06/2024', 'FrontEnd do nosso sistema')
 
empresa1 = Empresa('Senac'.ljust(7), 'estudante'.ljust(9), 'rodovia'.ljust(7), 2345667788)
empresa2 = Empresa('Senai'.ljust(7), 'estudante'.ljust(9), 'rodovia'.ljust(7), 2345667789)
 
 
 
def  main():
    print(user_sarah)
    print(empresa1)
    print(empresa2)
 
# if __name__ == '__main__':
#     main()
 
 
# from modelos.trabalho import User, Empresa, Trabalho
 
class Relatorio:
    def __init__(self):
        self.usuarios = User.dados
        self.empresas = Empresa.empresas
        self.trabalhos = Trabalho.trabalhos
 
    def listar_usuarios(self):
        print("=== Lista de Usuários ===")
        for usuario in self.usuarios:
            print(usuario)
 
    def listar_empresas(self):
        print("=== Lista de Empresas ===")
        for empresa in self.empresas:
            print(empresa)
 
    def listar_trabalhos(self):
        print("=== Lista de Trabalhos ===")
        for trabalho in self.trabalhos:
            print(trabalho)
 
    def relatorio_completo(self):
        self.listar_usuarios()
        print()
        self.listar_empresas()
        print()
        self.listar_trabalhos()
 
if __name__ == "__main__":
    relatorio = Relatorio()
    relatorio.relatorio_completo()
