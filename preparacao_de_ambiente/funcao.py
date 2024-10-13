# Função para criar um aluno
def criar_aluno(nome, login, ra):
    return {"nome": nome, "login": login, "ra": ra}


# Função para criar uma turma
def criar_turma(codigo, nota):
    return {"codigo": codigo, "nota": nota}


# Função que verifica se o aluno foi aprovado em uma turma
def aprovado_turma(turma):
    return turma["nota"] >= 6


# Função para criar uma turma presencial
def criar_turma_presencial(codigo, nota, frequencia):
    return {"codigo": codigo, "nota": nota, "frequencia": frequencia}


# Função que verifica se o aluno foi aprovado em uma turma presencial (nota e frequência)
def aprovado_turma_presencial(turma_presencial):
    return turma_presencial["nota"] >= 6 and turma_presencial["frequencia"] >= 75


# Função principal
def main():
    # Recebendo informações do aluno
    nome = input("Digite o nome do aluno: ")
    login = input("Digite o login do aluno: ")
    ra = input("Digite o RA do aluno: ")
    aluno1 = criar_aluno(nome, login, ra)

    # Recebendo informações da turma
    codigo_turma = input("Digite o código da turma: ")
    nota_turma = float(input("Digite a nota da turma: "))
    turma1 = criar_turma(codigo_turma, nota_turma)

    # Recebendo informações da turma presencial
    codigo_turma_presencial = input("Digite o código da turma presencial: ")
    nota_turma_presencial = float(input("Digite a nota da turma presencial: "))
    frequencia = float(input("Digite a frequência do aluno (em %): "))
    turma_presencial1 = criar_turma_presencial(
        codigo_turma_presencial, nota_turma_presencial, frequencia
    )

    # Verificando a aprovação nas turmas
    print(
        f"{aluno1['nome']} está {'aprovado' if aprovado_turma(turma1) else 'reprovado'} na turma {turma1['codigo']}."
    )
    print(
        f"{aluno1['nome']} está {'aprovado' if aprovado_turma_presencial(turma_presencial1) else 'reprovado'} na turma presencial {turma_presencial1['codigo']}."
    )


# Executando a função principal
if __name__ == "__main__":
    main()
