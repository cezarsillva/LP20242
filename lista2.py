'''
Exercícios sobre os comandos de condição em python
'''
#---------------------------------------------------------------------------------------------------------------------------------------#
#1. Faça um programa que leia dois valores numéricos inteiros e efetue
#   a adição, caso o resultado seja maior que 10, apresentá-lo.


#num1 = int(input('Digite o primeiro número: '))
#num2 = int(input('Digite o segundo número: '))


#soma = (num1 + num2)


#if soma >= 10:
#    print(f'A soma é maior que 10: {soma}')
#else:
#    print(f'A soma é menor que 10. {soma}')


#---------------------------------------------------------------------------------------------------------------------------------------#
#2. Faça um programa que leia dois valores inteiros e efetue a adição.
#   Caso o valor somado seja maior que 20, este deverá ser apresentado
#   somando-se a ele mais 8, caso o valor somado seja menor ou igual a
#   20, este deverá ser apresentado subtraindo-se 5.


#valor1 = int(input('Digite o primeiro valor: '))
#valor2 = int(input('Digite o segundo valor: '))

#soma = valor1 + valor2

#if soma > 20:
#    print(f'O Valor somado é {soma} então adiciona 8 : {soma + 8}')

#elif soma <= 20:
#    print(f'O valor somado é {soma} então subtrai 5 : {soma - 5}')


#---------------------------------------------------------------------------------------------------------------------------------------#
#3. Faça um programa que leia um número e imprima uma das duas mensagens:
#   "É múltiplo de 3"ou "Não é múltiplo de 3".


#num = int(input('Digite o valor: '))

#if num % 3 == 0:
#    print(f' O valor {num} é múltiplo de 3.')
#else:
#    print(f'O valor não é múltiplo de 3.')



#---------------------------------------------------------------------------------------------------------------------------------------#
#4. Faça um programa que leia um número e informe se ele é ou não divisível por 5.


#num = int(input('Digite o valor desejado: '))


#if num % 5 == 0:
#    print(f' O valor {num} é divisível de 5.')
#else:
#    print(f'O valor {num} não é divisível de 5.')
   

#---------------------------------------------------------------------------------------------------------------------------------------#
#5. Faça um programa que leia um número e informe se ele é divisível por 3 e por 7.

#num = int(input('Digite o número desejado: '))


#if num % 3 == 0 and num % 7 == 0:
#    print(f'O valor digitado é divisível por 3 e por 7.')

#else:
#    print(f'O valor digitado não é divisível por 3 e nem por 7.')

#---------------------------------------------------------------------------------------------------------------------------------------#
#6. A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários
#   estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
#   bruto. Faça um programa que permita entrar com o salário bruto
#   e o valor da prestação e informar se o empréstimo pode ou não ser concedido.


#salario_bruto = float(input('Digite o Salário Bruto: '))
#valor_prestacao = float(input('Digite o valor da pretação: '))


#if valor_prestacao > salario_bruto * 0.3:
#    print(f'Emprestimo não liberado.')
#else:
#    print(f'Emprestimo  liberado.')




#---------------------------------------------------------------------------------------------------------------------------------------#
#7. Faça um programa que leia um número e indique se o número está compreendido
#   entre 20 e 50 ou não.


#num = int(input('Digite um número qualquer: '))


#if num > 20 and num < 50:
#    print(f'Valor está entre os números 20 e 50. ')
#else:
#    print(f'Valor não está entre os números 20 e 50. ')



#---------------------------------------------------------------------------------------------------------------------------------------#
#8. Faça um programa que leia um número e imprima uma das mensagens:
#   "Maior do que 20", "Igual a 20"ou "Menor do que 20".

#num = int(input('Digite um número qualquer: '))


#if num > 20:
#    print(f'O número é maior que 20. ')
#elif num == 20:
#    print(f'O número é igual a 20. ')
#else:
#    print(f'O número é menor que 20. ')


#---------------------------------------------------------------------------------------------------------------------------------------#
#9. Faça um programa que permita entrar com o ano de nascimento da pessoa e com o
#   ano atual. O programa deve imprimir a idade da pessoa. Não se esqueça de
#   verificar se o ano de nascimento informado é válido.



#ano_nascimento = int(input('Digite o ano de nascimento da pessoa: '))
#ano_atual = int(input('Digite o ano atual: '))


#idade_pessoa = (ano_atual - ano_nascimento)

#if ano_nascimento > ano_atual:
    #print(f'O ano do nascimento é inválido.')
#else:
    #print(f'A idade da pessoa é: {idade_pessoa} anos.')


#---------------------------------------------------------------------------------------------------------------------------------------#
#10. Faça um programa que leia três números inteiros e imprima os três em ordem
#crescente.



