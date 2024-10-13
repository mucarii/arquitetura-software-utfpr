# Definindo a classe Aluno
class Aluno:
    def __init__(self, nome, login, ra):
        self.nome = nome
        self.login = login
        self.ra = ra


# Definindo a classe Turma
class Turma:
    def __init__(self, codigo, nota):
        self.codigo = codigo
        self.nota = nota

    def aprovado(self):
        return self.nota >= 7  # Supondo que a média para aprovação seja 7


# Definindo a classe TurmaPresencial (herda de Turma)
class TurmaPresencial(Turma):
    def __init__(self, codigo, nota, frequencia):
        super().__init__(codigo, nota)
        self.frequencia = frequencia

    def aprovado(self):
        return (
            super().aprovado() and self.frequencia >= 75
        )  # Adicionando uma condição de frequência


# Função principal
def main():
    # Recebendo informações do aluno
    nome = input("Digite o nome do aluno: ")
    login = input("Digite o login do aluno: ")
    ra = input("Digite o RA do aluno: ")
    aluno1 = Aluno(nome, login, ra)

    # Recebendo informações da turma
    codigo_turma = input("Digite o código da turma: ")
    nota_turma = float(input("Digite a nota da turma: "))
    turma1 = Turma(codigo_turma, nota_turma)

    # Recebendo informações da turma presencial
    codigo_turma_presencial = input("Digite o código da turma presencial: ")
    nota_turma_presencial = float(input("Digite a nota da turma presencial: "))
    frequencia = float(input("Digite a frequência do aluno (em %): "))
    turma_presencial1 = TurmaPresencial(
        codigo_turma_presencial, nota_turma_presencial, frequencia
    )

    # Verificando a aprovação nas turmas
    print(
        f"{aluno1.nome} está {'aprovado' if turma1.aprovado() else 'reprovado'} na turma {turma1.codigo}."
    )
    print(
        f"{aluno1.nome} está {'aprovado' if turma_presencial1.aprovado() else 'reprovado'} na turma presencial {turma_presencial1.codigo}."
    )


# Executando a função principal
if __name__ == "__main__":
    main()
