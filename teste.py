#Faça um programa que leia o valor unitário de um produto, a quantidade desejada e imprima o valor total a pagar.

#valor_unitario = float(input("Informe o valor unitário do produto: "))
#quantidade = float(input("Informe a quantidade do produto: "))
#valor_total = valor_unitario * quantidade
#print("O valor total a ser pago pelo consumidor é:", valor_total)




# Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
# a nota da prova 2, a média das notas e uma das mensagens: "Aprovado", "Reprovado" ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
# reprovação e as demais em prova final).


#nome = str(input('Digite o nome do aluno: '))
#n1 = float(input('Digite a primeira nota do aluno: '))
#n2 = float(input('Digite a primeira nota do aluno: '))

#media = (n1 + n2) / 2

#print('\n')
#print(f'A nota 1 é: {n1}')
#print('\n')
#print(f'A nota 2 é: {n2}')
#print('\n')
#print(f'A média é: {media}')

#print('\n')
#print('--------------------------------------------')
#if media >= 7:
#    print(f'Aluno Aprovado.')
#elif media < 3:
#    print(f'Aluno Reprovado.')
#else:
#    print(f'Aluno ficou de prova final.')
#print('--------------------------------------------')
#print('\n')

# 3. Faça um programa que apresente um menu com 4 opções:
# [1] - Cadastrar
# [2] - Excluir
# [3] - Pesquisar
# [0] - Sair
# O usuário deve escolher uma opção e o programa deve imprimir uma mensagem 
# ao entrar em cada opção do menu. O programa só deve encerrar quando a opção
# escolhida for zero (0).



#while True:

#  print("Menu:")
#  print("1. Opção Cadastrar")
#  print("2. Opção Excluir")
#  print("3. Opção Pesquisar")
#  print("0. Sair")
  
  
#  escolha = input("Escolha uma opção (1/2/3/0): ")
  
  
#  if escolha == "1":
#      print("Você escolheu a Opção Cadastrar.")
    
#  elif escolha == "2":
#      print("Você escolheu a Opção Excluir.")
    
#  elif escolha == "3":
#      print("Você escolheu a Opção  Pesquisar.")
    
#  elif escolha == "0":
#      print("Saindo do programa. Adeus!")
#      break  
#  else:
#      print("Opção inválida. Por favor, escolha uma opção válida.")



#Faça um programa que calcule o retorno de um investimento.
# O programa deve solicitar do usuário o:
#  - valor que será investido;
#  - prazo do investimento (meses);
#  - juros mensal (juros composto).




#C = float(input('Digite o valor do capital: '))
#i = float(input('Digite o valor da taxa: '))
#t = float(input('Digite o tempo: '))

#M = C*(1+i)**t

#print(f'O valor do montante é: {M}')



#    Faça um programa que calcule o valor de uma prestação em atraso.
#    Para isso, o programa deve ler o valor da prestação vencida, a
#    taxa periódica de juros e o período de atraso. Ao final, o
#    programa deve imprimir o valor da prestação atrasada, o período
#    de atraso, os juros que serão cobrados pelo período de atraso, o
#    valor da prestação acrescido dos juros. Considere juros simples.


#valor = float(input ('Digite o valor da prestação:'))
#taxa = float(input ('Digite o valor da taxa:'))
#tempo = float(input ('Digite o tempo atrasado em dias:'))

#juros = (valor * taxa/100 * tempo)
#novovalor = (valor + juros)

#print("\n")

#print(f'O valor da prestação atrasada é : {valor} ')


#print(f'O período de atraso é : {tempo} ')


#print(f'O valor da prestação acrescido dos juros é : {novovalor} ')


#print(f'Os juros que serão cobrados pelo período de atraso é : {juros} ')

#print("\n")