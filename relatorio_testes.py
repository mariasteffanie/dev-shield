<<<<<<< HEAD

# Nome do aluno: Gustavo Emidio
# Este programa apresenta um relatório com os resultados
# de uma execução de testes do sistema LearnHub EdTech.

=======
# Nome do aluno: Gustavo Emidio
# Este programa apresenta um relatório com os resultados
# de uma execução de testes do sistema LearnHub EdTech.

>>>>>>> 36b5a4b0a6159ceea28f0fa82bb53f856ec4b82f
# Aqui guardamos as informações principais do projeto.
projeto = "LearnHub EdTech"
modulo = "Emissão de Certificados e Validação de Notas"
responsavel = "Gabriel Souza"
data_execucao = "10/11/2026"

# Nesta parte informamos quantos testes foram aprovados,
# quantos foram reprovados e quantos ainda não foram executados.
testes_aprovados = 28
testes_reprovados = 14
testes_nao_executados = 8

# Somamos as três quantidades para descobrir o total de testes.
total_testes = testes_aprovados + testes_reprovados + testes_nao_executados

# Começamos a montar o relatório que será mostrado no terminal.
# Os sinais de igual servem para deixar a apresentação mais organizada.
print("=" * 50)
print("       RELATÓRIO DE EXECUÇÃO DE TESTES")
print("=" * 50)

# Aqui mostramos os dados do projeto que foram guardados nas variáveis.
# Usamos f-string para inserir os valores dentro dos textos.
print(f"Projeto: {projeto}")
print(f"Módulo: {modulo}")
print(f"Responsável: {responsavel}")
print(f"Data da execução: {data_execucao}")

# Esta linha separa as informações do projeto dos resultados dos testes.
print("-" * 50)

# Agora apresentamos a quantidade de testes de cada situação.
print(f"Testes aprovados: {testes_aprovados}")
print(f"Testes reprovados: {testes_reprovados}")
print(f"Testes não executados: {testes_nao_executados}")

# Outra linha para separar os resultados do total de testes.
print("-" * 50)

# Mostramos a soma de todos os testes realizados ou não executados.
print(f"Total de testes: {total_testes}")

# Finalizamos o relatório indicando que a inicialização foi concluída.
print("=" * 50)
print("       INICIALIZAÇÃO CONCLUÍDA")
print("=" * 50)

