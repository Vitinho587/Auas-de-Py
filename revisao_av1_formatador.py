# ==============================================================================
# REVISÃO AV1: MODULARIZAÇÃO E MANIPULAÇÃO DE STRINGS
# ARQUIVO: revisao_av1_formatador.py
# Nome do Aluno:
# Data:
# ==============================================================================

# 1. FUNÇÃO PARA CITAÇÃO BIBLIOGRÁFICA
def formatar_citacao(nome_completo):
    # Separa o nome em partes
    partes = nome_completo.split()

    # Pega o último sobrenome e converte para maiúsculas
    sobrenome = partes[-1].upper()

    # Junta os nomes anteriores
    nome = " ".join(partes[:-1])

    # Retorna no formato "SOBRENOME, Nome"
    return f"{sobrenome}, {nome}"


# 2. FUNÇÃO PARA GERAR CÓDIGO/MATRÍCULA
def gerar_codigo(ano, cpf):
    # Remove espaços extras do CPF
    cpf = cpf.strip()

    # Pega os 3 primeiros dígitos do CPF
    tres_primeiros_digitos = cpf[:3]

    # Retorna a matrícula formatada
    return f"ALU-{ano}-{tres_primeiros_digitos}"


# --- TESTE DAS FUNÇÕES (FLUXO PRINCIPAL) ---

autor = "Carlos Eduardo Andrade"

citacao_formatada = formatar_citacao(autor)
print("Citação Bibliográfica:", citacao_formatada)

matricula = gerar_codigo("2026", "456.789.123-00")
print("Matrícula Gerada :", matricula)
