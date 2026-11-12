projeto = "LearnHub EdTech"
modulo = "Emissão de Certificados e Validação de Notas"
responsavel = "Gabriel Souza"
data_execucao = "10/11/2026"
testes_aprovados = 28
testes_reprovados = 14
testes_nao_executados = 8


print("========================================RELATÓRIO DE EXECUÇÃO DE TESTES========================================")
print("Projeto: " + projeto)
print("Módulo: " + modulo)
print("Responsável: " + responsavel)
print("Data: " + data_execucao)
print("Testes Aprovados: " + str(testes_aprovados))
print("Testes Reprovados: " + str(testes_reprovados))
print("Testes Não Executados: " + str(testes_nao_executados))


print("---------------------------------------- RESULTADOS REGISTRADOS ----------------------------------------")


total_testes = testes_aprovados + testes_reprovados + testes_nao_executados
print("Total de Testes: " + str(total_testes))

taxa_de_aprovacao = testes_aprovados / total_testes * 100
print("taxa_de_aprovacao: " + str(taxa_de_aprovacao) + "%")