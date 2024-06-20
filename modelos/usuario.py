from modelos.trabalho import Trabalho
class User:

    dados = []

    def __init__ (self, nome, email, telefone):
        self._nome = nome
        self._email = email
        self._telefone = telefone
        self._trabalhos = []
        User.dados.append(self)

    def __str__(self):
        return f'Nome: {self._nome} | Email: {self._email} | Tel: {self._telefone}'

    def adicionar_trabalho(self,valor, hora_entrada, hora_saida, data_inicio, data_fim, descricao):
        trabalho = Trabalho(valor, hora_entrada, hora_saida, data_inicio, data_fim, descricao)
        self._trabalhos.append(trabalho)
 
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    def __repr__(self):
        return f'User(nome={self._nome}, email={self._email}, telefone={self._telefone})'
