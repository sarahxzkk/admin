class Relatorio:
    def calcular_salario_diario(self):
        salario_diario = self.valor_hora * 8
        return salario_diario

    def calcular_salario_semanal(self):
        horas_trabalhadas_semana = 5 * 8 
        salario_semanal = self.valor_hora * horas_trabalhadas_semana
        return salario_semanal

    def calcular_salario_mensal(self):
        horas_trabalhadas_mes = 22 * 8  
        salario_mensal = self.valor_hora * horas_trabalhadas_mes
        return salario_mensal

    def calcular_salario_anual(self):
        horas_trabalhadas_ano = 260 * 8  
        salario_anual = self.valor_hora * horas_trabalhadas_ano
        return salario_anual

    def __str__(self):
        return f"Valor Hora: {self.valor_hora}, Hora Entrada: {self.hora_entrada}, Hora Saída: {self.hora_saida}, Data Início: {self.data_inicio}, Data Fim: {self.data_fim}, Descrição: {self.descricao}"