#num1 = int(input('Digite o primeiro número: '))
#num2 = int(input('Digite o segundo número: '))
#num3 = int(input('Digite o terceiro número: '))



#if num1 < num2 < num3:
    
    #print(f' {num1} - {num2} - {num3} ')

#elif num1 < num3 < num2:
    
    #print(f' {num1} - {num3} - {num2} ')

#elif num2 < num1 < num3:
    
    #print(f' {num2} - {num1} - {num3} ')

#elif num2 < num3 < num1:
    
    #print(f' {num2} - {num3} - {num1} ')

#elif num3 < num1 < num2:
    
    #print(f' {num3} - {num1} - {num2} ')

#elif num3 < num2 < num1:
    
    #print(f' {num3} - {num2} - {num1} ')



#---------------------------------------------------------------------------------------------------------------------------------------#
#11. Faça um programa que leia 3 números e imprima o maior deles.


#num1 = int(input ('Digite o primeiro número: '))
#num2 = int(input ('Digite o segundo número: '))
#num3 = int(input ('Digite o terceiro número: '))

# if num1 > num2 > num3:
    
#     print(f' {num1}  ')

# elif num1 > num3 > num2:
    
#     print(f' {num1} ')

# elif num2 > num1 > num3:
    
#     print(f' {num2} ')

# elif num2 > num3 > num1:
    
#     print(f' {num2} ')

# elif num3 > num1 > num2:
    
#     print(f' {num3} ')

# elif num3 > num2 > num1:
    
#     print(f' {num3} ')


#---------------------------------------------------------------------------------------------------------------------------------------#
#12. Faça um programa que leia a idade de uma pessoa e informe:
#• Se é maior de idade
#• Se é menor de idadea
#• Se é maior de 65 anos


# idade = int(input('Digite a idade da Pessoa: '))


# if idade < 18:
#     print('A pessoa é menor de 18 anos.')
# elif idade >= 18 and idade < 65:
#     print('A pessoa é maior de idade.')
# else:
#     print('A pessoa tem mais de 65 anos')


#---------------------------------------------------------------------------------------------------------------------------------------#
#13. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
#da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
#a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
#"Reprovado"ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
#reprovação e as demais em prova final).



# nome = str(input('Digite o nome do aluno: '))
# nota1 = float(input('Digite a primeira nota do aluno: '))
# nota2 = float(input('Digite a segunda nota do aluno: '))


# media = (nota1 + nota2) / 2

# print(f'A media do aluno {nome} é: {media}')


# if media >= 7:
#     print('Aluno aprovado.')
# elif media < 3:
#     print('Aluno reprovado.')
# else:
#     print('Aluno prova final.')

#---------------------------------------------------------------------------------------------------------------------------------------#
#14. Faça um programa que permita entrar com o salário de uma pessoa e imprima o
#desconto do INSS segundo a tabela seguir:
#Salário Faixa de Desconto
#Menor ou igual à R$600,00 Isento
#Maior que R$600,00 e menor ou igual a R$1200,00 20%
#Maior que R$1200,00 e menor ou igual a R$2000,00 25%
#Maior que R$2000,00 30%



# salario = float(input('Digite o valor do salário: '))

# if salario <= 600:
#     print('Isento de Taxa.')
# elif salario > 600 and salario <=1200:
#     print('O desconto será de 20%.')
# elif salario > 1200 and salario <= 2000:
#     print('O desconto será de 25%. ')
# else:
#     print('O desconto é de 30%.')


#---------------------------------------------------------------------------------------------------------------------------------------#
#15. Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o
#valor da compra for menor que R$20,00, caso contrário, o lucro será de 30%.
#Faça um programa que leia o valor do produto e imprima o valor da venda.


# valor_produto = float(input('Digite o valor do produto: '))


# lucro1 = valor_produto * 45 / 100
# lucro2 = valor_produto * 30 / 100

# if valor_produto < 20:
#     print(f'O valor da venda é: {valor_produto + lucro1}')
# else:
#     print(f'O valor da venda é {valor_produto + lucro2}')



#---------------------------------------------------------------------------------------------------------------------------------------#
#16. A confederação brasileira de natação irá promover eliminatórias para o
#próximo mundial. Faça um programa que receba a idade de um nadador e imprima
#a sua categoria segundo a tabela a seguir:
#Categoria Idade
#Infantil A 5 - 7 anos
#Infantil B 8 - 10 anos
#Juvenil A 11 - 13 anos
#Juvenil B 14 - 17 anos
#Sênior maiores de 18 anos


# idade = int(input('Digite a idade do jogador: '))


