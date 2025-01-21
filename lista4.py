
'''
Lista de Exercícios referentes a coleções em python
'''
from biblioteca import *

#print('-------------------------------------------------------------------------------------------------')
#1. Faça um programa que armazene 15 números inteiros em uma lista e depois
#permita que o usuário digite um número inteiro para ser buscado na lista, se
#for encontrado o programa deve imprimir a posição desse número na lista, caso
#contrário, deve imprimir a mensagem: "Nao encontrado!".

def q1():

    numeros = []
    print("Digite 15 números inteiros:")

    for i in range(15):
        num = int(input(f"Digite o {i+1}º número: "))
        numeros.append(num)

    numero_busca = int(input("Digite um número para buscar na lista: "))


    if numero_busca in numeros:
        posicao = numeros.index(numero_busca)
        print(f"O número {numero_busca} foi encontrado na posição {posicao}.")
    else:
        print("Não encontrado!")


#print('-------------------------------------------------------------------------------------------------')
#2. Faça um programa que armazene 10 letras em uma lista e imprima uma listagem
#numerada.

def q2():

    letras = []
    print("Digite 10 letras: ")

    for i in range(10):
        letra = input(f"Digite a {i+1}ª letra: ")
        letras.append(letra)

    print("\nListagem das letras:")
    for i, letra in enumerate(letras, start=1):
        print(f"{i}. {letra}")



#print('-------------------------------------------------------------------------------------------------')
#3. Construa uma programa que armazene 15 números em uma lista e imprima
#uma listagem numerada contendo o número e uma das mensagens: par ou ímpar.

def q3():

    numeros = []
    print("Digite 15 números inteiros:")

    for i in range(15):
        num = int(input(f"Digite o {i+1}º número: "))
        numeros.append(num)

    print("\nListagem dos números com a indicação de par ou ímpar:")
    for i, num in enumerate(numeros, start=1):
        if num % 2 == 0:
            print(f"{i}. {num} - Par")
        else:
            print(f"{i}. {num} - Ímpar")


#print('-------------------------------------------------------------------------------------------------')
#4. Faça um programa que armazene 8 números em uma lista e imprima todos os
#números. Ao final, imprima o total de números múltiplos de seis.

def q4():

    numeros = []

    
    for i in range(8):
        numero = int(input(f"Digite o {i+1}º número: "))
        numeros.append(numero)

    
    print("\nNúmeros inseridos:")
    for numero in numeros:
        print(numero)

    
    multiplo_seis = 0
    for numero in numeros:
        if numero % 6 == 0:
            multiplo_seis += 1

    
    print(f"\nTotal de números múltiplos de seis: {multiplo_seis}")



#print('-------------------------------------------------------------------------------------------------')
#5. Faça um programa que armazene as notas das provas 1 e 2 de 15 alunos. Calcule
#e armazene a média arredondada. Armazene também a situação do aluno: 1-
#Aprovado ou 2-Reprovado. Ao final o programa deve imprimir uma listagem
#contendo as notas, a média e a situação de cada aluno em formato tabulado.
#Utilize quantas listas forem necessárias para armazenar os dados.

def q5():

    soma = 0

    notas_provas = []


    for i in range(1, 3):
        print("\n==============================\n")
        
        print(f"Aluno - {i}\n")


        nome = input('Digite o nome do Aluno: ')
        prova1 = float(input("\nDigite a nota da prova 1: "))
        prova2 = float(input("Digite a nota da prova 2: "))
        notas_provas.append((prova1, prova2))


        media = (prova1 + prova2) / 2
        soma = soma + media

        




    print("\n-----------------------------------------------------")
    print("Notas dos alunos:")
    print("-----------------------------------------------------")


    for i, notas in enumerate(notas_provas, 1):

        print(f"Aluno {i}") 
        print(f"Prova 1: |{notas[0]} | Prova 2: |{notas[1]}|\n")

        print(f'A média do aluno {i} é {media}')


        if media >= 7:
            print(f'Aluno aprovado com a média {media}.')

        else:
            print(f'Aluno Reprovado com media {media}!!!')


    mediageral = soma / i

    print(f'A média geral de turma é: {mediageral}')





#print('-------------------------------------------------------------------------------------------------')
#6. Construa um programa que permita armazenar o salário de 20 pessoas. Calcular
#e armazenar o novo salário sabendo-se que o reajuste foi de 8%. Imprimir uma
#listagem numerada com o salário e o novo salário. Declare quantas listas forem
#necessárias.


