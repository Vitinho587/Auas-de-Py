# Dados no formato: "nome_completo;cargo_ou_setor;telefone_ou_cpf"
dados_brutos = [
   "  carlos eduardo silva;desenvolvedor;11988887777  ",
   "  ana paula mendes;analista de rh;21977776666  ",
   "  roberto carlos oliveira;gerente de projetos;31966665555  "
]

def limpar_e_formatar_texto(texto):
   """Remove espaços das pontas e converte para MAIÚSCULAS."""
   return texto.strip().upper()

def extrair_codigo_ou_ddd(dado):
   """Remove espaços e extrai os 2 primeiros dígitos via fatiamento."""
   return dado.strip()[0:2]

def processar_e_exibir_cadastros(lista_dados):
   """Percorre a lista com for, formata e exibe cada cadastro; retorna o total."""
   contador = 0
   for registro in lista_dados:
       nome, cargo, telefone = registro.split(";")
       print(f"Nome: {limpar_e_formatar_texto(nome)} | Cargo: {limpar_e_formatar_texto(cargo)} | DDD: {extrair_codigo_ou_ddd(telefone)}")
       contador += 1
   return contador

def main():
   print("SISTEMA DE GESTÃO MODULARIZADO - AV2\n")
   total_processado = processar_e_exibir_cadastros(dados_brutos)
   print(f"\nTotal de registros processados: {total_processado}")
   print("PROCESSAMENTO CONCLUÍDO")

if __name__ == "__main__":
   main()

   # ==============================================================================
# PROVA PRÁTICA AV2 - 3º BIMESTRE | ARQUIVO: av2_sistema_modular.py
# Nome do Aluno: João Vitor       Data:18/09     Link do Repositório:  classe:1B T.I
# ==============================================================================