# if idade > 0 and  idade < 5:
#     print(f'Sem categoria.')
# elif idade > 5 and idade < 7:
#     print(f'Categoria Infantil A .')
# elif idade > 8 and idade < 10:
#     print(f'Categoria Infantil B.')
# elif idade > 11 and idade < 13:
#     print(f'Categoria Juvenil A.')
# elif idade >14 and idade < 17:
#     print(f'Categoria Juvenil B.')
# else:
#     print(f'Categoria senior.')



#---------------------------------------------------------------------------------------------------------------------------------------#
#17. Depois da liberação do governo para as mensalidades dos planos de saúde,
#as pessoas começaram a fazer pesquisas para descobrir um bom plano, não
#muito caro. Um vendedor de um plano de saúde apresentou a tabela a seguir.
#Faça um programa que entre com o nome e a idade de uma pessoa e imprima o
#nome e o valor que ela deverá pagar.
#Idade Valor
#Até 10 anos R$30,00
#Acima de 10 até 29 anos R$60,00
#Acima de 29 até 45 anos R$120,00
#Acima de 45 até 59 anos R$150,00
#Acima de 59 até 65 anos R$250,00
#Maior que 65 anos R$400,00


# nome = str(input('Digite o nome do beneficiario: '))
# idade = int(input('Digite a idade do beneficiario: '))


# if idade <= 10:
#     print(f'O beneficiario {nome} pagara o valor de R$ 30,00.')
# elif idade > 10 and  idade < 29:
#     print(f'O beneficiario {nome} pagara o valor de R$ 60,00.')
# elif idade > 29 and  idade < 45:
#     print(f'O beneficiario {nome} pagara o valor de R$ 120,00.')
# elif idade > 45 and  idade < 59:
#     print(f'O beneficiario {nome} pagara o valor de R$ 150,00.')
# elif idade > 59 and  idade < 65:
#     print(f'O beneficiario {nome} pagara o valor de R$ 250,00.')
# else:
#     print(f'O beneficiario {nome} pagara o valor de R$ 400,00')


#---------------------------------------------------------------------------------------------------------------------------------------#
#18. Faça um programa que leia um número inteiro entre 1 e 12 e escreva o mês
#correspondente. Caso o usuário digite um número fora desse intervalo, deverá
#aparecer uma mensagem informando que não existe mês com este número.

# mes = int(input('Digite o um número de 1 a 12 de acordo com o mês correspondente: '))

# if mes == 1:
#     print(f'JANEIRO')
# elif mes == 2:
#     print(f'FEVEREIRO')
# elif mes == 3:
#     print(f'MARÇO')
# elif mes == 4:
#     print(f'ABRIL')
# elif mes == 5:
#     print(f'MAIO')
# elif mes == 6:
#     print(f'JUNHO')
# elif mes == 7:
#     print(f'JULHO')
# elif mes == 8:
#     print(f'AGOSTO')
# elif mes == 9:
#     print(f'SETEMBRO')
# elif mes == 10:
#     print(f'OUTUBRO')
# elif mes == 11:
#     print(f'NOVEMBRO')
# elif mes == 12:
#     print(f'NOVEMBRO')
# else:
#     print(f'MÊS INVÁLIDO')


##########################################################################################################################################

#Exemplo Prof com biblioteca:

# mes = int(input('Digite o um número de 1 a 12 de acordo com o mês correspondente: '))

# if mes <1 or me >12:
#     print('Mês Inválido')
# else:
#     data = datetime.strptime(f'01/{mes}/24','%d/%m/%y')
#     mes_extenso = data.strftime('%B')
#     print(tradutor.translate(mes_extenso))


##########################################################################################################################################

#---------------------------------------------------------------------------------------------------------------------------------------#
#19. Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores
#para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o
#mesmo número de pontos, criar um programa que informe se uma equipe foi
#classificada, de acordo com a seguinte especificação:
#• Ler os pontos obtidos por cada jogador da equipe;
#• Mostrar esses valores em ordem decrescente;
#• Se a soma dos pontos for maior do que 100, imprimir a média aritmética entre eles,
#  caso contrário, imprimir a mensagem "Equipe desclassificada".


# jogador1= float(input ('Digite a nota do primeiro jogador: '))
# jogador2= float(input ('Digite a nota do segundo jogador: '))
# jogador3= float(input ('Digite a nota do primeiro jogador: '))


# soma = jogador1 + jogador2 + jogador3


# if soma > 100:
#     print(f'Resultado maior que 100 então sua média é: {soma / 3}.')
#     print(f'"A equipe foi classificada."')
# else:
#     print(f'Equipe Desclassificada.')

# if jogador1 > jogador2 > jogador3:
    
#     print(f' {jogador1} - {jogador2} - {jogador3} ')

# elif jogador1 > jogador3 > jogador2:
    
