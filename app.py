
from modelos.usuario import User
from modelos.empresa import Empresa
from modelos.relatorio import Relatorio

user_sarah = User('Sarah', 'sara@sara', 359999999)

user_sarah.adicionar_trabalho('FrontEnd', 10, 15, '19/06/2024', '19/06/2024', 'FrontEnd do nosso sistema')

empresa1 = Empresa('Senac', 'estudante', 'rodovia', 2345667788)
empresa2 = Empresa('Senai', 'estudante', 'rodovia', 2345667789)





def  main():
    print(user_sarah)
    print(empresa1)
    print(empresa2)

if __name__ == '__main__':
    main()
