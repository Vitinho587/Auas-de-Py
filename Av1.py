# ==============================================================================
# PROVA PRÁTICA AV1 - 3º BIMESTRE
# ARQUIVO: av1_saneamento_dados.py
# Nome do Aluno: João Vitor
# Data: 28/08/2026
# ==============================================================================

# Dados brutos recebidos pelo sistema
cadastros = [
    "  joao da silva;11988887777  ",
    "  maria sousa;21977776666  ",
    "  carlos edgardo oliveira;31966665555  ",
    "  ana paula lima;41955554444  "
]

print("==================================================")
print("       SISTEMA DE ORGANIZAÇÃO DE CADASTROS       ")
print("==================================================\n")

for cadastro in cadastros:
    dados = cadastro.strip()
    nome, telefone = dados.split(";")

    nome_formatado = nome.upper()
    codigo_ddd = telefone[:2]

    print(f"Funcionário: {nome_formatado}")
    print(f"DDD: {codigo_ddd} | Telefone: {telefone}")
    print("-----------------------------------------------")

print("\n==================================================")
print("          DADOS PROCESSADOS COM SUCESSO          ")
print("==================================================")