#     print(f' {jogador1} - {jogador3} - {jogador2} ')

# elif jogador2 > jogador1 > jogador3:
    
#     print(f' {jogador2} - {jogador1} - {jogador3} ')

# elif jogador2 > jogador3 > jogador1:
    
#     print(f' {jogador2} - {jogador3} - {jogador1} ')

# elif jogador3 > jogador1 > jogador2:
    
#     print(f' {jogador3} - {jogador1} - {jogador2} ')

# elif jogador3 > jogador2 > jogador1:
    
#     print(f' {jogador3} - {jogador2} - {jogador1} ')

# else:
#     print('Erro desconhecido.')

#---------------------------------------------------------------------------------------------------------------------------------------#
#20. O banco XXX concederá um crédito especial com juros de 2% aos seus clientes de
#acordo com o saldo médio no último ano. Faça um programa que leia o saldo médio
#de um cliente e calcule o valor do crédito de acordo com a tabela a seguir.
#O programa deve imprimir uma mensagem informando o saldo médio e o valor de
#crédito.
#Saldo Médio Percentual
#de 0 a 500 nenhum crédito
#de 501 a 1000 30% do valor do saldo médio
#de 1001 a 3000 40% do valor do saldo médio
#acima de 3001 50% do valor do saldo médio


# saldo = int(input('Digite o saldo do cliente: '))


# if saldo > 0 and saldo < 500:
#     print(f'Nenhum crédito.')
# elif saldo > 501 and saldo < 1000:
#     print(f'O cliente tem direito a 30% do valor do saldo médio. ')
# elif saldo > 1001 and saldo < 3000:
#     print(f'O cliente tem direito a 40% do valor do saldo médio. ')
# else:
#     print(f'O cliente tem direito a 50% do valor do saldo médio. ')


#---------------------------------------------------------------------------------------------------------------------------------------#
#21. A biblioteca de uma Universidade deseja fazer um programa que leia o nome do
#livro que será emprestado, o tipo de usuário (professor ou aluno) e possa
#imprimir um recibo conforme mostrado a seguir. Considerar que o professor
#tem dez dias para devolver o livro e o aluno só três dias.
#• Nome do livro:
#• Tipo de usuário:
#• Total de dias:
nome = str(input('Digite o nome do Usuário: '))
nome_livro = str(input('Digite o nome do Livro: '))
usuario = int(input('Digite para Aluno: 1 e para Professor: 2: '))
total_dias = int(inpu('Digite para Aluno: 3 e para Professor 10: '))



if usuario == 1 and total_dias == 3:
    print(f'O usuário é {nome} e tem {total_dias} dias para devolução do livro {nome_livro} ')

































#---------------------------------------------------------------------------------------------------------------------------------------#
#22. Construa um programa que leia o percurso em quilômetros, o tipo do carro e
#informe o consumo estimado de combustível, sabendo-se que um carro tipo A faz
#12 km com um litro de gasolina, um tipo B faz 9 km e o tipo C 8 km por litro.




































#---------------------------------------------------------------------------------------------------------------------------------------#
#23. Crie um programa que informe a quantidade total de calorias de uma refeição
#a partir da escolha do usuário que deverá informar o prato, a sobremesa, e
#bebida conforme a tabela a seguir.
#Prato  Sobremesa   Bebida
#Vegetariano    180cal Abacaxi          75cal  Chá               20cal
#Peixe          230cal Sorvete diet     110cal Suco de laranja   70cal
#Frango         250cal Mousse diet      170cal Suco de melão     100cal
#Carne          350cal Mousse chocolate 200cal Refrigerante diet 65cal

































#---------------------------------------------------------------------------------------------------------------------------------------#
#24. A polícia rodoviária resolveu fazer cumprir a lei e vistoriar veículos para
#cobrar dos motoristas o DUT. Sabendo-se que o mês em que o emplacamento do
#carro deve ser renovado é determinado pelo último número da placa do mesmo,
#faça um programa que, a partir da leitura da placa do carro, informe o mês
#em que o emplacamento deve ser renovado.







































#---------------------------------------------------------------------------------------------------------------------------------------#
#25. A prefeitura contratou uma firma especializada para manter os níveis de
#poluição considerados ideais para um país do 1º mundo. As indústrias,
#maiores responsáveis pela poluição, foram classificadas em três grupos.
#Sabendo-se que a escala utilizada varia de 0,05 e que o índice de poluição
#aceitável é até 0,25, fazer um programa que possa imprimir intimações de
#acordo com o índice e a tabela a seguir:
#Índice Indústrias que receberão intimação
#0,3 1º grupo
#0,4 1º e 2º grupos
#0,5 1º, 2º e 3º grupos