def q6():

    # Lista para armazenar os salários
    salarios = []
    novos_salarios = []

    # Entrada dos salários das 20 pessoas
    for i in range(3):
        salario = float(input(f"Digite o salário da {i+1}ª pessoa: R$ "))
        salarios.append(salario)

    # Cálculo do novo salário com reajuste de 8%
    for salario in salarios:
        novo_salario = salario * 1.08  # Reajuste de 8%
        novos_salarios.append(novo_salario)

    # Imprimir a listagem numerada com salários e novos salários
    print("\nListagem dos Salários e Novos Salários:")
    for i in range(3):
        print(f"{i+1}. Salário: R$ {salarios[i]:.2f} -> Novo Salário: R$ {novos_salarios[i]:.2f}")



#print('-------------------------------------------------------------------------------------------------')
#7. Crie um programa que leia o preço de compra e o preço de venda de 100 mercadorias
#(utilize listas). Ao final, o programa deverá imprimir quantas mercadorias
#proporcionam:

#• lucro < 10%
#• 10% <= lucro <= 20%
#• lucro > 20%

def q7():

    produtos = []

    produto = dict()
    precodecompra = float(input('Digite o preço de compra do produto: '))
    precodevenda = float(input('Digite o preço de venda do produto: '))
    produto['precocompra'] = precodecompra
    produtos.append(produto)
    


    print(produto)






#    produto = []
#    precoproduto = []
#    tudo = []


#    for i in range(5):
#        nomeproduto = input(f'Digite o nome do {i+1}ª produto: ')
#        valorproduto = float(input(f"Digite o valor do {i+1}ª produto: R$ "))
#        produto.append(nomeproduto)
#        precoproduto.append(valorproduto)

#        ordem = produto[i],precoproduto[i]
#        tudo.append(ordem)
#    print(tudo)


#print('-------------------------------------------------------------------------------------------------')
#8. Construa um programa que armazene o código, a quantidade, o valor de compra
#e o valor de venda de 30 produtos. A listagem pode ser de todos os produtos ou
#somente de um ao se digitar o código. Utilize dicionário como estrutura de dados.
















#print('-------------------------------------------------------------------------------------------------')
#9. Faça um programa que leia dois conjuntos de números inteiros, tendo
#cada um 10 elementos. Ao final o programa deve listar os elementos comuns aos
#conjuntos.

















#print('-------------------------------------------------------------------------------------------------')
#10. Faça um programa que leia uma lista com 10 elementos e obtenha outra lista resultado
#cujos valores são os fatoriais da lista original.
#Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.

















#print('-------------------------------------------------------------------------------------------------')
#11. Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.

#12. Crie um programa para gerenciar um sistema de reservas de mesas em uma casa
#de espetáculo. A casa possui 30 mesas de 5 lugares cada. O programa deverá
#permitir que o usuário escolha o código de uma mesa (1 a 30) e forneça a
#quantidade de lugares desejados. O programa deverá informar se foi possível
#realizar a reserva e atualizar a reserva. Se não for possível, o programa deverá
#emitir uma mensagem. O programa deve terminar quando o usuário digitar
#o código 0 (zero) para uma mesa ou quando todos os 150 lugares estiverem
#ocupados.

#13. Construa um programa que realize as reservas de passagens áreas de uma companhia.
#O programa deve permitir cadastrar o número de 10 voos e definir a
#quantidade de lugares disponíveis para cada um. Após o cadastro, leia vários
#pedidos de reserva, constituídos do número da carteira de identidade do cliente e
#do número do voo desejado. Para cada cliente, verificar se há possibilidade no
#voo desejado. Em caso afirmativo, imprimir o número da identidade do cliente e
#o número do voo, atualizando o número de lugares disponíveis. Caso contrário,
#avisar ao cliente a inexistência de lugares. A leitura do número 0 (zero) para o voo
#desejado indica o término da leitura de reservas.

#14. Faça um programa que armazene 50 números inteiros em uma lista. O programa
#deve gerar e imprimir uma segunda lista em que cada elemento é o quadrado do
#elemento da primeira lista.

#15. Faça um programa que leia e armazene vários números, até digitar o número
#0. Imprimir quantos números iguais ao último número foram lidos. O limite de
#números é 100.

#16. Crie um programa para ler um conjunto de 100 números reais e informe:
#• quantos números lidos são iguais a 30
#• quantos são maior que a média
#• quantos são iguais a média

#17. Faça um programa que leia um conjunto de 30 valores inteiros, armazene-os em
#um vetor e os imprima ao contrário da ordem de leitura.

#18. Faça um programa que permita entrar com 20 valores numéricos,
# em que podem existir vários elementos repetidos. Gere
#uma lista ordenada que terá apenas os elementos não repetidos.

#19. Suponha uma estrutura de 30 elementos contendo: código e telefone. Faça
#um programa que permita buscar pelo código e imprimir o telefone.

#20. Faça um programa que leia a matrícula e a média de 100 alunos. Ordene da maior
#para a menor nota e imprima uma relação contendo todas as matrículas e médias.




questao = int(input('\nQuestão a ser executada: '))
eval(f'q{questao}()')