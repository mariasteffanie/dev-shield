
nome = input("qual é o nome do seu pet? ")
idade_humano = input("qual é a idade do seu pet? ")
idade_pet = int(idade_humano) * 7

print ("qual é o porte do seu pet?")
print ("1 - pequeno")
print ("2 - médio")
print ("3 - grande")
porte = input("Digite o número correspondente ao porte do seu pet: ")

if porte == "1":
    valor_banho = 50.00
    custo_banho = 5.00
elif porte == "2":
    valor_banho = 60.00
    custo_banho = 15.00
elif porte == "3":
    valor_banho = 75.00
    custo_banho = 20.00
else:
    print ("Opção inválida")

banhos = input("quantos banhos o seu pet toma por ano? ")
lucro_banho = int(banhos) * (valor_banho - custo_banho)

print ("O nome do seu pet é: " + nome + " e a"
" idade dele em anos de cachorro é: " + str(idade_pet))
print ("O lucro com banhos por ano é: R$ " + str(lucro_banho))